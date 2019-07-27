import React from 'react';
import ReactDOM from 'react-dom';
import 'index.css';
import App from 'App';
import { Provider } from 'react-redux';
import { ConnectedRouter } from "connected-react-router";
import store, { history } from "redux/configureStore";
//import 'ReactotronConfig';

//console.log(store.getState());
//store.dispatch({type: "BULLSHIT"});

ReactDOM.render(
    <Provider store={store}>
        <ConnectedRouter history={history}>
            <App />
        </ConnectedRouter>
    </Provider>,
 document.getElementById('root')
);