<script setup lang="ts">
import SideBar from "@/components/userpanel/Sidebar.vue";
import Table from "@/components/Table.vue";
import { Student, ResponseData } from "../../types";
import { computed } from "vue";

const incomingHeaders: Array<string> = [
  "id",
  "name",
  "surname",
  "email",
  "company",
];

const IncomingData: Student[] = [
  {
    id: "1",
    name: "Name",
    surname: "surname",
    email: "email@o2.com",
    company: "company",
  },
  {
    id: "1",
    name: "Name",
    surname: "surname",
    email: "email@o2.com",
    company: "company",
  },
  {
    id: "1",
    name: "Name",
    surname: "surname",
    email: "email@o2.com",
    company: "company",
  },
];

const rawData = computed(() => {
  return JSON.parse(JSON.stringify(IncomingData));
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
        <h1 class="text-start">User</h1>
        <h2 class="text-start">Twoja grupa</h2>
        <Table
          :incomingHeaders="incomingHeaders"
          :IncomingData="IncomingData"
        ></Table>
      </div>
    </div>
    headery dla tabeli:
    <p v-if="rawData">{{ rawData2 }}</p>
    tabela:
    <p v-if="rawData">{{ rawData }}</p>
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
