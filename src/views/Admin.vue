<template>
    <div class="m-4">
        <UButton disabled>Get Character</UButton>
        <hr class="my-4">
        <UForm class="flex flex-col w-fit gap-2" @submit="onSubmit" :state="state">
            <UFormField label="Name" name="name">
                <UInput v-model="state.name"/>
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
import { reactive } from 'vue'

const toast = useToast()


const state = reactive({
  name: '',
  ban: false,
  file: null
})


async function handleFileChange(e) {
    state.file = e.target.files[0]
}

async function onSubmit() {
    

    const form_data = new FormData()
    form_data.append('name', state.name)
    form_data.append('ban', state.ban)
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