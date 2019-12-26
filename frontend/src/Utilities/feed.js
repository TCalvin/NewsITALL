import axios from 'axios' 
 
export async function getAllPosts(){
        
        var articles = []

       //Get all posts
       await axios.post('http://localhost:5000/getallposts')
       .then(response => {

         //Store articles on the frontend
         articles = response.data.result
       })
       .catch(error => {
         console.log(error)
       })

       return articles
}
     
    
    
export async function getUserPosts(email){

    var articles = []

    //Get all posts for a specific user
    await axios.post('http://localhost:5000/getuserposts', {'email': email})
    .then(response => {

        //Store articles on the frontend
        articles = response.data.result
        
    })
    .catch(error => {
        console.log(error)
    })

    return articles
}  