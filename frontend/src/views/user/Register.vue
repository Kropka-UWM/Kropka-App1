<script setup lang="ts">
import { reactive, ref } from "vue";
import { User, ErrorMessage } from "../../types";
import "../../store/index";
import { key } from "@/store";
import { useStore } from "vuex";
import { useRouter } from "vue-router";

const store = useStore(key);

const router = useRouter();

let error = ref<ErrorMessage>(null);

const user: User = reactive({
  name: "User",
  email: "Email",
  password: "Password",
  userType: "User",
});

function register() {
  store
    .dispatch("register", {
      name: user.name,
      email: user.email,
      password: user.password,
    })
    .then(() => {
      router.push({ name: "About" });
    })
    .catch((err) => {
      error.value = err.response;
    });
}
</script>

<template>
  <div class="register">
    <p>Test: {{ store.state.user.email }}</p>

    <h1>{{ user.name }}</h1>
    <form @submit.prevent="register">
      <label for="name"> Name: </label>
      <input v-model="user.name" type="text" name="name" value />

      <label for="email"> Email: </label>
      <input v-model="user.email" type="email" name="email" value />

      <label for="password"> Password: </label>
      <input v-model="user.password" type="password" name="password" value />

      <button type="submit" name="button">Register</button>
    </form>
    <p v-if="error">{{ error }}</p>
  </div>
</template>
