// 나의 스토어를 설정/구성 (여러 리듀서를 한번에 모아서 관리)
import { createStore, combineReducers } from 'redux';
import users from 'redux/modules/users';

const reducer = combineReducers({
    users
});

let store = initialState => createStore(reducer);

export default store();