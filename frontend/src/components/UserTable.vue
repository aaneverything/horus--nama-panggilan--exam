<template>
  <div class="overflow-x-auto">
    <table class="min-w-full border">
      <thead class="bg-gray-100">
        <tr>
          <th class="px-3 py-2 border">ID</th>
          <th class="px-3 py-2 border">Username</th>
          <th class="px-3 py-2 border">Nama Lengkap</th>
          <th class="px-3 py-2 border">Email</th>
          <th class="px-3 py-2 border">Aksi</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="u in users" :key="u.id" class="odd:bg-white even:bg-gray-50">
          <td class="px-3 py-2 border">{{ u.id }}</td>
          <td class="px-3 py-2 border">{{ u.username }}</td>
          <td class="px-3 py-2 border">{{ u.nama }}</td>
          <td class="px-3 py-2 border">{{ u.email }}</td>
          <td class="px-3 py-2 border">
            <button class="px-2 py-1 border rounded mr-2" @click="$emit('update', u)">U</button>
            <button class="px-2 py-1 border rounded" @click="$emit('delete', u)">H</button>
          </td>
        </tr>
        <tr v-if="!users || users.length === 0">
          <td colspan="5" class="text-center py-4 text-gray-500">Tidak ada data.</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
defineProps({ users: { type: Array, default: () => [] } })
defineEmits(['update', 'delete'])
</script>
