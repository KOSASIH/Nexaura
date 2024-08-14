import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import { composeWithDevTools } from 'redux-devtools-extension';
import rootReducer from '../reducers';
import apiMiddleware from '../middleware/api';

const initialState = {};

const middleware = [thunk, apiMiddleware];

const store = createStore(
  combineReducers({ rootReducer }),
  initialState,
  composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
