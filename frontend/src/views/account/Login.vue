<script setup lang="ts">
import { reactive, ref } from "vue";
import { LoginData, ErrorMessage } from "../../types";
import "../../store/index";
import { key } from "../../store";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { useForm, useField } from "vee-validate";
import * as yup from "yup";
import { SchemaOf } from "yup";

const store = useStore(key);

const router = useRouter();

let error = ref<ErrorMessage>(null);

// Schema interface
interface loginInterface {
  email: string;
  password: string;
}

// Define a validation schema
const schema: SchemaOf<loginInterface> = yup.object().shape({
  email: yup.string().required().email(),
  password: yup.string().required().min(8),
});
// Create a form context with the validation schema
useForm({
  validationSchema: schema,
});
// No need to define rules for fields
const { value: email, errorMessage: emailError } = useField("email");
const { value: password, errorMessage: passwordError } = useField("password");

function login() {
  store
    .dispatch("login", {
      email: email.value,
      password: password.value,
    })
    .then(() => {
      router.push({ name: "Panel" });
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
  <div class="login">
    <h2>Just log in!</h2>
    <form @submit.prevent="login">
      <div class="standard-form__container">
        <label for="email"> Email: </label>
        <div class="standard-form__container__input-container">
          <input
            v-model="email"
            type="email"
            name="email"
            value
            class="form-control standard-form__container__input-container__input"
            :class="{ 'is-invalid': emailError }"
          />

          <span v-if="emailError" class="invalid-feedback">{{
            emailError
          }}</span>
        </div>
      </div>
      <div class="standard-form__container">
        <label for="password"> Password: </label>
        <div class="standard-form__container__input-container">
          <input
            v-model="password"
            type="password"
            name="password"
            value
            class="form-control standard-form__container__input-container__input"
            :class="{ 'is-invalid': passwordError }"
          />
          <span v-if="passwordError" class="invalid-feedback">{{
            passwordError
          }}</span>
        </div>
      </div>

      <button type="submit" name="button" class="btn btn-primary mt-3">
        Login
      </button>
    </form>

    <p v-if="error">{{ error }}</p>

    <router-link class="navbar-brand" to="/register"
      >Zarejestruj się</router-link
    >
  </div>
</template>
