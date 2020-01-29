<template>
  <div v-if="show_house">
    <div v-if="edit_mode">
      <center><h3>House {{house}}</h3></center>
      <div class="table-row" v-for="(date_info, date_index) in house_info" :key="date_index">
        <div class="table-cell tc-10">
          <div class="labels">
            <span class="badge badge-info">{{ date_info.date }}</span>
          </div>
        </div>
        <div class="table-cell tc-30" v-for="(data_value, data_type) in date_info" :key="data_type">
          <UpdateButton 
            :street_name="street_name"
            :house_name="house"
            :date="date_info.date"
            :data_type="data_type"
            :data_value="data_value"
          />
        </div>
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
