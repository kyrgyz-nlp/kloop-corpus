import { createSlice } from '@reduxjs/toolkit'
import { testNER } from './fixtures.js'

const initialState = {
  text: '@@@@',
  textNER: testNER,
  loading: false,
  error: null,
}

export const textSlice = createSlice({
  name: 'text_data',
  initialState
})

export default textSlice.reducer