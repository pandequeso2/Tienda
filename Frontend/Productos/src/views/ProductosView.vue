<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/api'

const productos = ref([])
const cargando = ref(false)
const error = ref('')

const formVisible = ref(false)
const editandoId = ref(null)
const form = ref({
  nombre: '',
  descripcion: '',
  sku: '',
  precio: '',
  stock: '',
  sede_id: '',
  activo: true,
})

function resetForm() {
  form.value = {
    nombre: '',
    descripcion: '',
    sku: '',
    precio: '',
    stock: '',
    sede_id: '',
    activo: true,
  }
  editandoId.value = null
}

async function cargarProductos() {
  cargando.value = true
  error.value = ''
  try {
    const respuesta = await api.get('/productos/')
    productos.value = respuesta.data
  } catch (err) {
    error.value = 'No se pudieron cargar los productos. ¿Está corriendo el Gateway y el microservicio de Productos?'
    console.error(err)
  } finally {
    cargando.value = false
  }
}

function abrirCrear() {
  resetForm()
  formVisible.value = true
}

function abrirEditar(producto) {
  editandoId.value = producto.id
  form.value = { ...producto }
  formVisible.value = true
}

async function guardar() {
  try {
    if (editandoId.value) {
      await api.put(`/productos/${editandoId.value}/`, form.value)
    } else {
      await api.post('/productos/', form.value)
    }
    formVisible.value = false
    resetForm()
    await cargarProductos()
  } catch (err) {
    error.value = 'Error al guardar el producto. Revisa los campos.'
    console.error(err.response?.data || err)
  }
}

async function eliminar(id) {
  if (!confirm('¿Seguro que quieres eliminar este producto?')) return
  try {
    await api.delete(`/productos/${id}/`)
    await cargarProductos()
  } catch (err) {
    error.value = 'Error al eliminar el producto.'
    console.error(err)
  }
}

onMounted(cargarProductos)
</script>

<template>
  <div>
    <div class="header-row">
      <h2>Productos</h2>
      <button class="btn-primary" @click="abrirCrear">+ Nuevo Producto</button>
    </div>

    <p v-if="error" class="error">{{ error }}</p>
    <p v-if="cargando">Cargando...</p>

    <table v-if="!cargando && productos.length" class="tabla">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre</th>
          <th>SKU</th>
          <th>Precio</th>
          <th>Stock</th>
          <th>Sede ID</th>
          <th>Activo</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="producto in productos" :key="producto.id">
          <td>{{ producto.id }}</td>
          <td>{{ producto.nombre }}</td>
          <td>{{ producto.sku }}</td>
          <td>${{ producto.precio }}</td>
          <td>{{ producto.stock }}</td>
          <td>{{ producto.sede_id || '-' }}</td>
          <td>{{ producto.activo ? 'Sí' : 'No' }}</td>
          <td class="acciones">
            <button class="btn-secundario" @click="abrirEditar(producto)">Editar</button>
            <button class="btn-peligro" @click="eliminar(producto.id)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>

    <p v-if="!cargando && !productos.length && !error">No hay productos todavía.</p>

    <!-- Modal simple para crear/editar -->
    <div v-if="formVisible" class="modal-overlay" @click.self="formVisible = false">
      <div class="modal">
        <h3>{{ editandoId ? 'Editar Producto' : 'Nuevo Producto' }}</h3>
        <form @submit.prevent="guardar">
          <label>Nombre</label>
          <input v-model="form.nombre" required />

          <label>Descripción</label>
          <textarea v-model="form.descripcion"></textarea>

          <label>SKU</label>
          <input v-model="form.sku" required />

          <label>Precio</label>
          <input v-model="form.precio" type="number" step="0.01" required />

          <label>Stock</label>
          <input v-model="form.stock" type="number" required />

          <label>ID de Sede (opcional)</label>
          <input v-model="form.sede_id" type="number" />

          <label class="checkbox-label">
            <input v-model="form.activo" type="checkbox" />
            Activo
          </label>

          <div class="modal-acciones">
            <button type="button" class="btn-secundario" @click="formVisible = false">Cancelar</button>
            <button type="submit" class="btn-primary">Guardar</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<style scoped>
.header-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}
.tabla {
  width: 100%;
  border-collapse: collapse;
  background: white;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}
.tabla th, .tabla td {
  padding: 0.75rem 1rem;
  text-align: left;
  border-bottom: 1px solid #e5e7eb;
}
.tabla th {
  background: #f9fafb;
  font-weight: 600;
}
.acciones {
  display: flex;
  gap: 0.5rem;
}
.btn-primary {
  background: #3b82f6;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
}
.btn-secundario {
  background: #e5e7eb;
  color: #1f2937;
  border: none;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  cursor: pointer;
}
.btn-peligro {
  background: #ef4444;
  color: white;
  border: none;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  cursor: pointer;
}
.error {
  color: #b91c1c;
  background: #fee2e2;
  padding: 0.75rem 1rem;
  border-radius: 6px;
}
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
}
.modal {
  background: white;
  padding: 1.5rem 2rem;
  border-radius: 10px;
  width: 400px;
  max-height: 90vh;
  overflow-y: auto;
}
.modal form {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}
.modal label {
  font-size: 0.85rem;
  font-weight: 600;
  margin-top: 0.5rem;
}
.modal input, .modal textarea {
  padding: 0.5rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 0.9rem;
}
.checkbox-label {
  flex-direction: row !important;
  align-items: center;
  gap: 0.5rem;
}
.modal-acciones {
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
  margin-top: 1rem;
}
</style>