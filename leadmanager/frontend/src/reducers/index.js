import { combineReducers } from 'redux';
// This function is used to combine multiple reducers
// into a single reducer.
import leads from './leads';
import errors from './errors';
import messages from './messages';
import auth from './auth'

export default combineReducers({
    leads,
    errors,
    messages,
    auth
});