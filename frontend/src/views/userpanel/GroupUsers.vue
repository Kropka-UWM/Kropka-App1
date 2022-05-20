<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div
            v-for="(lists, value) in multipleLists"
            v-bind:key="value"
            :class="value === 'unsetted' ? 'col-lg-12' : 'col-lg-3'"
          >
            <div>
              <h3>{{ value }}</h3>
              <draggable
                class="list-group"
                :list="lists"
                group="people"
                @change="log"
                itemKey="name"
              >
                <template #item="{ element, index }">
                  <div class="list-group-item">
                    {{ element.name }} {{ index }}
                  </div>
                </template>
              </draggable>
            </div>
          </div>

          <div v-if="rawData">{{ rawData }}</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import draggable from "vuedraggable";
export default {
  name: "two-lists",
  display: "Two Lists",
  order: 1,
  components: {
    draggable,
  },
  data() {
    return {
      multipleLists: {
        unsetted: [
          { name: "John", id: 1 },
          { name: "Joao", id: 2 },
          { name: "Jean", id: 3 },
          { name: "Gerard", id: 4 },
        ],
        list1: [
          { name: "John", id: 1 },
          { name: "Joao", id: 2 },
          { name: "Jean", id: 3 },
          { name: "Gerard", id: 4 },
        ],
        list2: [
          { name: "Juan", id: 5 },
          { name: "Edgard", id: 6 },
          { name: "Johnson", id: 7 },
        ],
      },
    };
  },
  methods: {
    add: function () {
      this.list.push({ name: "Juan" });
    },
    replace: function () {
      this.list = [{ name: "Edgard" }];
    },
    clone: function (el) {
      return {
        name: el.name + " cloned",
      };
    },
    log: function (evt) {
      window.console.log(evt);
    },
  },
  computed: {
    rawData() {
      // `this` points to the component instance
      return JSON.parse(JSON.stringify(this.multipleLists));
    },
  },
};
</script>
