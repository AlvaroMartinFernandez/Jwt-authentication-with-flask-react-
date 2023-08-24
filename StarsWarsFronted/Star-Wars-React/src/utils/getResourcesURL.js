import connectToAPIProtect from "./connectToAPIProtect.js";

const getResourcesUrl = async (resource) => {
    const list = await connectToAPIProtect(`${import.meta.env.VITE_BACKEND_URL}/${resource}/`);
    return list;
};

export default getResourcesUrl;