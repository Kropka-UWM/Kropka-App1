import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import UserLayout from "../views/account/Layout.vue";
import UserRegister from "../views/account/Register.vue";
import UserLogin from "../views/account/Login.vue";
import GroupUsers from "../views/userpanel/GroupUsers.vue"
import UserPanel from "../views/userpanel/UserPanel.vue"
import CompanyPanel from "../views/userpanel/CompanyPanel.vue"
import WaitingPhase from "../views/userpanel/WaitingPhase.vue"
import AdminPanel from "../views/userpanel/AdminPanel.vue"

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "UserLayout",
    component: UserLayout,
    children: [
      {
        alias: "",
        path: "login",
        name: "UserLogin",
        component: UserLogin,
        meta: {
          arleadyLoggedIn: true,
        },
      },
      {
        alias: "register",
        path: "register",
        name: "UserRegister",
        component: UserRegister,
        meta: {
          arleadyLoggedIn: true,
        },
      },
    ],
  },
  {
    path: "/panel",
    name: "Panel",
    children: [
      {
        path: "groupusers",
        name: "GroupUsers",
        component: GroupUsers,
      },
      {
        path: "UserPanel",
        name: "UserPanel",
        component: UserPanel,
      },
      {
        path: "CompanyPanel",
        name: "CompanyPanel",
        component: CompanyPanel,
      },
      {
        path: "WaitingPhase",
        name: "WaitingPhase",
        component: WaitingPhase,
      },
      {
        path: "AdminPanel",
        name: "AdminPanel",
        component: AdminPanel,
      },
    ],
    meta: {
      requiresAuth: true,
    },
    // route level code-splitting
    // this generates a separate chunk (panel.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "panel" */ "../views/userpanel/Layout.vue"),
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

  if (to.matched.some((record) => record.meta.arleadyLoggedIn) && loggedIn) {
    next("/panel");
  }
  next();
});

export default router;
