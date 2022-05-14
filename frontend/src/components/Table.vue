<script lang="ts" setup>
import { defineProps, PropType } from "vue";

const props = defineProps({
  incomingHeaders: {
    type: Array as PropType<unknown[]> | null,
    required: true,
  },
  IncomingData: {
    type: Object as PropType<unknown[]> | null,
    required: true,
  },
});
</script>

<template>
  <table class="table table-striped">
    <thead>
      <tr>
        <th
          v-for="(incomingHeader, index) in props.incomingHeaders"
          v-bind:key="index"
        >
          {{ incomingHeader }}
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(value, index) in props.IncomingData" v-bind:key="index">
        <td v-for="(item, index) in value" v-bind:key="index">
          {{ item }}
        </td>
      </tr>
    </tbody>
  </table>
</template>
