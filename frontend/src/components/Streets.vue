<template>
  <div>
    <ul class="nav nav-tabs">
      <li class="nav-item" v-for="(street, street_index) in streets" :key="street_index">
        <a
          class="nav-link"
          href="#"
          @click.prevent="requestStreet(street)"
          v-bind:class="{'active': (street == active_street)}"
        > {{street}}  </a>
      </li>
    </ul>
    <div v-if="this.active_street">
      <div class="table-row">
        <div class="table-cell tc-10"> Current street is {{this.active_street}} </div>
        <div class="table-cell tc-30"> There will be buttons </div>
      </div>
      <div v-for="(house_info, house_index) in street_info" :key="house_index">
        <HouseRow :house=house_index :house_info=house_info :street_name=active_street />
      </div>
    </div>
    <div v-else>
      No street is selected
    </div>
  </div>
</template>

<script>
import Bus from '../bus'
import HouseRow from './HouseRow.vue'
import { common_state_store } from '../shared'

export default {
  components: {
    HouseRow
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
