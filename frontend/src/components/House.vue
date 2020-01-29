<template>
  <div v-if="show_house">
    <div v-if="edit_mode">
      <div class="container">
        <div :class="'row row-cols-'+dataTypes.length">
          <div class="col" v-for="(data_type, data_type_index) in dataTypes" :key="data_type_index">
            {{ data_type=='date'?`House ${house}`:data_type }}
          </div>
        </div>
        <div :class="'row row-cols-'+dataTypes.length" v-for="(date_info, date_index) in house_info" :key="date_index">
          <div class="col" v-for="(data_type, data_type_index) in dataTypes" :key="data_type_index">
            {{ date_info[data_type] }}
          </div>
        </div>
      </div>
      <div class="container">
        <UpdateButton 
          class="row"
          :street_name="street_name"
          :house_name="house"
          :date="house_info[house_info.length-1].date"
          :data_type="data_type"
          :data_value="house_info[house_info.length-1][data_type]"
          v-for="(data_type, data_type_index) in common_store.state.dataTypes" :key="data_type_index"
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
  computed: {
    dataTypes() {
      return ['date', ...this.common_store.state.dataTypes]
    },
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
