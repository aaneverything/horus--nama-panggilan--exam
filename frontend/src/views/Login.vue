<template>
  <div class="max-w-md mx-auto bg-white border rounded p-6 shadow-sm">
    <h2 class="text-xl font-semibold text-center mb-4">LOGIN</h2>
    <form @submit.prevent="onSubmit" class="space-y-3">
      <div>
        <label class="block mb-1">Username</label>
        <input v-model.trim="form.username" type="text" class="w-full border rounded px-3 py-2" required />
      </div>
      <div>
        <label class="block mb-1">Password</label>
        <input v-model.trim="form.password" type="password" class="w-full border rounded px-3 py-2" required />
      </div>
      <p v-if="error" class="text-red-600 text-sm">{{ error }}</p>
      <div class="flex gap-2 justify-end">
        <button class="px-4 py-2 border rounded" type="submit" :disabled="loading">
          {{ loading ? '...' : 'Login' }}
        </button>
        <RouterLink to="/register" class="px-4 py-2 border rounded inline-flex items-center">Registrasi</RouterLink>
      </div>
    </form>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { AuthAPI } from '../services/api'
import { useAuthStore } from '../store/auth'

const router = useRouter()
const route = useRoute()
const auth = useAuthStore()

const form = reactive({ username: '', password: '' })
const error = ref('')
const loading = ref(false)

const onSubmit = async () => {
  error.value = ''
  loading.value = true
  try {
    const { data } = await AuthAPI.login({ username: form.username, password: form.password })
    let token =
      data?.token ??
      data?.access_token ??
      null

    if (!token && typeof data?.message === 'string') {
      const m = data.message.match(/token:\s*([A-Za-z0-9\-\._]+)/i)
      token = m?.[1] || null
    }

    if (!token) throw new Error(data?.message || 'Login gagal')

    auth.setToken(token)
    if (data.user) auth.setUser(data.user)
    router.replace(route.query.redirect || '/')
    router.push(redirect)
  } catch (e) {
    error.value = e.message || 'Username atau password salah'
  } finally {
    loading.value = false
  }
}
</script>
