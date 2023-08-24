
const Authentication = async (email, password) => {
    return (
        await fetch(`${import.meta.env.VITE_BACKEND_URL}/users/login`, { method: "POST", headers: { "Content-Type": "application/json" }, 
        body: JSON.stringify({ email: email, password: password })})
        .then((res) => {
            if (!res.ok) {
                return false;
            }
            return res.json();
        })
        .then(data => {
            if (data.token === undefined) {
                return false;
            }
            else {
            sessionStorage.setItem("token", data.token)
        }})
        .catch(err => console.log(err))
    );
};


export default Authentication;