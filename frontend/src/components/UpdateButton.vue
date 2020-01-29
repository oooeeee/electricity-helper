<template>
  <div>
    <div class="input-group">
      <div class="input-group-prepend">
        <div class="input-group-text">{{this.data_type}}</div>
      </div>
      <input type="number" :min="data_value" name="data_value" class="form-control" v-model="data_value_">
      <span class="input-group-btn">
        <AsyncButton
          :url='`/storage/street/${this.street_name}/house/${this.house_name}/set/${this.date}/${this.data_type}/${this.data_value_}`'
          method='put'
          text="Update"
          :callback_success='success_edit'
        />
      </span>
    </div>
  </div>
</template>

<script>
import Bus from '../bus'
import AsyncButton from './AsyncButton.vue'

export default {
  components: {
    AsyncButton,
  },
  props: {
    street_name: { type: String, required: true },
    house_name: { type: String, required: true },
    date: { type: String, required: true },
    data_type: { type: String, required: true },
    data_value: { type: String, required: true },
  },
  data() {
    return {
      data_value_: this.data_value,
    };
  },
  methods: {
    success_edit() {
      Bus.$emit("update_street", this.street_name, false)
    }
  },
}
</script>