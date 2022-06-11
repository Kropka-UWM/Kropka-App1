<script setup lang="ts">
import { reactive, ref } from "vue";
import { User, ErrorMessage } from "../../types";
import "../../store/index";
import { key } from "../../store";
import { useStore } from "vuex";
import { useRouter } from "vue-router";

const store = useStore(key);

const router = useRouter();

let error = ref<ErrorMessage>(null);

const user: User = reactive({
  name: "First name",
  last_name: "Last name",
  userName: "username",
  email: "Email",
  password: "Password",
  userType: "Student",
});

function register() {
  store
    .dispatch("register", {
      first_name: user.name,
      last_name: user.lastName,
      email: user.email,
      username: user.userName,
      password: user.password,
      account_type: user.userType,
    })
    .then(() => {
      store.commit("ADD_TOAST", {
        text: "Zarejestrowano pomyślnie",
        toastClass: "bg-success",
        textClass: "text-white",
      });
      router.push({ name: "login" });
    })
    .catch((err) => {
      store.commit("ADD_TOAST", {
        text: err.response.data,
        toastClass: "bg-danger",
        textClass: "text-white",
      });
    });
}
</script>

<template>
  <div class="register">
    <form @submit.prevent="register">
      <label for="userName"> Username: </label>
      <input v-model="user.userName" type="text" name="userName" value />

      <label for="name"> First Name: </label>
      <input v-model="user.name" type="text" name="name" value />

      <label for="lastName"> last Name: </label>
      <input v-model="user.lastName" type="text" name="name" value />

      <label for="email"> Email: </label>
      <input v-model="user.email" type="email" name="email" value />

      <label for="password"> Password: </label>
      <input v-model="user.password" type="password" name="password" value />

      <label for="userType">User type:</label>

      <select v-model="user.userType" name="userType" id="userType">
        <option value="company">Company</option>
        <option value="leader">Leader</option>
        <option value="student leader">Student leader</option>
        <option value="student">Student</option>
      </select>

      <button type="submit" name="button">Register</button>
    </form>
    <p v-if="error">{{ error }}</p>
  </div>
</template>
