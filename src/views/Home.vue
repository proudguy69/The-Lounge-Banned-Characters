<template>
    <div class="mx-4 flex gap-2 justify-center flex-wrap">
        <div class="relative cursor-pointer" v-for="character in characters">
            <p class="absolute left-2 top-2 font-bold text-2xl bg-black/25">{{character.name}}</p>
            <img :src="'@/../backend/'+character.primary_image" class="h-80 border-2 border-amber-300" :class="{ 'border-red-300': character.ban}">
        </div>
    </div>
</template>



<script setup>
import { ref, onMounted } from 'vue'

const characters = ref([
    
])

async function getCharacters() {
    const response = await fetch('/api/characters')
    const response_json = await response.json()
    characters.value = response_json.characters
}

onMounted(async () => {
    await getCharacters()
})

</script>

<style>

</style>