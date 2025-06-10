<template>
    <div class="m-4">
        <UButton disabled>Get Character</UButton>
        <hr class="my-4">
        <UForm class="flex flex-col w-fit gap-2" @submit="onSubmit" :state="state">
            <UFormField label="Name" name="name">
                <UInput v-model="state.name"/>
            </UFormField>

            <UFormField label="category" name="category">
                <UInputMenu @create="createCategory" v-model="state.category" :items="categories" create-item/>
            </UFormField>

            <UFormField label="Ban" name="ban">
                <USwitch v-model="state.ban"/>
            </UFormField>

            <UFormField label="Primary Image" name="file">
                <UInput @change="handleFileChange" type="file"/>
            </UFormField>

            <UButton type="submit">Upload</UButton>
        </UForm>
    </div>
    
</template>

<script setup>
import { reactive, ref, onMounted } from 'vue'

const toast = useToast()


const categories = ref(['Uncatagorized'])


const state = reactive({
  name: '',
  category: '',
  ban: false,
  file: null
})




onMounted(async () => {
    const response = await fetch('/api/categories')
    const data = await response.json()
    for (let i=0; i < data.categories.length; i++) {
        categories.value.push(data.categories[i])
    }
})

function createCategory(name) {
    categories.value.push(name)

    state.category = name
}

async function handleFileChange(e) {
    state.file = e.target.files[0]
}





async function onSubmit() {
    

    const form_data = new FormData()
    form_data.append('name', state.name)
    form_data.append('ban', state.ban)
    form_data.append('category', state.category)
    form_data.append('file', state.file)

    const response = await fetch('/api/characters/upload', {
        method: 'POST',
        body: form_data
    })
    if (response.status != 200) {
        console.log(response)
        toast.add({title: "Error", description: `An error occured: ${response.status} ${response.statusText}`, color: 'error'})
        return
    } else {
        toast.add({title: "Character added", color: 'primary'})
    }
    const response_json = await response.json()
    console.log(response_json)
}

</script>