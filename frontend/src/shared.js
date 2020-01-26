export const BASE_URL = (process.env.NODE_ENV == 'development') ? 'http://localhost:8080' : '';

export const common_state_store = {
  state: {
    street: {},
    streets: [],
  },
  setStreetAction (newValue) {
    this.state.street = newValue
  },
  setStreetsAction (newValue) {
    this.state.streets = newValue
  },
}
