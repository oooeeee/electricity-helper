<template>
  <div class="main-app">
    <div class="header"></div>
    <Streets/>
  </div>
</template>

<script>
import Bus from './bus'
import Vue from 'vue'
import Streets from './components/Streets.vue'
import { BASE_URL, common_state_store } from './shared'
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";

Vue.use(Toast, {
  transition: "Vue-Toastification__bounce",
  maxToasts: 20,
  newestOnTop: false,
});



export default {
  name: 'app',

  components: {
    Streets,
  },

  data: () => ({
    common_store: common_state_store,
    busy_streets: false,
    busy_street: false,
    street: '',
    schedulers: [],
  }),

  created() {
    Bus.$on('update_street', (street, need_clean) => this.get_street(street, need_clean))
    Bus.$on('notification_info', (message) => this.notification_info(message))
    Bus.$on('notification_error', (message) => this.notification_error(message))
    this.get_streets()
    this.schedulers.push(setInterval(() => this.get_street(), 10000))
  },

  beforeDestroy() {
    this.schedulers.forEach((i) => clearInterval(i))
  },

  methods: {
    clean_street() {
    },
    async get_streets() {
      if (this.busy_streets) return
      this.busy_streets = true;
      try {
        const resp = await fetch(BASE_URL + "/storage/streets")
        if (resp.status != 200){
          const message = `Response code ${resp.status}: ${await resp.text()}`;
          if (typeof Error !== "undefined") {
            throw new Error(message);
          }
          throw message;
        }
        const streets = await resp.json()
        this.common_store.setStreetsAction(streets)
      } catch (err) {
        Bus.$emit("notification_error", `${err}`)
        setTimeout(() => this.get_streets(), 5000);
      }
      this.busy_streets = false;
    },
    async get_street(street, need_clean) {
      if (street) this.street = street;
      if (!this.street) return;
      if (this.busy_street) return;
      this.busy_street = true;
      if (need_clean) this.common_store.setStreetAction({});
      try {
        const resp = await fetch(BASE_URL + `/storage/street/${this.street}/latest`)
        if (resp.status != 200){
          const message = `Response code ${resp.status}: ${await resp.text()}`;
          if (typeof Error !== "undefined") {
            throw new Error(message);
          }
          throw message;
        }
        const street = await resp.json()
        this.common_store.setStreetAction(street)
      } catch (err) {
        Bus.$emit("notification_error", `${err}`)
      }
      this.busy_street = false;
    },
    notification_error(message) {
      var toast_params = {
        position: "top-right",
        timeout: 20000,
        closeOnClick: true,
        pauseOnFocusLoss: true,
        pauseOnHover: true,
        draggable: true,
        draggablePercent: 0.6,
        hideCloseButton: false,
        hideProgressBar: false,
        icon: true,
      }
      this.$toast.error(message, toast_params)
    },
    notification_info(message) {
      var toast_params = {
        position: "top-right",
        timeout: 5000,
        closeOnClick: true,
        pauseOnFocusLoss: true,
        pauseOnHover: true,
        draggable: true,
        draggablePercent: 0.6,
        hideCloseButton: false,
        hideProgressBar: false,
        icon: true,
      }
      this.$toast.info(message, toast_params)
    },

  }
}
</script>

<style>
.main-app {
  width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.header {
  margin: 20px 0 40px 0;
}

.header > div, .header > a {
  display: inline;
  margin-right: 10px;
}

.table-header {
  border-bottom: 1px solid black;
  display: flex;
}

.table-header > .table-cell {
  font-weight: 600;
}

.table-row {
  border-bottom: 1px solid darkgray;
  display: flex;
}

.table-row:last-child {
  border-bottom: none;
  margin-bottom: 20px;
}

.table-cell {
  display: flex;
  padding: 10px;
  justify-content: center;
  flex-direction: column;
}

.table-cell.tc-5 {
  width: 5%;
}

.table-cell.tc-20 {
  width: 20%;
}

.table-cell.tc-30 {
  width: 30%;
}

.table-cell.tc-40 {
  width: 40%;
}

.table-cell.tc-50 {
  width: 50%;
}

.table-cell.tc-60 {
  width: 60%;
}

.buttons {
  display: flex;
}

.buttons > * {
  margin-right: 10px;
}

.labels > .label {
  margin-right: 5px;
}

</style>
