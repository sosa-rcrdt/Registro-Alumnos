import { createApp } from 'vue' // Importar la función createApp de Vue para crear la instancia de la aplicación
import App from './App.vue' // Importar el componente raíz de la aplicación
import router from './router' // Importar el enrutador para manejar las rutas de la aplicación
import './assets/main.css' // Importar los estilos principales de la aplicación

const app = createApp(App) // Crear la instancia de la aplicación Vue con el componente raíz
app.use(router) // Configurar el enrutador para que la aplicación lo utilice
app.mount('#app') // Montar la aplicación en el elemento con id 'app' en el HTML

