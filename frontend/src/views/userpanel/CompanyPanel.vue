<script setup lang="ts">
import Table from "@/components/Table.vue";
import { Student, ResponseData } from "../../types";
import { computed } from "vue";

const incomingHeaders: Array<string> = [
  "id",
  "first_name",
  "last_name",
  "email",
  "company",
];

const multipleTables = {
  group1: [
    {
      id: "1",
      first_name: "Name",
      last_name: "surname",
      email: "email@o2.com",
      company: "company",
    },
    {
      id: "1",
      first_name: "Name",
      last_name: "surname",
      email: "email@o2.com",
      company: "company",
    },
    {
      id: "1",
      first_name: "Name",
      last_name: "surname",
      email: "email@o2.com",
      company: "company",
    },
  ],
  group2: [
    {
      id: "1",
      first_name: "Name",
      last_name: "surname",
      email: "email@o2.com",
      company: "company",
    },
    {
      id: "1",
      first_name: "Name",
      last_name: "surname",
      email: "email@o2.com",
      company: "company",
    },
    {
      id: "1",
      first_name: "Name",
      last_name: "surname",
      email: "email@o2.com",
      company: "company",
    },
  ],
  group3: [
    {
      id: "1",
      first_name: "Name",
      last_name: "surname",
      email: "email@o2.com",
      company: "company",
    },
    {
      id: "1",
      first_name: "Name",
      last_name: "surname",
      email: "email@o2.com",
      company: "company",
    },
    {
      id: "1",
      first_name: "Name",
      last_name: "surname",
      email: "email@o2.com",
      company: "company",
    },
  ],
};

const rawData = computed(() => {
  return JSON.parse(JSON.stringify(multipleTables));
});

const rawData2 = computed(() => {
  return JSON.parse(JSON.stringify(incomingHeaders));
});

// // Ref way
// let users = ref<Array<IUser>>([]);

// onMounted(async () => {
//   users.value = await UsersApi.getAllUsers();
// });
</script>

<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <h1 class="text-start">Company</h1>

        <div
          v-for="(multipleTable, value) in multipleTables"
          v-bind:key="value"
        >
          <h2 class="text-start">{{ value }}</h2>
          <Table
            :incomingHeaders="incomingHeaders"
            :IncomingData="multipleTable"
          ></Table>
        </div>
      </div>
      headery dla tabeli:
      <p v-if="rawData">{{ rawData2 }}</p>
      tabele:
      <p v-if="rawData">{{ rawData }}</p>
    </div>
  </div>
</template>

<style lang="scss">
.content-container {
  width: calc(100% - 280px);
}

.panel-template {
  display: flex;
  flex-wrap: nowrap;
  height: 100vh;
  max-height: 100vh;
  overflow-y: hidden;
}
</style>
