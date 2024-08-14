import axios from 'axios';
import { API_URL } from '../constants';
import { toast } from 'react-toastify';

export const SET_USER = 'SET_USER';
export const SET_TOKEN = 'SET_TOKEN';
export const SET_CONVERSATIONS = 'SET_CONVERSATIONS';
export const SET_INSIGHTS = 'SET_INSIGHTS';
export const SET_ERROR = 'SET_ERROR';

export const setUser = (user) => ({
  type: SET_USER,
  user,
});

export const setToken = (token) => ({
  type: SET_TOKEN,
  token,
});

export const setConversations = (conversations) => ({
  type: SET_CONVERSATIONS,
  conversations,
});

export const setInsights = (insights) => ({
  type: SET_INSIGHTS,
  insights,
});

export const setError = (error) => ({
  type: SET_ERROR,
  error,
});

export const login = (credentials) => async (dispatch) => {
  try {
    const response = await axios.post(`${API_URL}/auth/login`, credentials);
    const { token, user } = response.data;
    dispatch(setToken(token));
    dispatch(setUser(user));
    toast.success('Logged in successfully!');
  } catch (error) {
    dispatch(setError(error.response.data.error));
    toast.error('Login failed!');
  }
};

export const register = (credentials) => async (dispatch) => {
  try {
    const response = await axios.post(`${API_URL}/auth/register`, credentials);
    const { token, user } = response.data;
    dispatch(setToken(token));
    dispatch(setUser(user));
    toast.success('Registered successfully!');
  } catch (error) {
    dispatch(setError(error.response.data.error));
    toast.error('Registration failed!');
  }
};

export const getConversations = () => async (dispatch) => {
  try {
    const response = await axios.get(`${API_URL}/conversations`);
    const conversations = response.data;
    dispatch(setConversations(conversations));
  } catch (error) {
    dispatch(setError(error.response.data.error));
  }
};

export const getInsights = () => async (dispatch) => {
  try {
    const response = await axios.get(`${API_URL}/insights`);
    const insights = response.data;
    dispatch(setInsights(insights));
  } catch (error) {
    dispatch(setError(error.response.data.error));
  }
};

export const sendMessage = (message) => async (dispatch) => {
  try {
    const response = await axios.post(`${API_URL}/conversations`, message);
    const conversation = response.data;
    dispatch(setConversations([...conversation]));
  } catch (error) {
    dispatch(setError(error.response.data.error));
  }
};
