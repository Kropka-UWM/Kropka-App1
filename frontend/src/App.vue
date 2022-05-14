<script setup lang="ts">
import { onMounted } from "vue";
import axios from "axios";
import { key } from "@/store";
import { useStore } from "vuex";
import ToastMangaer from "./components/ToastMangaer.vue";
import ToastManager from "./components/ToastManager.vue";

const store = useStore(key);

// Auto login
onMounted(() => {
  const userString = localStorage.getItem("user");
  if (userString) {
    const userData = JSON.parse(userString);
    store.commit("SET_USER_DATA", userData);
  }
  axios.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error.response.status === 401) {
        store.dispatch("logout");
      }
      return Promise.reject(error);
    }
  );
});
</script>

<template>
  <ToastManager></ToastManager>
  <main v-bind:class="{ dark: store.state.darkMode }">
    <router-view />
  </main>
</template>

<style lang="scss">
body {
  min-height: 100vh;
}

#app {
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
