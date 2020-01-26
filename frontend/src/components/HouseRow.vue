<template>
  <div>
    <div class="table-row">
      <div class="table-cell tc-10"> House {{this.house}} </div>
    </div>
    <div class="table-row" v-for="(date_info, date) in house_info" :key="date">
      <div class="table-cell tc-10">
        <div class="labels">
          <span class="badge badge-info">{{ date }}</span>
        </div>
      </div>
      <div class="table-cell tc-30" v-for="(data_value, data_type) in date_info" :key="data_type">
        <UpdateButton 
          :street_name="street_name"
          :house_name="house"
          :date="date"
          :data_type="data_type"
          :data_value="data_value"
        />
      </div>
    </div>
  </div>
</template>
<script>

import { common_state_store } from '../shared'
import UpdateButton from './UpdateButton.vue'

export default {
  components: {
    UpdateButton
  },
  props: {
    street_name: { type: String, required: true },
    house_info: { type: Object, required: true },
    house: {type: String, required: true },
  },

  data: () => ({
    common_store: common_state_store,
  }),

}
</script>
