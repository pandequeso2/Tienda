<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="layout">
    <nav class="navbar">
      <h1>Tienda - Empleados</h1>
    </nav>
    <main class="content">
      <RouterView />
    </main>
  </div>
</template>

<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Segoe UI', Arial, sans-serif; background: #f4f5f7; }
.layout { min-height: 100vh; }
.navbar { background: #1f2937; color: white; padding: 1rem 2rem; }
.navbar h1 { font-size: 1.2rem; margin: 0; }
.content { padding: 2rem; max-width: 1100px; margin: 0 auto; }
</style>