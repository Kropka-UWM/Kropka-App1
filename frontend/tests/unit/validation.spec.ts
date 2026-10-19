import { describe, expect, it } from "vitest";
import { mount } from "@vue/test-utils";
import { createStore } from "vuex";
import { createMemoryHistory, createRouter } from "vue-router";
import Login from "@/views/account/Login.vue";
import { key } from "@/store";

describe("login validation", () => {
  it("rejects invalid credentials with the upgraded Yup schema", async () => {
    const store = createStore({ state: {} });
    const router = createRouter({
      history: createMemoryHistory(),
      routes: [{ path: "/", component: Login }],
    });
    await router.push("/");
    const wrapper = mount(Login, {
      global: { plugins: [[store, key], router] },
    });

    await wrapper.get('input[name="email"]').setValue("invalid-email");
    await wrapper.get('input[name="password"]').setValue("short");
    await expect.poll(() => wrapper.findAll(".invalid-feedback").length).toBe(2);

    await wrapper.get('input[name="email"]').setValue("student@example.com");
    await wrapper.get('input[name="password"]').setValue("valid-password");
    await expect.poll(() => wrapper.findAll(".invalid-feedback").length).toBe(0);
    wrapper.unmount();
  });
});
