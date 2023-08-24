const getData = async (url) => {
    try {
        const response = await fetch(`https://www.swapi.tech/api/${url}`, {
            method: "GET",
        });
        const res = await response.json();
        const data = await Promise.all(res.result.map((element) => {
            fetch(element.url)
            .then(res => res.json())
            .then((res) => (res))
            .catch((error) => {console.log(error)});
        return data;
    }))
    
    } catch (error) {
        return;
    }
};

export default getData;
