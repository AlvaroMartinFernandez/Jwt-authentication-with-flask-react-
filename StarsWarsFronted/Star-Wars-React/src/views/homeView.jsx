import Section from "../components/Section.jsx";
import useAppContext from "../context/AppContext.jsx";
import Card from "../components/Card.jsx";
function Home () { 
    const {store: {people, vehicles, planets,loggedIn}} = useAppContext();
    const token=sessionStorage.getItem("token");
    console.log(token)
    console.log(loggedIn)
    if(loggedIn === false &&  token === null )
    {
        window.location.href = "/login"
    }
   else{
    
    return(
        <div>
            <Section  title="Characters">{people.map((person, index) => {return (<Card name={person.name} type={person.type} id={person.id} key={index}><p><strong>Height: </strong>{person.height}</p><p><strong>Mass: </strong>{person.mass}</p><p><strong>Hair Color: </strong>{person.hair_color}</p></Card>)})}</Section>
            <Section  title="Vehicles">{vehicles.map((vehicle, index) => {return (<Card name={vehicle.name} type={vehicle.type} id={vehicle.id} key={index}><p><strong>Model: </strong>{vehicle.model}</p><p><strong>Vehicle Class: </strong>{vehicle.vehicle_class}</p><p><strong>Manufacturer: </strong>{vehicle.manufacturer}</p></Card>)})}</Section>
            <Section  title="Planets">{planets.map((planet, index) => {return (<Card name={planet.name} type={planet.type} id={planet.id} key={index}><p><strong>Diamater: </strong>{planet.diamater}</p><p><strong>Rotation Period: </strong>{planet.rotation_period}</p><p><strong>Orbital Period: </strong>{planet.orbital_period}</p></Card>)})}</Section>
        </div>
    )
}
}

export default Home;