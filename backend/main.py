from fastapi import FastAPI, UploadFile, File, Form
from uvicorn import run
from typing import Annotated
from uuid import uuid4
import shutil
import os
from pymongo import MongoClient

app = FastAPI(debug=True)
client = MongoClient('mongodb://localhost:27017')
database = client.get_database('lounge')
characters = database.get_collection('characters')


UPLOAD_DIRECTORY = 'images'
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)



class Character:
    def __init__(self, data:dict):
        self._id = str(data.get('_id'))
        self.name = data.get('name')
        self.ban = data.get('ban')
        self.category = data.get('category')
        self.primary_image = data.get('primary_image')

    
    @classmethod
    def new(cls, name:str, category:str, ban:bool, file:UploadFile):

        unique_filename = f"{uuid4()}{os.path.splitext(file.filename)[1]}"
        file_location = os.path.join(UPLOAD_DIRECTORY, unique_filename)

        with open(file_location, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)

        data = {
            "name": name,
            "category": category,
            "ban": ban,
            "primary_image": file_location
        }

        characters.insert_one(data)
        
        return Character(data)

        

@app.post('/api/characters/upload')
async def character_upload(name:Annotated[str, Form()], category:Annotated[str, Form()], ban:Annotated[bool, Form()], file:Annotated[UploadFile, File()]):

    char = Character.new(name, category, ban, file)

    return {'success':True, 'character': char.__dict__}
    

@app.get('/api/characters')
async def api_characters():
    characters_list = [Character(data).__dict__ for data in characters.find()]

    return {'success': True, 'characters': characters_list}

@app.get('/api/categories')
async def api_categories():
    characters_list = characters.find()
    categories = set(Character(c).category for c in characters_list)

    return {'success': True, 'categories': categories}



run(app)