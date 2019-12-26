import axios from 'axios'

export async function validate(){
    var token = decodeCookie()
    var email = ''
    await axios({method: 'get', url: 'http://localhost:5000/validate', headers: {'Authorization': 'Bearer ' + token}})
    .then(response =>{
      email = response.data.email
    }).catch((error) => {
      email = ''
      console.log(error)
    })

    return email
}

function decodeCookie(){
    var cookie = document.cookie.split(';')
    return cookie[0].substr(5, cookie[0].length)
}