import axios from 'axios'

// URL base de la API para los alumnos
const API_URL = 'http://localhost:8000/alumnos'

// Obtiene la lista de todos los alumnos
export function getAlumnos() {
  return axios.get(API_URL)
}

// Elimina un alumno por su id
export function deleteAlumno(id) {
  return axios.delete(`${API_URL}/${id}`)
}

// Agrega un nuevo alumno (data es un objeto con los datos del alumno)
export function addAlumno(data) {
  return axios.post(API_URL, data)
}

// Actualiza los datos de un alumno existente
export function updateAlumno(id, data) {
  return axios.put(`${API_URL}/${id}`, data)
}

// Obtiene los datos de un solo alumno por su id
export function getAlumnoById(id) {
  return axios.get(`${API_URL}/${id}`)
}