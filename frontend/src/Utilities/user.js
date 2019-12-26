import axios from 'axios'

export async function getUserInfo(email){
    var user = {}

    await axios.get('http://localhost:5000/getuser', {params: {"email": email}})
    .then(response => {
        user = response.data.result
    })
    .catch(error => {
        console.log(error)
    })

    return user
}

export async function updateUserInfo(email, new_email, password, phone){
    var user = {}

    await axios.get('http://localhost:5000/updateuser', {
        params: {
            "email": email, "newEmail": new_email, "password": password, "phone": phone
        }
    })
    .then(response => {
        user = response.data.result
    })
    .catch(error => {
        console.log(error)
    })

    return user
}