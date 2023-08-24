import { useParams, useNavigate } from "react-router-dom";
import Card from "../components/Card.jsx";
import useAppContext from "../context/AppContext";

function Detail() {
    const params = useParams();
    const { store } = useAppContext();
    const navigate = useNavigate();
    const resource = (r) => {
        if (r.resource === "characters") { return store["people"] }
        return store[r.resource]
    }
    const resources = resource(params);
    const targetResource = resources.find(element => element.id === params.id);
    if(store.loggedIn === false){
         navigate("/login");
        }
    else{
    return (
        <div>
            <Card name={targetResource.name} type={targetResource.type} id={targetResource.id}>
                {targetResource.type === "characters" && (
                    <div>
                        <p><strong>Height: </strong>{targetResource.height}</p>
                        <p><strong>Mass: </strong>{targetResource.mass}</p>
                        <p><strong>Hair Color: </strong>{targetResource.hair_color}</p>
                        <p><strong>Skin Color: </strong>{targetResource.skin_color}</p>
                        <p><strong>Eye Color: </strong>{targetResource.eye_color}</p>
                        <p><strong>Birth year: </strong>{targetResource.birth_year}</p>
                        <p><strong>Gender: </strong>{targetResource.gender}</p>
                    </div>
                )}
                {targetResource.type === "vehicles" && (
                    <div>
                        <p><strong>Model: </strong>{targetResource.model}</p><p><strong>Vehicle Class: </strong>{targetResource.vehicle_class}</p>
                        <p><strong>Manufacturer: </strong>{targetResource.manufacturer}</p>
                        <p><strong>Cost in credits: </strong>{targetResource.cost_in_credits}</p>
                        <p><strong>Length: </strong>{targetResource.length}</p>
                        <p><strong>Crew: </strong>{targetResource.crew}</p>
                        <p><strong>Passengers: </strong>{targetResource.passengers}</p>
                        <p><strong>Speed: </strong>{targetResource.max_atmosphering_speed}</p>
                        <p><strong>Cargo Capacity: </strong>{targetResource.cargo_capacity}</p>
                    </div>
                )}
                {targetResource.type === "planets" && (
                    <div>
                        <p><strong>Diamater: </strong>{targetResource.diamater}</p>
                        <p><strong>Rotation Period: </strong>{targetResource.rotation_period}</p>
                        <p><strong>Orbital Period: </strong>{targetResource.orbital_period}</p>
                        <p><strong>Gravity: </strong>{targetResource.gravity}</p>
                        <p><strong>Population: </strong>{targetResource.population}</p>
                        <p><strong>Climate: </strong>{targetResource.climate}</p>
                        <p><strong>Terrain: </strong>{targetResource.terrain}</p>
                        <p><strong>Surface Water: </strong>{targetResource.surface_water}</p>
                    </div>
                )}
                </Card>
        </div>
    )
}
}
export default Detail;