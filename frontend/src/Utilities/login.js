import axios from 'axios'
import bcrypt from 'bcryptjs'

export async function login(email, password){

    //make encrypted passcode
    var pw = bcrypt.hashSync(password, 0)
    var result = {}
    await axios.get('http://localhost:5000/login', { params:{ "email": email, "password": pw}})
    .then(response =>{

        //if it worked, create cookie
        if(response.data.status == 0){
            createCookie(response.data.token)
            result = {"message" : JSON.stringify(response.data.msg), "success": true}
        }else{
            result = {"message" : JSON.stringify(response.data.msg), "success": false}
        }
    }).catch(error => {
        result = {"message" : JSON.stringify(error), "success": false}
    })
    return result
}

//creates cookie with token
function createCookie(token){
    var date = new Date()
    date.setTime(date.getTime() + 24 * 60 * 60 * 1000)
    document.cookie = "VDFU=" + token + ";expires=" + date.toUTCString() + ";path=/;"
}