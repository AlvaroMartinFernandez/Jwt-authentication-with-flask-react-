import {useState, useEffect} from "react";
import getResources from "../utils/getResources";

const useResources = (targetResource) => {
    const [resources, setResources] = useState([]);
    useEffect(() => {
        const fetchData = async () => {
            const fetchedResources = await getResources(targetResource);
            setResources(fetchedResources);
        }
        fetchData();
    }, []);
    
    return resources;
}

export default useResources;