<script setup lang="ts">
import SideBar from "@/components/userpanel/Sidebar.vue";

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
      <router-view></router-view>
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
