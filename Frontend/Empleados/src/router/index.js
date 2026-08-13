import { createRouter, createWebHistory } from 'vue-router'
import EmpleadosView from '../views/EmpleadosView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'empleados',
      component: EmpleadosView,
    },
  ],
})

export default router