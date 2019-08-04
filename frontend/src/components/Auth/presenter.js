import React from 'react';
import styles from "./styles.module.scss";
import { LoginForm, SignupForm } from 'components/AuthForms'

const Auth = (props, context) => (
    <main className={styles.auth}>
        <div className={styles.column}>
            <img src={require("images/phone.png")} alt="Checkout our app. Is cool" />
        </div>
        <div className={styles.column}>
            <div className={`${styles.whiteBox} ${styles.formBox}`}>
                {props.action === "login" && <LoginForm />}
                {props.action === "signup" && <SignupForm />}
            </div>
            <div className={styles.whiteBox}>
                {props.action === "login" && (
                    <p className={styles.text}>
                        Don't have an account?{" "}
                        <span className={styles.changeLink} onClick={props.changeAction}>
                            Sign up
                        </span>
                    </p>
                )}
                {props.action === "signup" &&(
                    <p className={styles.text}>
                        Have an account?{" "}
                        <span className={styles.changeLink} onClick={props.changeAction}>
                            Log in
                        </span>
                    </p>
                )}
            </div>
            <div className={styles.appBox}>
                <span>Get the app</span>
                <div className={styles.appStores}>
                    <img src={require("images/ios.png")} alt="Donload it on Apple Appstore"/>
                    <img src={require("images/android.png")} alt="Donload it on Apple Appstore"/>
                </div>
            </div>
        </div>
    </main>
);

export default Auth;