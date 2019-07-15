// 나의 스토어를 설정/구성 (여러 리듀서를 한번에 모아서 관리)
import { createStore, combineReducers, applyMiddleware } from 'redux';
import users from 'redux/modules/users';
import thunk from "redux-thunk";

const middlewares = [thunk];

const reducer = combineReducers({
    users
});

let store = initialState => createStore(reducer, applyMiddleware(...middlewares));  // ...middlewares -> thunk, dsle, dlwek  배열이 unpack됨.

export default store();