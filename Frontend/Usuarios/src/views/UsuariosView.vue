<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/api'

const usuarios = ref([])
const cargando = ref(false)
const error = ref('')

const formVisible = ref(false)
const editandoId = ref(null)
const form = ref({
  username: '',
  password: '',
  email: '',
  rut: '',
  nombre_completo: '',
  correo: '',
  fecha_nacimiento: '',
  genero: '',
  tipo_usuario: 'CLIENTE',
})

function resetForm() {
  form.value = {
    username: '',
    password: '',
    email: '',
    rut: '',
    nombre_completo: '',
    correo: '',
    fecha_nacimiento: '',
    genero: '',
    tipo_usuario: 'CLIENTE',
  }
  editandoId.value = null
}

async function cargarUsuarios() {
  cargando.value = true
  error.value = ''
  try {
    const respuesta = await api.get('/usuarios/')
    usuarios.value = respuesta.data
  } catch (err) {
    error.value = 'No se pudieron cargar los usuarios. ¿Está corriendo el Gateway y el microservicio de Usuarios?'
    console.error(err)
  } finally {
    cargando.value = false
  }
}

function abrirCrear() {
  resetForm()
  formVisible.value = true
}

function abrirEditar(usuario) {
  editandoId.value = usuario.id
  form.value = { ...usuario, password: '' }
  formVisible.value = true
}

async function guardar() {
  try {
    const datosAEnviar = { ...form.value }
    // Si estamos editando y no se escribió una contraseña nueva, no la mandamos
    if (editandoId.value && !datosAEnviar.password) {
      delete datosAEnviar.password
    }

    if (editandoId.value) {
      await api.patch(`/usuarios/${editandoId.value}/`, datosAEnviar)
    } else {
      await api.post('/usuarios/', datosAEnviar)
    }
    formVisible.value = false
    resetForm()
    await cargarUsuarios()
  } catch (err) {
    error.value = 'Error al guardar el usuario. Revisa los campos.'
    console.error(err.response?.data || err)
  }
}

async function eliminar(id) {
  if (!confirm('¿Seguro que quieres eliminar este usuario?')) return
  try {
    await api.delete(`/usuarios/${id}/`)
    await cargarUsuarios()
  } catch (err) {
    error.value = 'Error al eliminar el usuario.'
    console.error(err)
  }
}

onMounted(cargarUsuarios)
</script>

<template>
  <div>
    <div class="header-row">
      <h2>Usuarios</h2>
      <button class="btn-primary" @click="abrirCrear">+ Nuevo Usuario</button>
    </div>

    <p v-if="error" class="error">{{ error }}</p>
    <p v-if="cargando">Cargando...</p>

    <table v-if="!cargando && usuarios.length" class="tabla">
      <thead>
        <tr>
          <th>ID</th>
          <th>Username</th>
          <th>Nombre Completo</th>
          <th>RUT</th>
          <th>Correo</th>
          <th>Tipo</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="usuario in usuarios" :key="usuario.id">
          <td>{{ usuario.id }}</td>
          <td>{{ usuario.username }}</td>
          <td>{{ usuario.nombre_completo }}</td>
          <td>{{ usuario.rut }}</td>
          <td>{{ usuario.correo }}</td>
          <td>{{ usuario.tipo_usuario }}</td>
          <td class="acciones">
            <button class="btn-secundario" @click="abrirEditar(usuario)">Editar</button>
            <button class="btn-peligro" @click="eliminar(usuario.id)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>

    <p v-if="!cargando && !usuarios.length && !error">No hay usuarios todavía.</p>

    <div v-if="formVisible" class="modal-overlay" @click.self="formVisible = false">
      <div class="modal">
        <h3>{{ editandoId ? 'Editar Usuario' : 'Nuevo Usuario' }}</h3>
        <form @submit.prevent="guardar">
          <label>Username</label>
          <input v-model="form.username" required />

          <label>{{ editandoId ? 'Nueva contraseña (dejar en blanco para no cambiar)' : 'Contraseña' }}</label>
          <input v-model="form.password" type="password" :required="!editandoId" />

          <label>Email (login)</label>
          <input v-model="form.email" type="email" />

          <label>RUT</label>
          <input v-model="form.rut" required />

          <label>Nombre Completo</label>
          <input v-model="form.nombre_completo" required />

          <label>Correo</label>
          <input v-model="form.correo" type="email" required />

          <label>Fecha de Nacimiento</label>
          <input v-model="form.fecha_nacimiento" type="date" />

          <label>Género</label>
          <select v-model="form.genero">
            <option value="">Sin especificar</option>
            <option value="M">Masculino</option>
            <option value="F">Femenino</option>
            <option value="O">Otro</option>
          </select>

          <label>Tipo de Usuario</label>
          <select v-model="form.tipo_usuario">
            <option value="CLIENTE">Cliente</option>
            <option value="EMPLEADO">Empleado</option>
            <option value="ADMIN">Administrador</option>
          </select>

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
.modal input, .modal select { padding: 0.5rem; border: 1px solid #d1d5db; border-radius: 6px; font-size: 0.9rem; }
.modal-acciones { display: flex; justify-content: flex-end; gap: 0.5rem; margin-top: 1rem; }
</style>