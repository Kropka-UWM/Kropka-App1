<script setup lang="ts">
import { computed } from "vue";
import Toast from "./common/Toast.vue";

import { key } from "@/store";
import { useStore } from "vuex";

const store = useStore(key);

const toasts = computed(() => store.state.toasts);
</script>

<template>
  <div class="toast-container position-absolute top-0 end-0 m-4">
    <Toast
      v-for="(toast, index) in toasts"
      :text-class="`text-white`"
      :toast-class="toast.toastClass"
      :key="index"
    >
      {{ toast.text }}
    </Toast>
  </div>
</template>
