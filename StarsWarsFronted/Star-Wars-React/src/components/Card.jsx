import { Link } from "react-router-dom";
import useAppContext from "../context/AppContext";
import { AiOutlineHeart } from 'react-icons/ai';
import {AiFillHeart} from "react-icons/ai";
import styles from "./Card.module.css";


const Card = ({name, children, type, id, favorites }) => {
    const { actions, store } = useAppContext();
    return (
        <div className="card" style={{ minWidth: "18rem" }}>
            <img style={{ maxWidth: "30rem"}} src={`https://starwars-visualguide.com/assets/img/${type}/${id}.jpg`} className="card-img-top img-fluid" alt="..." />
            <div className="card-body">
                <h5 className="card-title">{name}</h5>
                {children}
                <div className="d-flex justify-content-between">
                    <Link to={`/detail/${type}/${id}`} className="btn btn-primary">
                        Learn more!
                    </Link>
                    {store.favorites.find((favorite) => favorite.id === id)?<AiFillHeart className= {styles.heartIcon} onClick={()=>actions.addFavorites(id, type, name)}/>
                            :<AiOutlineHeart className= {styles.heartIcon} onClick={()=>actions.addFavorites(id, type, name)}/>}
                </div>
            </div>
        </div>
    );
};

export default Card;
