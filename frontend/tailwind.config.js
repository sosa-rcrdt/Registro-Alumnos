/** 
 * @type {import('tailwindcss').Config} 
 * Archivo de configuración de Tailwind CSS para el proyecto frontend.
 */
export default {
  // Indicar a Tailwind en qué archivos buscar clases CSS para generar los estilos necesarios
  content: [
    "./index.html", // Incluir el archivo HTML principal
    "./src/**/*.{vue,js,ts,jsx,tsx}", // Incluir todos los archivos fuente dentro de src con estas extensiones
  ],
  theme: {
    // Extender o personalizar el tema de Tailwind (colores, fuentes, etc.)
    extend: {},
  },
  // Agregar plugins de Tailwind a utilizar (vacío por defecto, se pueden agregar plugins oficiales o de la comunidad)
  plugins: [],
}

