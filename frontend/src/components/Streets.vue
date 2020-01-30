<template>
  <div>
    <div class="streets-container">
      <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          {{active_street?active_street:'Choose street'}}
        </button>
        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
          <a v-for="(street, street_index) in streets" :key="street_index" class="dropdown-item" href="#" @click.prevent="requestStreet(street)"> {{street}}</a>
          <a class="dropdown-item" :href="base_url + '/storage/export.xlsx'">Export all</a>
        </div>
      </div>
      <button v-if="show_back_button" type="button" class="btn btn-primary" @click.prevent="back_houses()">Back</button>
    </div>
    <div v-if="this.active_street" v-bind:class="{'streets-container': !show_back_button}">
      <div v-for="(house_info, house_index) in street_info" :key="house_index">
        <House :house=house_index :house_info=house_info :street_name=active_street />
      </div>
    </div>
  </div>
</template>

<script>
import Bus from '../bus'
import House from './House.vue'
import { BASE_URL, common_state_store } from '../shared'

export default {
  components: {
    House
  },

  data: () => ({
    common_store: common_state_store,
    active_street: '',
    show_back_button: false,
    base_url: BASE_URL,
  }),

  computed: {
    streets() {
      return this.common_store.state.streets
    },
    street_info() {
      return this.common_store.state.street
    },
  },
  created() {
    Bus.$on('show_houses', () => {this.show_back_button = false})
    Bus.$on('hide_houses', () => {this.show_back_button = true})
  },

  methods: {
    back_houses() {
      Bus.$emit('show_houses')
    },
    requestStreet(street) {
      this.active_street = street;
      this.back_houses()
      Bus.$emit('update_street', this.active_street, true);
    }
  }
}
</script>

<style>
.streets-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
</style>
