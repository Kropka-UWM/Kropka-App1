import { InjectionKey } from "vue";
import { createStore, Store } from "vuex";
import { User } from "../types";
import axios from "axios";
import { Notification } from "../types";

// define your typings for the store state
export interface State {
  user: User;
  darkMode: boolean;
  toasts: Notification[];
  userToken: string;
}

// define injection key
export const key: InjectionKey<Store<State>> = Symbol();

export const store = createStore<State>({
  state: {
    user: {} as User,
    darkMode: false,
    toasts: [],
    userToken: "",
  },
  mutations: {
    SET_USER_DATA(state, userData) {
      state.user = userData;
      localStorage.setItem("user", JSON.stringify(userData));
      axios.defaults.headers.common[
        "Authorization"
      ] = `Bearer ${userData.access_token}`;
      state.userToken = userData.access_token;
    },
    CLEAR_USER_DATA() {
      localStorage.removeItem("user");
      location.reload();
    },
    SET_DAY_MODE(state) {
      state.darkMode = !state.darkMode;
    },
    ADD_TOAST(state, toast: Notification) {
      state.toasts.push(toast);
    }
  },
  actions: {
    async register({ commit }, credentials) {
      const { data } = await axios.post(
        "http://vps-9ee2e9ea.vps.ovh.net:8000/register/",
        credentials
      );
      commit("SET_USER_DATA", data);
    },
    async login({ commit }, credentials) {
      const { data } = await axios.post(
        "http://vps-9ee2e9ea.vps.ovh.net:8000/login/",
        credentials
      );
      commit("SET_USER_DATA", data);
    },
    logout({ commit }) {
      commit("CLEAR_USER_DATA");
    },
  },
  getters: {
    loggedIn(state) {
      return !!state.user.email;
    },
  },
});
