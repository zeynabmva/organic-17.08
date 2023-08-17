// src/store.js

import { createStore, combineReducers } from "redux";
import authReducer from "./reducers/authReducer";

const rootReducer = combineReducers({
  auth: authReducer,
  // digər reducer-lar...
});

const store = createStore(rootReducer);

export default store;