// import

// actions

// action createors

// initial state

const initialState = {
    isLoggedIn: localStorage.getItem("jwt") || false
};

// reducer

function reducer(state = initialState, action){
    switch(action.type) {
        default:
            return state;
    }
}
// reducer fuctions

// exports

// reducer export

export default reducer;