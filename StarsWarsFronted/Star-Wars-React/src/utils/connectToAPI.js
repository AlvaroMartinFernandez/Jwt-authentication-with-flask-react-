const connectToAPI = (url) => {
    return (
        fetch(url)
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

export default connectToAPI; 