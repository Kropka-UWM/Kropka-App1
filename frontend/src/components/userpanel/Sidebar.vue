<script setup lang="ts">
import { computed } from "vue";
import { key } from "@/store";
import { useStore } from "vuex";

const store = useStore(key);

function logout() {
  store.dispatch("logout");
}

let dayMode = store.state.darkMode;

function changeMode() {
  store.commit("SET_DAY_MODE");
}
</script>

<template>
  <div
    class="d-flex flex-column flex-shrink-0 p-3 bg-light"
    style="width: 280px"
  >
    <a
      href="/"
      class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none"
    >
      <svg class="bi me-2" width="40" height="32">
        <use xlink:href="/@/assets/icons/bootstrap-icons.svg#bootstrap"></use>
      </svg>
      <span class="fs-4">Sidebar</span>
    </a>
    <hr />
    <ul class="nav nav-pills flex-column mb-auto">
      <li>
        <router-link class="navbar-brand" to="/panel/groupusers">
          <svg class="bi me-2" width="16" height="16">
            <use
              xlink:href="@/assets/icons/bootstrap-icons.svg#speedometer2"
            ></use>
          </svg>
          Group users</router-link
        >
      </li>
      <li>
        <router-link class="navbar-brand" to="/panel/userpanel">
          <svg class="bi me-2" width="16" height="16">
            <use
              xlink:href="@/assets/icons/bootstrap-icons.svg#speedometer2"
            ></use>
          </svg>
          User panel</router-link
        >
      </li>
      <li>
        <router-link class="navbar-brand" to="/panel/companypanel">
          <svg class="bi me-2" width="16" height="16">
            <use
              xlink:href="@/assets/icons/bootstrap-icons.svg#speedometer2"
            ></use>
          </svg>
          Company panel</router-link
        >
      </li>
      <li>
        <router-link class="navbar-brand" to="/panel/adminpanel">
          <svg class="bi me-2" width="16" height="16">
            <use
              xlink:href="@/assets/icons/bootstrap-icons.svg#speedometer2"
            ></use>
          </svg>
          Admin panel</router-link
        >
      </li>
      <li>
        <router-link class="navbar-brand" to="/panel/waitingphase">
          <svg class="bi me-2" width="16" height="16">
            <use
              xlink:href="@/assets/icons/bootstrap-icons.svg#speedometer2"
            ></use>
          </svg>
          Waiting phase</router-link
        >
      </li>
    </ul>
    <div class="form-check form-switch">
      <input
        class="form-check-input"
        type="checkbox"
        id="flexSwitchCheckDefault"
        v-model="dayMode"
        @change="changeMode"
      />
      <label class="form-check-label" for="flexSwitchCheckDefault"
        >Day/Light mode</label
      >
    </div>
    <hr />
    <div class="dropdown">
      <a
        href="#"
        class="d-flex align-items-center link-dark text-decoration-none dropdown-toggle"
        id="dropdownUser2"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        <img
          src="https://github.com/mdo.png"
          alt=""
          width="32"
          height="32"
          class="rounded-circle me-2"
        />
        <strong>{{ store.state.user.name }}</strong>
      </a>
      <ul
        class="dropdown-menu text-small shadow"
        aria-labelledby="dropdownUser2"
        style=""
      >
        <li><hr class="dropdown-divider" /></li>
        <li><a class="dropdown-item" href="#" @click="logout">Sign out</a></li>
      </ul>
    </div>
  </div>
</template>
