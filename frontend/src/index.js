import React from 'react';
import ReactDOM from 'react-dom';
import 'index.css';
import App from 'App';
import { Provider } from 'react-redux';
import store, { history } from "redux/configureStore";
import { ConnectedRouter } from 'react-router-redux';

console.log(store.getState());

ReactDOM.render(
    <Provider store={store}>
        <ConnectedRouter history={history}>
            <App />
        </ConnectedRouter>
    </Provider>,
 document.getElementById('root')
);