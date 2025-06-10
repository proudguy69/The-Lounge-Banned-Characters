<template>

    <div class="relative cursor-pointer">
        <p class="absolute left-2 top-2 font-bold text-2xl bg-black/25">{{name}}</p>
        <img :src="'@/../backend/'+primary_image" class="h-80 border-2 border-amber-300" :class="{ 'border-red-300': ban}">
    </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps(['name', 'ban', 'primary_image'])

</script>