<script setup>
import { computed } from 'vue'
import { useAuthStore } from '../src/store/auth'
const auth = useAuthStore()
const isLogged = computed(() => auth.isAuthenticated)
const logout = () => auth.logout()
</script>

<template>
<div class="min-h-screen bg-gray-50 text-gray-900">
    <header class="p-4 border-b bg-white flex items-center justify-between">
      <h1 class="font-semibold">User Admin</h1>
      <nav class="space-x-3">
        <RouterLink to="/">Dashboard</RouterLink>
        <RouterLink to="/login">Login</RouterLink>
        <RouterLink to="/register">Registrasi</RouterLink>
        <button v-if="isLogged" @click="logout" class="px-2 py-1 border rounded">Logout</button>
      </nav>
    </header>
    <main class="p-6">
      <RouterView />
    </main>
  </div>
</template>

<style>
:root { font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial; }
a { text-decoration: none; }
</style>
