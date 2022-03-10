<script setup lang="ts">
import { computed } from "vue";
import { key } from "@/store";
import { useStore } from "vuex";

const store = useStore(key);

const loggedIn = computed(() => store.getters.loggedIn);

function logout() {
  store.dispatch("logout");
}
</script>

<template>
  <div>
    <p>Zalogowany: {{ loggedIn }}, jako: {{ store.state.user.email }}</p>
    <div id="nav">
      <router-link v-if="!loggedIn" :to="{ name: 'UserLogin' }"
        >Login
      </router-link>
      <button v-if="loggedIn" @click="logout">Logout</button>

      <router-link v-if="!loggedIn" :to="{ name: 'UserRegister' }"
        >Register</router-link
      >
    </div>
    <router-view />
  </div>
</template>
