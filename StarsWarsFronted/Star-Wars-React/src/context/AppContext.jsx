import { createContext, useContext, useState } from "react";
import useResources from "../hooks/useResources.js"
import { useEffect } from "react";
const AppContext = createContext();

export const AppProvider = ({ children }) => {
    const people = useResources("people");
    const vehicles = useResources("vehicles");
    const planets = useResources("planets");
    const [favorites, setFavorties] = useState([]); 
    const[loggedIn, setLoggedIn] = useState(false);
useEffect(()=>{
    if (sessionStorage.getItem("token")){
        setLoggedIn(true);
    }},[])
    const logOut = () => {
        sessionStorage.removeItem("token");
        setLoggedIn(false);
    }
    const logIN=()=>{
        
        if(sessionStorage.getItem("token")){
            setLoggedIn(true);
        }
    }

    const addFavorites = ( id, type, name) => {
        console.log(favorites);
        setFavorties((prev) => {
            const newFavorite = {
                id,
                type,
                name
            }
            const filter = prev.filter(e=>e.id === id) 
            if (filter.length > 0){
                console.log("hola");
                return prev.filter(e=>e.id != id)
            }
            return ([...prev, newFavorite])
        }
        )
    }
    const store = {
        people, vehicles, planets, favorites, loggedIn
    }

    const actions = {
        addFavorites,
        setLoggedIn,
        logOut,
        logIN
    }

    return (<AppContext.Provider value={{store, actions}}>
        {children}
    </AppContext.Provider>)
}

const useAppContext = () => useContext(AppContext);

export default useAppContext;