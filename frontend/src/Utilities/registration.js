import axios from 'axios'

export async function register(email, password){
     var result = {}

    //Store user information on the backend
    await axios.get('http://localhost:5000/register', {
        params: {
        "email": email,
        "password": password
        }
    }).then(response =>{
        result = {"message" : JSON.stringify(response.data.msg), "success": true}
    }).catch(error => {
        result = {"message": "error: " + error, "success": false}
    })

    return result
}

