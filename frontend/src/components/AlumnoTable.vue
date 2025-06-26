<template>
  <!-- Recibe la lista de alumnos como prop y emite un evento cuando se quiere eliminar uno. -->
  <div class="overflow-x-auto rounded-lg shadow bg-white p-4">
    <table class="min-w-full table-auto">
      <thead class="bg-blue-600 text-white">
        <tr>
          <th class="px-4 py-2 text-center">Nombre</th>
          <th class="px-4 py-2 text-center">Correo</th>
          <th class="px-4 py-2 text-center">Carrera</th>
          <th class="px-4 py-2 text-center">Semestre</th>
          <th class="px-4 py-2 text-center">Acciones</th>
        </tr>
      </thead>
      <tbody>
        <!-- Recorro la lista de alumnos y muestro cada uno en una fila -->
        <tr
          v-for="alumno in alumnos"
          :key="alumno.id"
          class="border-b hover:bg-gray-100 transition"
        >
          <!-- Muestro los datos principales del alumno -->
          <td class="px-4 py-2 text-center">{{ alumno.nombre }}</td>
          <td class="px-4 py-2 text-center">{{ alumno.correo }}</td>
          <td class="px-4 py-2 text-center">{{ alumno.carrera }}</td>
          <td class="px-4 py-2 text-center">{{ alumno.semestre }}</td>
          <td class="px-4 py-2 text-center space-x-2">
            <!-- Botón para editar, lleva a la ruta de edición del alumno -->
            <router-link :to="`/editar/${alumno.id}`" class="text-blue-600 hover:underline">
              Editar
            </router-link>
            <!-- Botón para eliminar, emite un evento al componente padre -->
            <button class="text-red-600 hover:underline" @click="$emit('solicitar-eliminacion', alumno.id)">
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
// Este componente solo recibe la lista de alumnos como prop.
export default {
  props: {
    alumnos: Array // Lista de alumnos a mostrar en la tabla
  }
}
</script>