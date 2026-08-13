<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="layout">
    <nav class="navbar">
      <h1>Tienda - Panel de Administración</h1>
      <div class="nav-links">
        <RouterLink to="/productos">Productos</RouterLink>
        <RouterLink to="/empleados">Empleados</RouterLink>
        <RouterLink to="/sedes">Sedes</RouterLink>
        <RouterLink to="/usuarios">Usuarios</RouterLink>
      </div>
    </nav>
    <main class="content">
      <RouterView />
    </main>
  </div>
</template>

<style>
* {
  box-sizing: border-box;
}
body {
  margin: 0;
  font-family: 'Segoe UI', Arial, sans-serif;
  background: #f4f5f7;
}
.layout {
  min-height: 100vh;
}
.navbar {
  background: #1f2937;
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}
.navbar h1 {
  font-size: 1.2rem;
  margin: 0;
}
.nav-links {
  display: flex;
  gap: 1.5rem;
}
.nav-links a {
  color: #d1d5db;
  text-decoration: none;
  font-weight: 500;
}
.nav-links a.router-link-active {
  color: white;
  border-bottom: 2px solid #3b82f6;
}
.content {
  padding: 2rem;
  max-width: 1100px;
  margin: 0 auto;
}
</style>