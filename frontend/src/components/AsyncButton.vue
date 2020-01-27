<template>
  <button 
    v-bind:class="{
      'disabled': (this.pending | this.disabled),
      'btn-info': !(this.error | this.red),
      'btn-danger': (this.error | this.red),
    }"
    type="button"
    class="btn"
    @click.prevent="requestData()"
  >
    {{this.text}}
  </button>
</template>

<script>
import Bus from '../bus'
import { BASE_URL } from '../shared'

export default {
  props: {
    url: { type: String, default: "", required: true },
    method: { type: String, default: "get", required: false },
    params: { type: Object, default: () => ({}) },
    text: { type: String, default: "Button", required: false },
    red: { type: Boolean, default: false, required: false },
    disabled: { type: Boolean, default: false, required: false },
    update_envs_after_request: { type: Boolean, default: true, required: false },
    callback_success: { type: Function, default: null, required: false },
    callback_failure: { type: Function, default: null, required: false },
  },
  data() {
    return {
      pending: false,
      error: false,
      data: null
    };
  },
  methods: {
    async requestData() {
      this.pending = true;
      try {
        const resp = await fetch(
          BASE_URL + this.url,
          {
            method: this.method,
            headers: { 'Content-Type': 'application/json; charset=utf-8' },
            body: JSON.stringify(this.params)
          }
        )
        if (resp.status != 200){
          const message = `Response code ${resp.status}: ${await resp.text()}`;
          if (typeof Error !== "undefined") {
            throw new Error(message);
          }
          throw message;
        }
        const data = await resp.json()
        this.data = data;
        this.error = false;
        if (this.callback_success) this.callback_success();
      } catch (e) {
        this.data = null;
        this.error = e;
        Bus.$emit("notification_error", `${this.error}`)
        if (this.callback_failure) this.callback_failure();
      }
      this.pending = false;
      if (this.update_envs_after_request) {Bus.$emit('update_envs')}
    }
  }
}
</script>