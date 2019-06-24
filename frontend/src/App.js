import React from 'react';
import {ReactComponent as Logo} from './logo.svg';
import styles from './App.module.scss';
//restart
function App() {
  return (
    <div className={styles.app}>
      <header className={styles.appHeader}>
        <Logo/>
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
