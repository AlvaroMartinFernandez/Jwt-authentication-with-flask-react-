import getResourcesUrl from "./getResourcesURL.js"

const getResources = async (resource) => {
    const resources = await getResourcesUrl(resource);
    console.log(resources)
    const parsedResources = resources.map(res => {
        const id = res.id;
        const properties = res;
        properties.favorites = false;
        const type = resource === "people" ? "characters" : resource;
        const name = properties.name || properties.model;
        return  {id, ...properties, type, name};
    });
return parsedResources;
}

export default getResources;


