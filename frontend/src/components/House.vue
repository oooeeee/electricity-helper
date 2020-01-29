<template>
  <div v-if="show_house">
    <div v-if="edit_mode">
      <div class="container">
        <div class="row row-cols-3">
          <div class="col">House {{house}}</div>
          <div class="col">DAY</div>
          <div class="col">NIGHT</div>
        </div>
        <div class="row row-cols-3" v-for="(date_info, date_index) in house_info" :key="date_index">
          <div class="col">{{ date_info.date }}</div>
          <div class="col">{{ date_info.DAY }}</div>
          <div class="col">{{ date_info.NIGHT }}</div>
        </div>
      </div>
      <div class="container">
        <UpdateButton 
          class="row"
          :street_name="street_name"
          :house_name="house"
          :date="house_info[1].date"
          :data_type="'DAY'"
          :data_value="house_info[1].DAY"
        />
        <UpdateButton 
          class="row"
          :street_name="street_name"
          :house_name="house"
          :date="house_info[1].date"
          :data_type="'NIGHT'"
          :data_value="house_info[1].NIGHT"
        />
      </div>
    </div>
    <div v-else>
      <button type="button" class="btn btn-primary" @click.prevent="switchToEditMode()">{{this.house}}</button>
    </div>
  </div>
</template>
<script>

import Bus from '../bus'
import { common_state_store } from '../shared'
import UpdateButton from './UpdateButton.vue'

export default {
  components: {
    UpdateButton
  },
  props: {
    street_name: { type: String, required: true },
    house_info: { type: Array, required: true },
    house: {type: String, required: true },
  },

  created() {
    Bus.$on('hide_houses', () => {if (!this.edit_mode) this.show_house = false})
    Bus.$on('show_houses', () => {this.show_house = true; this.edit_mode = false})
  },

  data: () => ({
    common_store: common_state_store,
    edit_mode: false,
    show_house: true,
  }),

  methods: {
    switchToEditMode() {
      this.edit_mode = true;
      Bus.$emit("hide_houses")
    },
    returnToCommonMode() {
      Bus.$emit("show_houses")
    }
  },
}

</script>
