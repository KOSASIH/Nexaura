import { combineReducers } from 'redux';
import { SET_USER, SET_TOKEN, SET_CONVERSATIONS, SET_INSIGHTS, SET_ERROR } from '../actions';

const initialState = {
  user: null,
  token: null,
  conversations: [],
  insights: [],
  error: null,
};

const userReducer = (state = initialState.user, action) => {
  switch (action.type) {
    case SET_USER:
      return action.user;
    default:
      return state;
  }
};

const tokenReducer = (state = initialState.token, action) => {
  switch (action.type) {
    case SET_TOKEN:
      return action.token;
    default:
      return state;
  }
};

const conversationsReducer = (state = initialState.conversations, action) => {
  switch (action.type) {
    case SET_CONVERSATIONS:
      return action.conversations;
    default:
      return state;
  }
};

const insightsReducer = (state = initialState.insights, action) => {
  switch (action.type) {
    case SET_INSIGHTS:
      return action.insights;
    default:
      return state;
  }
};

const errorReducer = (state = initialState.error, action) => {
  switch (action.type) {
    case SET_ERROR:
      return action.error;
    default:
      return state;
  }
};

const rootReducer = combineReducers({
  user: userReducer,
  token: tokenReducer,
  conversations: conversationsReducer,
  insights: insightsReducer,
  error: errorReducer,
});

export default rootReducer;
