import axios from "axios";
import { returnErrors } from "./messages";
import { USER_LOADED,USER_LOADING, AUTH_ERROR, LOGIN_SUCCESS, LOGIN_FAIL, LOGOUT_SUCCESS, REGISTER_SUCCESS, REGISTER_FAIL } from "./types";

// CHECK TOKEN AN LOAD USER 

// This action loads the user's data based on the token. It dispatches USER_LOADING action
// to show loading state. It gets the token from the state, creates headers with the token,
// and sends a GET request to retrieve user data. It dispatches USER_LOADED with data on success
// or AUTH_ERROR on failure.

export const loadUser = () => (dispatch, getState) => {
    // User Loading
    dispatch({ type: USER_LOADING });

    axios.get('api/auth/user', tokenConfig(getState))
        .then(res => {
            dispatch({
                type: USER_LOADED,
                payload: res.data
            });
        }).catch(err => {
            dispatch(returnErrors(err.response.data, err.response.status));
            dispatch({
                type: AUTH_ERROR
            })
        });
};

// LOGIN USER

// This action logs in the user by sending a POST request with username and password.
// It dispatches LOGIN_SUCCESS on successful login or LOGIN_FAIL on failure. If there's
// an error, it dispatches error details using returnErrors.

export const login = (username, password) => dispatch => {
    //Headers -> config object that contains headers required for the HTTP request.
    const config = {
        headers: {
            'content-type': 'application/json'
        }
    };

    // Request body -> body object by stringifying an object with username and password.
    const body = JSON.stringify({ username, password })

    axios
        .post('api/auth/login', body, config)
        .then(res => {
            // If the request is successful, you dispatch an action with the type LOGIN_SUCCESS
            // and the response data (res.data) as the payload. This action will be handled by
            // the appropriate reducer to update the state.
            dispatch({
                type: LOGIN_SUCCESS,
                payload: res.data
            });
            // If there's an error in the request, the catch block is executed. Within it, you dispatch
            // returnErrors with the error response data and status. Then, you dispatch an action of
            // type LOGIN_FAIL.
        }).catch(err => {
            dispatch(returnErrors(err.response.data, err.response.status));
            dispatch({
                type: LOGIN_FAIL
            })
        });
};

// REGISTER USER
export const register = ({ username, password, email }) => dispatch => {
    //Headers -> config object that contains headers required for the HTTP request.
    const config = {
        headers: {
            'content-type': 'application/json'
        }
    };

    // Request body -> body object by stringifying an object with username and password.
    const body = JSON.stringify({ username, email, password })

    axios
        .post('api/auth/register', body, config)
        .then(res => {
            // If the request is successful, you dispatch an action with the type REGISTER_SUCCESS
            // and the response data (res.data) as the payload. This action will be handled by
            // the appropriate reducer to update the state.
            dispatch({
                type: REGISTER_SUCCESS,
                payload: res.data
            });
            // If there's an error in the request, the catch block is executed. Within it, you dispatch
            // returnErrors with the error response data and status. Then, you dispatch an action of
            // type REGISTER_FAIL.
        }).catch(err => {
            dispatch(returnErrors(err.response.data, err.response.status));
            dispatch({
                type: REGISTER_FAIL
            })
        });
};


// LOGOUT USER

// This action logs out the user by sending a GET request with the token in headers.
// It dispatches LOGOUT_SUCCESS on success and handles errors with returnErrors.

export const logout = () => (dispatch, getState) => {
    axios
        .post('api/auth/logout',null , tokenConfig(getState))
        .then(res => {
            dispatch({
                type: LOGOUT_SUCCESS,
            });
        }).catch(err => {
            dispatch(returnErrors(err.response.data, err.response.status));
        });
};

// setup the config with the token --> helper function
export const tokenConfig = (getState) => {
    // Get Token from state
    const token = getState().auth.token;

    //Headers
    const config = {
        headers: {
            'content-type': 'application/json'
        }
    };

    // if token, add to headers config
    if (token) {
        config.headers['Authorization'] = `Token ${token}`;
    };

    return config
}