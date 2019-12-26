import axios from 'axios'


export async function getUserLikes(email){
    var posts = []

    //Get posts based on a specific user
    await axios.post('http://127.0.0.1:5000/getlikedposts', {'email': email})
    .then(response => {

        //Store posts for use on the frontend
        posts = response.data.result
        console.log('Liked Posts Retreived')
    })
    .catch(error => {
        console.log(error)
    })
    return posts
}


export async function getUserDislikes(email){
    var posts = []

    //Get posts based on a specific user
    await axios.post('http://127.0.0.1:5000/getdislikedposts', {'email': email})
    .then(response => {
        //Store disliked posts for use on the frontend
        posts = response.data.result
        console.log('Disliked Posts Retreived')
    })
    .catch(error => {
      console.log(error)
    })
    return posts
}

export async function addTags(email, tags){
    var message
    //Get posts based on a specific user
    await axios.post('http://127.0.0.1:5000/addTag', {'email': email, 'tags': tags})
    .then(response => {
        //Store disliked posts for use on the frontend
        message = response.data.result
    })
    .catch(error => {
      console.log(error)
    })
    return message
}

export async function getTags(email){
    var tags = []
    //Get posts based on a specific user
    await axios.post('http://127.0.0.1:5000/getTags', {'email': email})
    .then(response => {
        //Store disliked posts for use on the frontend
        tags = response.data.result 
    })
    .catch(error => {
      console.log(error)
    })
    return tags
}

export async function removeTags(email, tags){
    var message
    //Get posts based on a specific user
    await axios.post('http://127.0.0.1:5000/removeTag', {'email': email, 'tags': tags})
    .then(response => {
        //Store disliked posts for use on the frontend
        message = response.data.result
    })
    .catch(error => {
      console.log(error)
    })
    return message
}