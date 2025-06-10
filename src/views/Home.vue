<template>
 
    <UCard class="mx-4 my-4">

        <UAccordion type="multiple" :items="categories" class="px-4">

            <template #genshin="{ item }">
                <div class="mx-4 flex gap-2 justify-center flex-wrap">
                    <CharacterPreview v-for="char in genshin" :name="char.name" :ban="char.ban" :primary_image="char.primary_image" />
                </div>
                
            </template>

            <template #uncatagorized="{ item }">
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
        label: "Genshin Impact",
        slot: 'genshin'
    },
    {
        label: "Uncatagorized",
        slot: 'uncatagorized'
    },
])


const characters = []
const genshin = ref([])
const uncatagorized = ref([])

async function getCharacters() {
    const response = await fetch('/api/characters')
    const response_json = await response.json()
    const characters = response_json.characters


    for (let i=0; i < characters.length; i++) {
        const char = characters[i]
        if (char.category == "Genshin Impact") {
            genshin.value.push(char)
        } else {
            uncatagorized.value.push(char)
        }
    }
}

onMounted(async () => {
    await getCharacters()
})

</script>

