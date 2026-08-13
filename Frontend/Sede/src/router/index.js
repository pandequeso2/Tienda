import { createRouter, createWebHistory } from 'vue-router'
import SedesView from '../views/SedesView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'sedes',
      component: SedesView,
    },
  ],
})

export default router