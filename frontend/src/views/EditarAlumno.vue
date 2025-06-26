<template>
  <!-- El formulario se autocompleta con los datos del alumno gracias a la prop :alumnoId. -->
  <div class="max-w-xl mx-auto space-y-4">
    <h2 class="text-2xl font-bold text-blue-700">Editar alumno</h2>
    <!-- Se pasa el id del alumno como prop y se escucha el evento para volver al inicio -->
    <AlumnoForm :alumnoId="id" @alumno-editado="volver" />
  </div>
</template>

<script>
import AlumnoForm from '@/components/AlumnoForm.vue'
// Se importan los hooks de Vue Router para acceder a la ruta y navegar
import { useRoute, useRouter } from 'vue-router'

export default {
  components: { AlumnoForm },
  setup() {
    // Se obtiene la ruta actual y el router para navegación programática
    const route = useRoute()
    const router = useRouter()

    // Se extrae el id del alumno desde los parámetros de la ruta
    const id = route.params.id

    // Función para volver a la pantalla principal después de editar
    const volver = () => router.push('/')

    // Se retornan las variables y métodos para usarlos en el template
    return { id, volver }
  }
}
</script>