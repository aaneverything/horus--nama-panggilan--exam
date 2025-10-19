<template>
  <section>
    <h2 class="text-xl font-semibold mb-4">DASHBOARD PENGGUNA</h2>

    <SearchBar @search="onSearch" class="mb-4" />
    <UserTable :users="filtered" @update="goUpdate" @delete="confirmDelete" />

    <div v-if="error" class="mt-3 text-sm text-red-600">{{ error }}</div>
  </section>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import SearchBar from '@/components/SearchBar.vue'   
import UserTable from '@/components/UserTable.vue'
import { UsersAPI } from '@/services/api'

const router = useRouter()
const users = ref([])
const q = ref('')
const error = ref('')

const fetchUsers = async () => {
  error.value = ''
  try {
    const { data } = await UsersAPI.list(q.value ? { q: q.value } : undefined)
    users.value = Array.isArray(data) ? data : data?.items || []
  } catch (e) {
    error.value = e.message
  }
}

const filtered = computed(() => {
  if (!q.value) return users.value
  const s = q.value.toLowerCase()
  return users.value.filter(u =>
    (u.name || '').toLowerCase().includes(s) ||
    (u.username || '').toLowerCase().includes(s)
  )
})

const onSearch = async (term) => { q.value = term; await fetchUsers() }
const goUpdate = (u) => router.push({ name: 'updateUser', params: { id: u.id }, state: { user: u } })
const confirmDelete = async (u) => {
  if (!window.confirm(`Apakah Anda yakin menghapus user "${u.username}"?`)) return
  try { await UsersAPI.delete(u.id); await fetchUsers() } catch (e) { error.value = e.message }
}

onMounted(fetchUsers)
</script>
