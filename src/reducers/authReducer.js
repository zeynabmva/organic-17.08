// authReducer.js

const initialState = {
    isAuthenticate: false, // İstifadəçi giriş etmədiyi üçün başlangıçda false olacaq
    // digər reducer-lar...
  };
  
  const authReducer = (state = initialState, action) => {
    switch (action.type) {
      case "LOGIN":
        return {
          ...state,
          isAuthenticate: true,
        };
      case "LOGOUT":
        return {
          ...state,
          isAuthenticate: false,
        };
      // digər reducer-lar üçün case-lər...
      default:
        return state;
    }
  };
  
  export default authReducer;
  


  