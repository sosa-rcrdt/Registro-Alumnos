<template>
  <!-- Se usa el componente AlumnoForm, pero sin pasarle un id, así que el formulario está vacío. -->
  <div class="max-w-xl mx-auto space-y-4">
    <h2 class="text-2xl font-bold text-blue-700">Registrar nuevo alumno</h2>
    <!-- Se usa el formulario y se escucha el evento para volver al inicio cuando se agrega un alumno -->
    <AlumnoForm @alumno-agregado="volver" />
  </div>
</template>

<script>
import AlumnoForm from '@/components/AlumnoForm.vue'

export default {
  components: { AlumnoForm },
  methods: {
    // Cuando se agrega un alumno, se navega de regreso a la pantalla principal
    volver() {
      this.$router.push('/')
    }
  }
}
</script>