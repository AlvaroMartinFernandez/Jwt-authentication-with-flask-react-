import { Link } from "react-router-dom"
import useAppContext from '../context/AppContext'


const ButtonLogin = () => {
    const { store, actions } = useAppContext();
    

    return (
        <>
            {store.loggedIn ? <button type="button" onClick={actions.logOut} className="btn btn-primary">Logout</button> :
                <Link to={"/login"}><button type="button" className="btn btn-primary">Login</button></Link>}
        </>
    )
}

export default ButtonLogin;