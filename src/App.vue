<template>
    <UApp>
        <UAlert title="Any issues contact Paul (1267552151454875751)" />
        <UNavigationMenu :items="items" highlight/>
        <router-view></router-view>
    </UApp>
    
</template>

<script setup>
import { ref } from 'vue'

const items = ref([
    {
        label: "Characters",
        to :'/'
    },
    {
        label: "Admin portal",
        to: '/admin'
    },
    {
        label: 'github',
        to: 'https://github.com/proudguy69/The-Lounge-Banned-Characters',
        icon: 'mdi:github'
    }
])



</script>