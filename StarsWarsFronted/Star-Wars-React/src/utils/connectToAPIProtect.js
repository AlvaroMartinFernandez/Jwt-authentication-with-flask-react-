const connectToAPIProtect = (url) => {
    const token= sessionStorage.getItem("token");
    return (
        fetch(url, {
            headers: {"Authorization": "Bearer " + token}
        })
            .then((res) => {
                if (!res.ok) {
                    throw Error();
                }
                return res.json();
            })
            .then(data => data)
            .catch(err => console.log(err))
    )
}

export default connectToAPIProtect; 