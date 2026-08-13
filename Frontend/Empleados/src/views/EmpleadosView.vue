<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/api'

const empleados = ref([])
const cargando = ref(false)
const error = ref('')

const formVisible = ref(false)
const editandoId = ref(null)
const form = ref({
  user_id: '',
  nombre_empleado: '',
  cargo: '',
  salario: '',
})

function resetForm() {
  form.value = { user_id: '', nombre_empleado: '', cargo: '', salario: '' }
  editandoId.value = null
}

async function cargarEmpleados() {
  cargando.value = true
  error.value = ''
  try {
    const respuesta = await api.get('/empleados/')
    empleados.value = respuesta.data
  } catch (err) {
    error.value = 'No se pudieron cargar los empleados. ¿Está corriendo el Gateway y el microservicio de Empleados?'
    console.error(err)
  } finally {
    cargando.value = false
  }
}

function abrirCrear() {
  resetForm()
  formVisible.value = true
}

function abrirEditar(empleado) {
  editandoId.value = empleado.id
  form.value = { ...empleado }
  formVisible.value = true
}

async function guardar() {
  try {
    if (editandoId.value) {
      await api.put(`/empleados/${editandoId.value}/`, form.value)
    } else {
      await api.post('/empleados/', form.value)
    }
    formVisible.value = false
    resetForm()
    await cargarEmpleados()
  } catch (err) {
    error.value = 'Error al guardar el empleado. Revisa los campos.'
    console.error(err.response?.data || err)
  }
}

async function eliminar(id) {
  if (!confirm('¿Seguro que quieres eliminar este empleado?')) return
  try {
    await api.delete(`/empleados/${id}/`)
    await cargarEmpleados()
  } catch (err) {
    error.value = 'Error al eliminar el empleado.'
    console.error(err)
  }
}

onMounted(cargarEmpleados)
</script>

<template>
  <div>
    <div class="header-row">
      <h2>Empleados</h2>
      <button class="btn-primary" @click="abrirCrear">+ Nuevo Empleado</button>
    </div>

    <p v-if="error" class="error">{{ error }}</p>
    <p v-if="cargando">Cargando...</p>

    <table v-if="!cargando && empleados.length" class="tabla">
      <thead>
        <tr>
          <th>ID</th>
          <th>User ID</th>
          <th>Nombre</th>
          <th>Cargo</th>
          <th>Salario</th>
          <th>Fecha Contratación</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="empleado in empleados" :key="empleado.id">
          <td>{{ empleado.id }}</td>
          <td>{{ empleado.user_id }}</td>
          <td>{{ empleado.nombre_empleado }}</td>
          <td>{{ empleado.cargo }}</td>
          <td>${{ empleado.salario }}</td>
          <td>{{ empleado.fecha_contratacion }}</td>
          <td class="acciones">
            <button class="btn-secundario" @click="abrirEditar(empleado)">Editar</button>
            <button class="btn-peligro" @click="eliminar(empleado.id)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>

    <p v-if="!cargando && !empleados.length && !error">No hay empleados todavía.</p>

    <div v-if="formVisible" class="modal-overlay" @click.self="formVisible = false">
      <div class="modal">
        <h3>{{ editandoId ? 'Editar Empleado' : 'Nuevo Empleado' }}</h3>
        <form @submit.prevent="guardar">
          <label>ID de Usuario</label>
          <input v-model="form.user_id" type="number" required />

          <label>Nombre</label>
          <input v-model="form.nombre_empleado" required />

          <label>Cargo</label>
          <input v-model="form.cargo" required />

          <label>Salario</label>
          <input v-model="form.salario" type="number" step="0.01" required />

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
.modal-acciones { display: flex; justify-content: flex-end; gap: 0.5rem; margin-top: 1rem; }
</style>