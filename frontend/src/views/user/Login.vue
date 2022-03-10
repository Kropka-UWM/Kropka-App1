<script setup lang="ts">
import { reactive, ref } from "vue";
import { LoginData, ErrorMessage } from "../../types";
import "../../store/index";
import { key } from "@/store";
import { useStore } from "vuex";
import { useRouter } from "vue-router";

const store = useStore(key);

const router = useRouter();

let error = ref<ErrorMessage>(null);

const user: LoginData = reactive({
  email: "Email",
  password: "Password",
});

function login() {
  store
    .dispatch("login", {
      email: user.email,
      password: user.password,
    })
    .then(() => {
      router.push({ name: "Panel" });
    })
    .catch((err) => {
      console.log(err.response);
      error.value = err.response;
    });
}
</script>

<template>
  <div class="login">
    <form @submit.prevent="login">
      <label for="email"> Email: </label>
      <input v-model="user.email" type="email" name="email" value />

      <label for="password"> Password: </label>
      <input v-model="user.password" type="password" name="password" value />

      <button type="submit" name="button">Login</button>
    </form>
    <p v-if="error">{{ error }}</p>
  </div>
</template>
