import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import NuevoAlumno from '@/views/NuevoAlumno.vue'
import EditarAlumno from '@/views/EditarAlumno.vue'

// Se definen las rutas de la aplicación:
const routes = [
  { path: '/', component: Home }, // Muestra la vista principal con la lista de alumnos
  { path: '/nuevo', component: NuevoAlumno }, // Muestra el formulario para registrar un nuevo alumno
  { path: '/editar/:id', component: EditarAlumno } // Muestra el formulario para editar un alumno existente (el id es dinámico)
]

// Se crea el router usando historial HTML5 (URLs limpias) y las rutas definidas
const router = createRouter({
  history: createWebHistory(),
  routes
})

// Se exportan el router para usarlo en la app principal
export default router