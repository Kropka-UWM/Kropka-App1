<script setup lang="ts">
import SideBar from "@/components/userpanel/Sidebar.vue";
import Table from "@/components/Table.vue";
import { onMounted, ref } from "vue";
import { UsersApi } from "@/services/UserDataService";
import { Student, ResponseData } from "@/types";
import { IUser } from "@/services/UserDataService";

const incomingHeaders: Array<string> = [
  "id",
  "name",
  "surname",
  "email",
  "active",
  "company",
];

const IncomingData: Student[] = [
  {
    id: "1",
    name: "Name",
    surname: "surname",
    email: "email@o2.com",
    active: true,
    company: "company",
  },
  {
    id: "1",
    name: "Name",
    surname: "surname",
    email: "email@o2.com",
    active: true,
    company: "company",
  },
  {
    id: "1",
    name: "Name",
    surname: "surname",
    email: "email@o2.com",
    active: true,
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
  <div class="panel-template">
    <SideBar></SideBar>
    <div class="content-container">
      <div class="container-fluid">
        <div class="row">
          <div class="col-lg-12">
            <h1 class="text-start">Users</h1>
            <h2 class="text-start">Students</h2>
            <Table
              :incomingHeaders="incomingHeaders"
              :IncomingData="IncomingData"
            ></Table>
          </div>
        </div>
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
