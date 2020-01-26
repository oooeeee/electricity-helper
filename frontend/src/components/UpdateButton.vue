<template>
  <div>
    <div class="input-group">
      <div class="input-group-prepend">
        <div class="input-group-text">{{this.data_type}}</div>
      </div>
      <input type="text" name="data_value" class="form-control" v-model="data_value_" :disabled="form_locked">
      <span v-if="form_locked" class="input-group-btn">
        <button type="button" class="btn btn-primary" @click.prevent="form_locked=false">Edit</button>
      </span>
      <span v-else class="input-group-btn">
        <AsyncButton
          :url='`/storage/street/${this.street_name}/house/${this.house_name}/set/${this.date}/${this.data_type}/${this.data_value_}`'
          method='put'
          text="Update"
          :callback_success='() => {this.form_locked = true}'
        />
        <button type="button" class="btn btn-info" @click.prevent="form_locked=true;data_value_=data_value">X</button>
      </span>
    </div>
  </div>
</template>

<script>
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
      form_locked: true,
    };
  },
}
</script>