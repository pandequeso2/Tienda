<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/api'

const sedes = ref([])
const cargando = ref(false)
const error = ref('')

const formVisible = ref(false)
const editandoId = ref(null)
const form = ref({
  nombre: '',
  direccion: '',
  comuna: '',
  region: '',
  telefono: '',
  fecha_apertura: '',
  activa: true,
})

function resetForm() {
  form.value = {
    nombre: '',
    direccion: '',
    comuna: '',
    region: '',
    telefono: '',
    fecha_apertura: '',
    activa: true,
  }
  editandoId.value = null
}

async function cargarSedes() {
  cargando.value = true
  error.value = ''
  try {
    const respuesta = await api.get('/sedes/')
    sedes.value = respuesta.data
  } catch (err) {
    error.value = 'No se pudieron cargar las sedes. ¿Está corriendo el Gateway y el microservicio de Sedes?'
    console.error(err)
  } finally {
    cargando.value = false
  }
}

function abrirCrear() {
  resetForm()
  formVisible.value = true
}

function abrirEditar(sede) {
  editandoId.value = sede.id
  form.value = { ...sede }
  formVisible.value = true
}

async function guardar() {
  try {
    if (editandoId.value) {
      await api.put(`/sedes/${editandoId.value}/`, form.value)
    } else {
      await api.post('/sedes/', form.value)
    }
    formVisible.value = false
    resetForm()
    await cargarSedes()
  } catch (err) {
    error.value = 'Error al guardar la sede. Revisa los campos.'
    console.error(err.response?.data || err)
  }
}

async function eliminar(id) {
  if (!confirm('¿Seguro que quieres eliminar esta sede?')) return
  try {
    await api.delete(`/sedes/${id}/`)
    await cargarSedes()
  } catch (err) {
    error.value = 'Error al eliminar la sede.'
    console.error(err)
  }
}

onMounted(cargarSedes)
</script>

<template>
  <div>
    <div class="header-row">
      <h2>Sedes</h2>
      <button class="btn-primary" @click="abrirCrear">+ Nueva Sede</button>
    </div>

    <p v-if="error" class="error">{{ error }}</p>
    <p v-if="cargando">Cargando...</p>

    <table v-if="!cargando && sedes.length" class="tabla">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre</th>
          <th>Dirección</th>
          <th>Comuna</th>
          <th>Región</th>
          <th>Teléfono</th>
          <th>Activa</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="sede in sedes" :key="sede.id">
          <td>{{ sede.id }}</td>
          <td>{{ sede.nombre }}</td>
          <td>{{ sede.direccion }}</td>
          <td>{{ sede.comuna }}</td>
          <td>{{ sede.region }}</td>
          <td>{{ sede.telefono || '-' }}</td>
          <td>{{ sede.activa ? 'Sí' : 'No' }}</td>
          <td class="acciones">
            <button class="btn-secundario" @click="abrirEditar(sede)">Editar</button>
            <button class="btn-peligro" @click="eliminar(sede.id)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>

    <p v-if="!cargando && !sedes.length && !error">No hay sedes todavía.</p>

    <div v-if="formVisible" class="modal-overlay" @click.self="formVisible = false">
      <div class="modal">
        <h3>{{ editandoId ? 'Editar Sede' : 'Nueva Sede' }}</h3>
        <form @submit.prevent="guardar">
          <label>Nombre</label>
          <input v-model="form.nombre" required />

          <label>Dirección</label>
          <input v-model="form.direccion" required />

          <label>Comuna</label>
          <input v-model="form.comuna" required />

          <label>Región</label>
          <input v-model="form.region" required />

          <label>Teléfono</label>
          <input v-model="form.telefono" />

          <label>Fecha de Apertura</label>
          <input v-model="form.fecha_apertura" type="date" />

          <label class="checkbox-label">
            <input v-model="form.activa" type="checkbox" />
            Activa
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
.header-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; }
.tabla { width: 100%; border-collapse: collapse; background: white; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.tabla th, .tabla td { padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid #e5e7eb; }
.tabla th { background: #f9fafb; font-weight: 600; }
.acciones { display: flex; gap: 0.5rem; }
.btn-primary { background: #3b82f6; color: white; border: none; padding: 0.5rem 1rem; border-radius: 6px; cursor: pointer; font-weight: 500; }
.btn-secundario { background: #e5e7eb; color: #1f2937; border: none; padding: 0.4rem 0.8rem; border-radius: 6px; cursor: pointer; }
.btn-peligro { background: #ef4444; color: white; border: none; padding: 0.4rem 0.8rem; border-radius: 6px; cursor: pointer; }
.error { color: #b91c1c; background: #fee2e2; padding: 0.75rem 1rem; border-radius: 6px; }
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.4); display: flex; align-items: center; justify-content: center; }
.modal { background: white; padding: 1.5rem 2rem; border-radius: 10px; width: 400px; max-height: 90vh; overflow-y: auto; }
.modal form { display: flex; flex-direction: column; gap: 0.4rem; }
.modal label { font-size: 0.85rem; font-weight: 600; margin-top: 0.5rem; }
.modal input { padding: 0.5rem; border: 1px solid #d1d5db; border-radius: 6px; font-size: 0.9rem; }
.checkbox-label { flex-direction: row !important; align-items: center; gap: 0.5rem; }
.modal-acciones { display: flex; justify-content: flex-end; gap: 0.5rem; margin-top: 1rem; }
</style>