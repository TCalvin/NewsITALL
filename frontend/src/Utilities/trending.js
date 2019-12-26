import axios from 'axios'

export async function getTrending(){
    var trending = []
    //Get posts based on a specific user
    await axios.post('http://127.0.0.1:5000/gettrending')
    .then(response => {
        //Store disliked posts for use on the frontend
        trending = response.data.result 
    })
    .catch(error => {
      console.log(error)
    })
    return trending
}

export async function getUserTrending(email){
    var trending = []
    //Get posts based on a specific user
    await axios.post('http://127.0.0.1:5000/getusertrending', {'email': email})
    .then(response => {
        //Store disliked posts for use on the frontend
        trending = response.data.result 
    })
    .catch(error => {
      console.log(error)
    })
    return trending
}