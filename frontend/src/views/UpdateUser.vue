<template>
  <div class="max-w-md mx-auto bg-white border rounded p-6 shadow-sm">
    <h2 class="text-xl font-semibold text-center mb-4">UPDATE USER</h2>

    <form @submit.prevent="onSubmit" class="space-y-3">
      <div>
        <label class="block mb-1">Nama Lengkap</label>
        <input
          v-model.trim="form.name"
          type="text"
          class="w-full border rounded px-3 py-2"
          required
        />
      </div>
      <div>
        <label class="block mb-1">Email</label>
        <input
          v-model.trim="form.email"
          type="email"
          class="w-full border rounded px-3 py-2"
          required
        />
      </div>
      <div>
        <label class="block mb-1">Username</label>
        <input
          v-model.trim="form.username"
          type="text"
          class="w-full border rounded px-3 py-2"
          required
        />
      </div>

      <p v-if="error" class="text-red-600 text-sm">{{ error }}</p>
      <p v-if="success" class="text-green-700 text-sm">{{ success }}</p>

      <div class="flex gap-2 justify-end">
        <button class="px-4 py-2 border rounded" type="submit" :disabled="loading">
          {{ loading ? '...' : 'Update' }}
        </button>
        <button class="px-4 py-2 border rounded" type="button" @click="goBack">Kembali</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { UsersAPI } from '../services/api'
import { ref, reactive, onMounted } from 'vue'

const route = useRoute()
const router = useRouter()
const id = route.params.id

const form = reactive({ name: '', email: '', username: '' })
const loading = ref(false)
const error = ref('')
const success = ref('')

const preload = async () => {
  error.value = ''
  try {
    // prefer data dari navigation state agar snappy
    const stateUser = history.state?.user
    if (stateUser && stateUser.id == id) {
      Object.assign(form, {
        name: stateUser.name || '',
        email: stateUser.email || '',
        username: stateUser.username || '',
      })
      return
    }
    const { data } = await UsersAPI.get(id)
    Object.assign(form, {
      name: data.name || '',
      email: data.email || '',
      username: data.username || '',
    })
  } catch (e) {
    error.value = e.message || 'Gagal memuat data user'
  }
}

const onSubmit = async () => {
  error.value = ''
  success.value = ''
  loading.value = true
  try {
    await UsersAPI.update(id, form)
    success.value = 'Berhasil diperbarui'
    setTimeout(() => router.push({ name: 'dashboard' }), 500)
  } catch (e) {
    error.value = e.message || 'Update gagal'
  } finally {
    loading.value = false
  }
}

const goBack = () => router.push({ name: 'dashboard' })

onMounted(preload)
</script>
