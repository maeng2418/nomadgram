// 나의 스토어를 설정/구성 (여러 리듀서를 한번에 모아서 관리)
import { createStore, combineReducers, applyMiddleware } from 'redux';
import users from 'redux/modules/users';
import thunk from "redux-thunk";
import { routerMiddleware, connectRouter } from "connected-react-router";
import { createBrowserHistory } from "history";
import Reactotron from 'ReactotronConfig';

const env = process.env.NODE_ENV;

const history = createBrowserHistory();

const middlewares = [thunk, routerMiddleware(history)];

if (env === "development"){
    const { logger } = require("redux-logger"); // for only dev not product
    middlewares.push(logger);
}

const reducer = combineReducers({
    users,
    router: connectRouter(history)
});

let store;

if(env === 'development') {
    store = initialState => 
        Reactotron.createStore(reducer, applyMiddleware(...middlewares));
} else {
    store = initialState => 
        createStore(reducer, applyMiddleware(...middlewares)); // ...middlewares -> thunk, dsle, dlwek  배열이 unpack됨.
}


export { history };

export default store();