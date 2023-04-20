import { configureStore } from "@reduxjs/toolkit"
import textReducer from './features/text/textSlice.js'

export const store = configureStore({
  reducer: {
    textData: textReducer
  }
})