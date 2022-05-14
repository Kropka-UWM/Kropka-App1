import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { store, key } from "./store";
import "@/scss/main.scss";
import "bootstrap/dist/js/bootstrap.min.js";

createApp(App).use(store, key).use(router).mount("#app");
