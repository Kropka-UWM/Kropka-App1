<script setup lang="ts">
import { onMounted, ref, Ref, defineProps } from "vue";
import Toast from "bootstrap/js/dist/toast.js";

const props = defineProps<{
  toastClass: string;
  textClass: string;
}>();

const toastRef: Ref<Element | string> = ref("");

let myToast = toastRef.value;

let bsToast = Toast.getInstance(myToast);

const showToast = () => {
  bsToast = new Toast(toastRef.value, { autohide: true, delay: 5000 });
  bsToast.show();
};

const hideToast = () => {
  bsToast = new Toast(toastRef.value, { autohide: true });
  bsToast.hide();
};

onMounted(() => {
  showToast();
});
</script>

<template>
  <div
    :class="props.toastClass"
    class="toast"
    role="alert"
    ref="toastRef"
    aria-live="assertive"
    aria-atomic="true"
  >
    <div class="toast-header">
      <button
        type="button"
        :class="props.textClass"
        class="btn-close ms-auto me-2"
        @click="hideToast"
        aria-label="Close"
        data-bs-dismiss="toast"
      ></button>
    </div>
    <div :class="props.textClass" class="toast-body">
      <slot></slot>
    </div>
  </div>
</template>
