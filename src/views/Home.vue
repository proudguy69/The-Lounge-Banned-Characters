<template>
 
    <UCard class="mx-4 my-4">

        <UAccordion type="multiple" :items="categories" class="px-4">

            <!--
            <template #genshin="{ item }">
                <div class="mx-4 flex gap-2 justify-center flex-wrap">
                    <CharacterPreview v-for="char in genshin" :name="char.name" :ban="char.ban" :primary_image="char.primary_image" />
                </div>
                
            </template>-->


            <template #Genshin_Impact="{ item }">
                <div class="mx-4 flex gap-2 justify-center flex-wrap">
                    <CharacterPreview v-for="char in category_data.Genshin_Impact" :name="char.name" :ban="char.ban" :primary_image="char.primary_image" />
                </div>
            </template>

            <template #Honkai_Star_Rail="{ item }">
                <div class="mx-4 flex gap-2 justify-center flex-wrap">
                    <CharacterPreview v-for="char in category_data.Honkai_Star_Rail" :name="char.name" :ban="char.ban" :primary_image="char.primary_image" />
                </div>
            </template>

            <template #Spy_x_Family="{ item }">
                <div class="mx-4 flex gap-2 justify-center flex-wrap">
                    <CharacterPreview v-for="char in category_data.Spy_x_Family" :name="char.name" :ban="char.ban" :primary_image="char.primary_image" />
                </div>
            </template>


            <template #uncatagorized="{ item }">
                test!
                <div class="mx-4 flex gap-2 justify-center flex-wrap">
                    <CharacterPreview v-for="char in uncatagorized" :name="char.name" :ban="char.ban" :primary_image="char.primary_image" />
                </div>
            </template>


        </UAccordion>

    </UCard>
    
</template>



<script setup>
import { ref, onMounted } from 'vue'
import CharacterPreview from '@/components/CharacterPreview.vue'



const categories = ref([
    {
        label: "Uncatagorized",
        slot: 'uncatagorized'
    },
])

const category_data = ref({
    uncatagorized: []
})


const characters = []
const uncatagorized = ref([])

async function getCharacters() {
    const response = await fetch('/api/characters')
    const response_json = await response.json()
    const characters = response_json.characters


    for (let i=0; i < characters.length; i++) {
        const char = characters[i]
        category_data.value[char.category.replace(/ /g, '_')].push(char)
    }

    console.log(category_data)
}

async function getCategories() {
    const response = await fetch('/api/categories')
    const data = await response.json()
    for (let i=0; i < data.categories.length; i++) {
        categories.value.push({
            label: data.categories[i],
            slot: data.categories[i].replace(/ /g, '_')
        })
        category_data.value[data.categories[i].replace(/ /g, '_')] = []
    }

    console.log(categories.value)
    console.log(category_data.value)
}

onMounted(async () => {
    await getCategories()
    await getCharacters()
})

</script>

