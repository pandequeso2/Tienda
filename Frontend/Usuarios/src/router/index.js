import { createRouter, createWebHistory } from 'vue-router'
import UsuariosView from '../views/UsuariosView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'usuarios',
      component: UsuariosView,
    },
  ],
})

export default router