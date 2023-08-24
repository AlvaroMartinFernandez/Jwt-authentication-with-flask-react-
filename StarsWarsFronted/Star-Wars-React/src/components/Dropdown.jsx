import React from "react";
import { Link } from "react-router-dom"
import useAppContext from "../context/AppContext";

const Dropdown = () => {
    const { store } = useAppContext();
    return (
        <div className="dropdown me-5">
            <button className="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Favorites 
            </button>
            <ul className="dropdown-menu dropdown-menu-end">
            {store.favorites.map((element, index) => {
                return (<li key={index} ><div className="dropdown-item p-2" >
                    <Link to={`http://localhost:5173/detail/${element.type}/${element.id}`}>{element.name}</Link></div></li>);
            })
            }</ul>
        </div>
    )
}

export default Dropdown;