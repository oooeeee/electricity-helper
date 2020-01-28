<template>
  <div>
    <div class="dropdown">
      <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        {{active_street?active_street:'Choose street'}}
      </button>
      <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
        <a v-for="(street, street_index) in streets" :key="street_index" class="dropdown-item" href="#" @click.prevent="requestStreet(street)"> {{street}}</a>
      </div>
    </div>
    <div v-if="this.active_street" class="houses">
      <div v-for="(house_info, house_index) in street_info" :key="house_index">
        <House :house=house_index :house_info=house_info :street_name=active_street />
      </div>
    </div>
  </div>
</template>

<script>
import Bus from '../bus'
import House from './House.vue'
import { common_state_store } from '../shared'

export default {
  components: {
    House
  },

  data: () => ({
    common_store: common_state_store,
    active_street: '',
  }),

  computed: {
    streets() {
      return this.common_store.state.streets
    },
    street_info() {
      return this.common_store.state.street
    },
  },

  methods: {
    requestStreet(street) {
      this.active_street = street;
      Bus.$emit('update_street', this.active_street, true);
    }
  }
}
</script>

<style>
.houses {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
</style>
