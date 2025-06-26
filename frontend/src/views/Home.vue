<template>
  <div class="max-w-5xl mx-auto p-6">
    <div class="flex justify-between items-center mb-6">
      <!-- Encabezado y botón de añadir alumno alineados horizontalmente -->
      <h1 class="text-3xl font-bold">Alumnos registrados</h1>
      <!-- Botón para ir a la pantalla de registro de un nuevo alumno -->
      <router-link to="/nuevo" class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700">
        + Añadir alumno
      </router-link>
    </div>

    <!-- Componente que muestra la tabla de alumnos, recibe la lista y emite evento para eliminar -->
    <AlumnoTable :alumnos="alumnos" @solicitar-eliminacion="mostrarModal" />

    <!-- Modal de confirmación para eliminar un alumno, solo visible si mostrarConfirmacion es true -->
    <ConfirmModal
      :visible="mostrarConfirmacion"
      mensaje="Esta acción no se puede deshacer."
      @confirmar="eliminarAlumno"
      @cancelar="cancelarEliminacion"
    />
  </div>
</template>

<script>
import AlumnoTable from '@/components/AlumnoTable.vue'
import ConfirmModal from '@/components/ConfirmModal.vue'
// Importo las funciones de la API centralizadas en services
import { getAlumnos, deleteAlumno } from '@/services/alumnos'

export default {
  components: {
    AlumnoTable,
    ConfirmModal
  },
  data() {
    return {
      alumnos: [], // Aquí se guarda la lista de alumnos obtenida del backend
      idAEliminar: null, // Aquí guardo el id del alumno que se quiera eliminar
      mostrarConfirmacion: false // Controla si el modal de confirmación está visible
    }
  },
  methods: {
    // Obtiene la lista de alumnos del backend y la guarda en el estado local
    async cargarAlumnos() {
      const res = await getAlumnos()
      this.alumnos = res.data
    },
    // Muestra el modal de confirmación y guarda el id del alumno a eliminar
    mostrarModal(id) {
      this.idAEliminar = id
      this.mostrarConfirmacion = true
    },
    // Oculta el modal y limpia el id a eliminar
    cancelarEliminacion() {
      this.idAEliminar = null
      this.mostrarConfirmacion = false
    },
    // Llama al backend para eliminar el alumno y recarga la lista
    async eliminarAlumno() {
      try {
        await deleteAlumno(this.idAEliminar)
        this.cancelarEliminacion()
        this.cargarAlumnos()
      } catch (err) {
        console.error('Error al eliminar alumno', err)
      }
    }
  },
  // Cuando se monta la vista, se carga la lista de alumnos automáticamente
  mounted() {
    this.cargarAlumnos()
  }
}
</script>