import { useState, createContext, useContext } from "react";

const AuthContext = createContext()

export const AuthProvider = ({children}) => {
    const [authnticated , setAuth] = useState(()=>{
        const token = localStorage.getItem('token')
        return token ? true : false
    })
    
    const login = (token) => {
        localStorage.setItem('token', token)
        setAuth(true)
    }

    const logout = () => {
        setAuth(false)
        localStorage.removeItem('token')
    }

    return(
        <AuthContext.Provider value={{authnticated, login, logout}}>
            {children}
        </AuthContext.Provider>
    )
}

export const useAuth = () => {
    return useContext(AuthContext)
}