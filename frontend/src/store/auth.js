import { defineStore } from 'pinia'
const TOKEN_KEY = import.meta.env.VITE_TOKEN_KEY || 'app_token'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem(TOKEN_KEY) || null,
    user: null
  }),
  getters: {
    isAuthenticated: (s) => !!s.token
  },
  actions: {
    setToken(token) {
      this.token = token
      localStorage.setItem(TOKEN_KEY, token)
    },
    setUser(user) {
      this.user = user
    },
    logout() {
      this.token = null
      this.user = null
      localStorage.removeItem(TOKEN_KEY)
    }
  }
})


