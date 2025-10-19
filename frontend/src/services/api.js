import axios from 'axios'
import { useAuthStore } from '@/store/auth'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
})

api.interceptors.request.use((config) => {
  const authStore = useAuthStore()
  if (authStore.token) {
    config.headers.Authorization = `Bearer ${authStore.token}`
  }
  return config
})

// src/services/api.js
api.interceptors.response.use(
  (res) => {
    // normalize hanya untuk /auth/login
    if (res.config.url?.includes('/api/auth/login')) {
      const d = res.data || {}
      if (!d.token && typeof d.message === 'string') {
        const m = d.message.match(/token:\s*([A-Za-z0-9\-\._]+)/i)
        if (m?.[1]) res.data = { ...d, token: m[1] }
      }
    }
    return res
  },
  (err) => {
    const data = err?.response?.data
    const msg = data?.message || data?.detail || err.message || 'Request error'
    return Promise.reject(new Error(msg))
  }
)


export const AuthAPI = {
  login: (payload) => api.post('users/login', payload),
  register: (payload) => api.post('users/register', payload),
}

export const UsersAPI = {
  list: (params) => api.get('/users', { params }),
  get: (id) => api.get(`/users/${id}`),
  update: (id, payload) => api.put(`/users/${id}`, payload),
  delete: (id) => api.delete(`/users/${id}`),
}

export default api
