<template>
  <div>
    <ul class="nav nav-tabs">
      <li class="nav-item" v-for="(street, street_index) in streets" :key="street_index">
        <a class="nav-link" href="#" @click.prevent="requestStreet(street)"> {{street}} <!-- v-bind:class="{'active': (street == '1-я ЛИНИЯ')}" --> </a>
      </li>
    </ul>
    <div v-if="this.street">
      <div class="table-row">
        <div class="table-cell tc-10"> Current street is {{this.street}} </div>
        <div class="table-cell tc-30"> There will be buttons </div>
      </div>
      <div class="table-row" v-for="(house_info, house_index) in street_info" :key="house_index">
        <div class="table-cell tc-20"> Current house {{house_index}}, info is {{house_info}} </div>
      </div>
    </div>
    <div v-else>
      No street is selected
    </div>
  </div>
</template>

<script>
import Bus from '../bus'
import { common_state_store } from '../shared'

export default {

  data: () => ({
    common_store: common_state_store,
    street: '',
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
      this.street = street;
      Bus.$emit('update_street', this.street, true);
    }
  }
}
</script>
