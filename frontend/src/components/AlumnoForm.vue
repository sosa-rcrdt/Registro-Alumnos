<template>
  <!-- Se usa v-model para enlazar los campos del formulario con el objeto form del data. -->
  <form @submit.prevent="enviarFormulario" class="space-y-4 bg-white p-6 rounded-lg shadow max-w-lg mx-auto">
    <!-- Título dinámico según si es edición o registro -->
    <h2 class="text-xl font-bold text-blue-700">
      {{ alumnoId ? 'Editar alumno' : 'Registrar nuevo alumno' }}
    </h2>

    <!-- Campo para el nombre del alumno -->
    <div>
      <label class="block font-medium">Nombre:</label>
      <input
        v-model="form.nombre"
        type="text"
        required
        class="w-full border rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
      />
    </div>

    <!-- Campo para el correo del alumno -->
    <div>
      <label class="block font-medium">Correo:</label>
      <input
        v-model="form.correo"
        type="email"
        required
        class="w-full border rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
      />
    </div>

    <!-- Campo para la carrera del alumno -->
    <div>
      <label class="block font-medium">Carrera:</label>
      <input
        v-model="form.carrera"
        type="text"
        required
        class="w-full border rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
      />
    </div>

    <!-- Campo para el semestre del alumno -->
    <div>
      <label class="block font-medium">Semestre:</label>
      <input
        v-model.number="form.semestre"
        type="number"
        min="1"
        required
        class="w-full border rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
      />
    </div>

    <!-- Botones de acción: Guardar/Actualizar y Regresar -->
    <div class="pt-4 flex gap-2">
      <!-- Botón para enviar el formulario. El texto cambia según si es edición o registro -->
      <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition">
        {{ alumnoId ? 'Actualizar' : 'Guardar' }}
      </button>
      <!-- Botón para regresar a la pantalla anterior -->
      <button
        type="button"
        @click="regresar"
        class="bg-gray-300 text-gray-800 px-4 py-2 rounded hover:bg-gray-400 transition"
      >
        Regresar
      </button>
    </div>

    <!-- Mensaje de error si ocurre algún problema al guardar -->
    <p v-if="error" class="text-red-600 mt-2">{{ error }}</p>
    <!-- Mensaje de éxito si el alumno fue registrado o actualizado -->
    <p v-if="exito" class="text-green-600 mt-2">
      {{ alumnoId ? 'Alumno actualizado ✅' : 'Alumno registrado exitosamente ✅' }}
    </p>
  </form>
</template>

<script>
// Se importan las funciones de la API desde services para mantener el código organizado
import { getAlumnoById, addAlumno, updateAlumno } from '@/services/alumnos'

export default {
  // Prop para saber si el formulario es de edición (alumnoId) o de registro (sin alumnoId)
  props: {
    alumnoId: Number
  },
  data() {
    return {
      // Objeto reactivo para los campos del formulario
      form: {
        nombre: '',
        correo: '',
        carrera: '',
        semestre: 1
      },
      error: null, // Mensaje de error si ocurre algún problema
      exito: false // Bandera para mostrar mensaje de éxito
    }
  },
  methods: {
    // Si estamos en modo edición, cargo los datos del alumno al montar el componente
    async cargarAlumno() {
      try {
        const res = await getAlumnoById(this.alumnoId)
        this.form = { ...res.data } // Se usa spread operator para copiar los datos del alumno
      } catch {
        this.error = 'No se pudo cargar el alumno.'
      }
    },
    // Envía el formulario para registrar o actualizar un alumno
    async enviarFormulario() {
      this.error = null
      this.exito = false

      try {
        if (this.alumnoId) {
          // Si hay alumnoId, actualizo el alumno existente
          await updateAlumno(this.alumnoId, this.form)
          this.$emit('alumno-editado') 
        } else {
          // Si no hay alumnoId, agrego un nuevo alumno
          await addAlumno(this.form)
          this.$emit('alumno-agregado')
          // Limpio el formulario después de registrar
          this.form = { nombre: '', correo: '', carrera: '', semestre: 1 }
        }
        this.exito = true
      } catch (err) {
        // Si el correo ya existe, muestro un mensaje específico
        if (!this.alumnoId && err.response?.status === 409) {
          this.error = 'El correo ya está registrado.'
        } else {
          this.error = 'Ocurrió un error al guardar.'
        }
      } //El try-catch maneja errores de la API
    },
    // Regresa a la pantalla anterior usando Vue Router o el historial del navegador
    regresar() {
      this.$router ? this.$router.back() : window.history.back()
    }
  },
  // Cuando el componente se monta, si es edición, cargo los datos del alumno
  mounted() {
    if (this.alumnoId) this.cargarAlumno()
  }
}
</script>