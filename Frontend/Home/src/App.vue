<script setup>
const secciones = [
  {
    nombre: 'Productos',
    descripcion: 'Gestiona el catálogo de productos, precios y stock.',
    url: 'http://localhost:5173/',
    color: '#3b82f6',
  },
  {
    nombre: 'Empleados',
    descripcion: 'Administra el personal, cargos y salarios.',
    url: 'http://localhost:5174/',
    color: '#10b981',
  },
  {
    nombre: 'Sedes',
    descripcion: 'Consulta y edita las sucursales de la tienda.',
    url: 'http://localhost:5175/',
    color: '#f59e0b',
  },
  {
    nombre: 'Usuarios',
    descripcion: 'Gestiona clientes, empleados y administradores.',
    url: 'http://localhost:5176/',
    color: '#8b5cf6',
  },
]
</script>

<template>
  <div class="home">
    <header class="hero">
      <h1>Tienda</h1>
      <p>Panel central de administración — elige un módulo para comenzar</p>
    </header>

    <div class="grid">
      <!-- Agregamos la etiqueta de apertura <a> que faltaba -->
      <a 
        v-for="seccion in secciones"
        :key="seccion.nombre"
        :href="seccion.url"
        class="card"
        :style="{ borderTopColor: seccion.color }"
      >
        <h2>{{ seccion.nombre }}</h2>
        <p>{{ seccion.descripcion }}</p>
        <span class="ir">Ir al módulo →</span>
      </a>
    </div>
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
</style>

<style scoped>
.home {
  min-height: 100vh;
  padding: 3rem 2rem;
}
.hero {
  text-align: center;
  margin-bottom: 3rem;
}
.hero h1 {
  font-size: 2.5rem;
  color: #1f2937;
  margin-bottom: 0.5rem;
}
.hero p {
  color: #6b7280;
  font-size: 1.1rem;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.5rem;
  max-width: 1000px;
  margin: 0 auto;
}
.card {
  background: white;
  border-radius: 10px;
  padding: 1.5rem;
  text-decoration: none;
  color: inherit;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  border-top: 4px solid #ccc;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.12);
}
.card h2 {
  margin: 0;
  color: #1f2937;
}
.card p {
  margin: 0;
  color: #6b7280;
  font-size: 0.9rem;
  flex-grow: 1;
}
.ir {
  font-weight: 600;
  font-size: 0.9rem;
  color: #374151;
}
</style>