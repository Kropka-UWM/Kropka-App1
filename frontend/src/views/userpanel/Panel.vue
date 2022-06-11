<script setup lang="ts">
import SideBar from "@/components/userpanel/Sidebar.vue";
import Table from "@/components/Table.vue";
import { onMounted, ref } from "vue";
import { UsersApi } from "@/services/UserDataService";
import { Student, ResponseData } from "@/types";
import { IUser } from "@/services/UserDataService";

const incomingHeaders: Array<string> = [
  "id",
  "first_name",
  "last_name",
  "email",
  "active",
  "company",
];

const IncomingData: Student[] = [
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
];

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
        <h2 class="text-start">Group1</h2>
        <Table
          :incomingHeaders="incomingHeaders"
          :IncomingData="IncomingData"
        ></Table>
        <h2 class="text-start">Group2</h2>
        <Table
          :incomingHeaders="incomingHeaders"
          :IncomingData="IncomingData"
        ></Table>
        <h2 class="text-start">Group3</h2>
        <Table
          :incomingHeaders="incomingHeaders"
          :IncomingData="IncomingData"
        ></Table>
      </div>
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
