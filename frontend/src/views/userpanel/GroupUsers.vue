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
                <template #item="{ element }">
                  <div class="list-group-item">
                    {{ element.Imie }} - {{ element.Srednia }}
                  </div>
                </template>
              </draggable>
            </div>
          </div>
          <button type="button" class="btn btn-primary mt-5 mb-5">
            Przydziel automatycznie
          </button>

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
          {
            Imie: "John",
            Nazwisko: "John",
            Srednia: "5",
            Priorytet: ["Akra", "Programisci"],
            id: 1,
          },
          {
            Imie: "John",
            Nazwisko: "John",
            Srednia: "5",
            Priorytet: ["Akra", "Programisci"],
            id: 2,
          },
          {
            Imie: "John",
            Nazwisko: "John",
            Srednia: "5",
            Priorytet: ["Akra", "Programisci"],
            id: 3,
          },
          {
            Imie: "John",
            Nazwisko: "John",
            Srednia: "5",
            Priorytet: ["Akra", "Programisci"],
            id: 4,
          },
        ],
        Akra: [
          {
            Imie: "John",
            Nazwisko: "John",
            Srednia: "5",
            Priorytet: ["Akra", "Programisci"],
            id: 1,
          },
          {
            Imie: "John",
            Nazwisko: "John",
            Srednia: "5",
            Priorytet: ["Akra", "Programisci"],
            id: 2,
          },
          {
            Imie: "John",
            Nazwisko: "John",
            Srednia: "5",
            Priorytet: ["Akra", "Programisci"],
            id: 3,
          },
          {
            Imie: "John",
            Nazwisko: "John",
            Srednia: "5",
            Priorytet: ["Akra", "Programisci"],
            id: 4,
          },
        ],
        Programisci: [
          {
            Imie: "John",
            Nazwisko: "John",
            Srednia: "5",
            Priorytet: ["Akra", "Programisci"],
            id: 1,
          },
          {
            Imie: "John",
            Nazwisko: "John",
            Srednia: "5",
            Priorytet: ["Akra", "Programisci"],
            id: 2,
          },
          {
            Imie: "John",
            Nazwisko: "John",
            Srednia: "5",
            Priorytet: ["Akra", "Programisci"],
            id: 3,
          },
          {
            Imie: "John",
            Nazwisko: "John",
            Srednia: "5",
            Priorytet: ["Akra", "Programisci"],
            id: 4,
          },
        ],
        Inna: [
          {
            Imie: "John",
            Nazwisko: "John",
            Srednia: "5",
            Priorytet: ["Akra", "Programisci"],
            id: 1,
          },
          {
            Imie: "John",
            Nazwisko: "John",
            Srednia: "5",
            Priorytet: ["Akra", "Programisci"],
            id: 2,
          },
          {
            Imie: "John",
            Nazwisko: "John",
            Srednia: "5",
            Priorytet: ["Akra", "Programisci"],
            id: 3,
          },
          {
            Imie: "John",
            Nazwisko: "John",
            Srednia: "5",
            Priorytet: ["Akra", "Programisci"],
            id: 4,
          },
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
