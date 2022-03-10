import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Home from "../views/Home.vue";
import UserLayout from "../views/user/Layout.vue";
import UserRegister from "../views/user/Register.vue";
import UserLogin from "../views/user/Login.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/user",
    name: "UserLayout",
    component: UserLayout,
    children: [
      {
        path: "login",
        name: "UserLogin",
        component: UserLogin,
      },
      {
        path: "register",
        name: "UserRegister",
        component: UserRegister,
      },
    ],
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/panel",
    name: "Panel",
    meta: {
      requiresAuth: true,
    },
    // route level code-splitting
    // this generates a separate chunk (panel.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "panel" */ "../views/Panel.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const loggedIn = localStorage.getItem("user");

  if (to.matched.some((record) => record.meta.requiresAuth) && !loggedIn) {
    next("/");
  }
  next();
});

export default router;
