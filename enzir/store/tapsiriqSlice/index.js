import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

// Backend'den tapsiriqlari getirmek için async thunk
export const fetchTasks = createAsyncThunk('tapsiriqlar/fetchTasks', async () => {
  const response = await axios.get('https://your-backend-api.com/tasks'); // Backend API URL'nizi buraya yazın
  return response.data;
});

const tapsiriqlarSlice = createSlice({
  name: 'tapsiriqlar',
  initialState: {
    tasks: [],
    status: 'idle', // 'idle' | 'loading' | 'succeeded' | 'failed'
    error: null,
    searchQuery: '',
    page: 1,
    itemsPerPage: 10,
  },
  reducers: {
    setSearchQuery: (state, action) => {
      state.searchQuery = action.payload;
    },
    setPage: (state, action) => {
      state.page = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchTasks.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchTasks.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.tasks = action.payload;
      })
      .addCase(fetchTasks.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      });
  },
});

export const { setSearchQuery, setPage } = tapsiriqlarSlice.actions;
export default tapsiriqlarSlice.reducer;