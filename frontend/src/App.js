import React from 'react';
import logo from './logo.svg';
// import { ReactComponent as Logo } from "./logo.svg";
import styles from './App.module.scss';

function App() {
  return (
    <div className={styles.App}>
      <header className={styles.appHeader}>
        <img src={logo} className={styles.appLogo} alt="logo" />
        {/*<Logo/>*/}
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className={styles.appLink}
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
