
export const Signup = async (userName,email, password) => {
    return (
        await fetch(`${import.meta.env.VITE_BACKEND_URL}/users/`, {method: "POST", headers: {"Content-Type": "application/json"}, 
        body: JSON.stringify({name: userName, email: email, password: password})})
        .then((res) => {
            if (!res.ok) {
               return false;
            }
            return res.json();
        })
        .then(data => data)
        .catch(err => console.log(err)) 
    )
}

