<script setup lang="ts">
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
        <h1 class="text-start">
          Aplikacja jest w trakcie przydzielana ról dla użytkowników
        </h1>
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
