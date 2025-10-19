<template>
  <form @submit.prevent="emitSearch" class="flex gap-2 items-center">
    <input
      v-model="q"
      type="text"
      placeholder="Cari nama atau username…"
      class="border rounded px-3 py-2 w-72"
    />
    <button class="border rounded px-3 py-2" type="submit">Cari</button>
    <button class="border rounded px-3 py-2" type="button" @click="reset">Reset</button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
const emit = defineEmits(['search'])
const q = ref('')
const emitSearch = () => emit('search', q.value.trim())
const reset = () => {
  q.value = ''
  emit('search', '')
}
</script>
