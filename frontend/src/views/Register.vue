<template>
  <div class="max-w-md mx-auto bg-white border rounded p-6 shadow-sm">
    <h2 class="text-xl font-semibold text-center mb-4">REGISTRASI</h2>
    <form @submit.prevent="onSubmit" class="space-y-3">
      <div>
        <label class="block mb-1">Nama Lengkap</label>
        <input
          v-model.trim="form.nama"
          type="text"
          class="w-full border rounded px-3 py-2"
          required
        />
        <p v-if="errs.nama" class="text-red-600 text-sm mt-1">{{ errs.nama }}</p>
      </div>

      <div>
        <label class="block mb-1">Email</label>
        <input
          v-model.trim="form.email"
          type="email"
          class="w-full border rounded px-3 py-2"
          required
        />
        <p v-if="errs.email" class="text-red-600 text-sm mt-1">{{ errs.email }}</p>
      </div>

      <div>
        <label class="block mb-1">Username</label>
        <input
          v-model.trim="form.username"
          type="text"
          class="w-full border rounded px-3 py-2"
          required
        />
        <p v-if="errs.username" class="text-red-600 text-sm mt-1">{{ errs.username }}</p>
      </div>

      <div>
        <label class="block mb-1">Password</label>
        <!-- jangan .trim password -->
        <input
          v-model="form.password"
          type="password"
          class="w-full border rounded px-3 py-2"
          required
        />
        <p v-if="errs.password" class="text-red-600 text-sm mt-1">{{ errs.password }}</p>
      </div>

      <p v-if="error" class="text-red-600 text-sm">{{ error }}</p>
      <p v-if="success" class="text-green-700 text-sm">{{ success }}</p>

      <div class="flex gap-2 justify-end">
        <button class="px-4 py-2 border rounded" type="submit" :disabled="loading">
          {{ loading ? '...' : 'Registrasi' }}
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { AuthAPI } from '../services/api' 

const router = useRouter()
const form = reactive({ nama: '', email: '', username: '', password: '' })
const errs = reactive({ nama: '', email: '', username: '', password: '' })
const error = ref('')
const success = ref('')
const loading = ref(false)

function validate() {
  errs.nama = errs.email = errs.username = errs.password = ''
  let ok = true

  if (!form.nama) {
    errs.nama = 'Nama wajib diisi'
    ok = false
  }

  if (!form.email) {
    errs.email = 'Email wajib diisi'
    ok = false
  } else {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!re.test(form.email)) {
      errs.email = 'Format email tidak valid'
      ok = false
    }
  }

  if (!form.username) {
    errs.username = 'Username wajib diisi'
    ok = false
  }

  if (!form.password) {
    errs.password = 'Password wajib diisi'
    ok = false
  } else {
    const hasMin = form.password.length >= 8
    const hasLetter = /[A-Za-z]/.test(form.password)
    const hasDigit = /\d/.test(form.password)
    if (!(hasMin && hasLetter && hasDigit)) {
      errs.password = 'Minimal 8 karakter, harus ada huruf & angka'
      ok = false
    }
  }

  return ok
}

const onSubmit = async () => {
  error.value = ''
  success.value = ''
  if (!validate()) {
    error.value = 'Field wajib kurang'
    return
  }

  loading.value = true
  try {
    await AuthAPI.register({
      username: form.username,
      password: form.password,
      email: form.email,
      nama: form.nama,
    })
    success.value = 'Registrasi berhasil. Silakan login.'
    setTimeout(() => router.push({ name: 'login' }), 600)
  } catch (e) {
    const msg = e?.response?.data?.message || e?.message || 'Registrasi gagal'
    error.value = msg
  } finally {
    loading.value = false
  }
}
</script>
