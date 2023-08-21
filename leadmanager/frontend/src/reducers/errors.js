import { GET_ERRORS } from "../actions/types";

const initialState = {
    msg: {},
    status: null
}

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_ERRORS:
            return {
                msg: action.payload.msg,
                status: action.payload.status
            };
        default:
            return state;
    }
}

// In Redux, a reducer is a pure JavaScript function responsible for specifying
// how the application's state changes in response to actions dispatched to the
// Redux store. It defines how the state transitions from one state to another
// based on the actions it receives.

// Reducers are a crucial part of the Redux architecture and play a central
// role in maintaining the predictability and immutability of the state.

// Reducers take the current state and an action as input, and they return a
// new state that reflects the changes brought about by the action. 

// It's important to note that reducers are pure functions, which means they
// should not have side effects or modify the state directly.