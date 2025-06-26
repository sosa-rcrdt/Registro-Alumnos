<template>
  <!-- Se muestra encima de todo el contenido cuando visible=true. -->
  <transition name="fade">
    <div
      v-if="visible"
      class="fixed inset-0 z-50 flex items-center justify-center backdrop-blur-sm bg-black/50"
      @keydown.esc="$emit('cancelar')"
      tabindex="0"
    >
      <div class="bg-white rounded-lg shadow-xl w-full max-w-md p-6 animate-scale-in">
        <!-- Título del modal -->
        <h2 class="text-xl font-semibold mb-4 text-red-600">¿Estás seguro?</h2>
        <!-- Mensaje personalizado que se recibe por prop -->
        <p class="mb-6 text-gray-700">{{ mensaje }}</p>
        <div class="flex justify-end space-x-3">
          <!-- Botón para cancelar la acción -->
          <button @click="cancelar" class="px-4 py-2 bg-gray-300 rounded hover:bg-gray-400">Cancelar</button>
          <!-- Botón para confirmar la acción -->
          <button @click="confirmar" class="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700">Sí, eliminar</button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
// Recibe props para controlar su visibilidad y el mensaje a mostrar.
export default {
  props: {
    visible: Boolean, // Controla si el modal se muestra o no
    mensaje: {
      type: String,
      default: '¿Deseas eliminar este elemento?'
    }
  },
  emits: ['confirmar', 'cancelar'],
  methods: {
    confirmar() {
      this.$emit('confirmar')
    },
    cancelar() {
      this.$emit('cancelar')
    },
    // Permite cerrar el modal con la tecla Escape
    teclaEscape(e) {
      if (e.key === 'Escape') this.cancelar()
    }
  },
  mounted() {
    // Escucho la tecla Escape cuando el modal está montado
    document.addEventListener('keydown', this.teclaEscape)
  },
  unmounted() {
    // Dejo de escuchar la tecla Escape cuando el modal se desmonta
    document.removeEventListener('keydown', this.teclaEscape)
  }
}
</script>

<style scoped>
/* Animación de aparición/desaparición del modal */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.15s ease-out;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Animación de escala para el modal */
@keyframes scale-in-pop {
  0% {
    transform: scale(0.85);
    opacity: 0;
  }
  80% {
    transform: scale(1.05);
    opacity: 1;
  }
  100% {
    transform: scale(1);
  }
}

.animate-scale-in {
  animation: scale-in-pop 0.15s ease-out;
}
</style>