import React from 'react';
import App from './presenter';

const Container = props => <App {...props} />; // state가 없으므로 클래스 컴포넌트로 작성하지 않음.

export default Container;