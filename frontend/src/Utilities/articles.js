
import axios from 'axios'

export async function addDislike(email, article){

    var post = {'email': email, 'rsslink': '', 'title': article.title, 'summary': article.summary, 'post_id': article.post_id, 'URL': article.URL} //Post to be disliked
        
    //Send post to backend to be stored
    await axios.post('http://127.0.0.1:5000/adddislikedpost', post)
    .catch(error => {
        console.log(error)
    })
    return
}

export async function removeDislike(email, article){
    var post = {'email': email, 'post_id': article.post_id} //Post to be un-disliked

        //Send post to backend to be removed from dislikes
        await axios.post('http://127.0.0.1:5000/removedislikedpost', post)
        .then(response => {
          console.log('Undisliked ' + article.title)
        })
        .catch(error => {
          console.log(error)
        })
}

export async function addLike(email, article){
    var post = {'email': email, 'rsslink': '', 'title': article.title, 'summary': article.summary, 'post_id': article.post_id, 'URL': article.URL} //Post that was liked
        
        //Send post to backend to be stored
        await axios.post('http://127.0.0.1:5000/addlikedpost', post)

        //A repsonse was received
        .then(response => {
          console.log('Liked ' + article.title)
        })

        //An error occurred
        .catch(error => {
          console.log(error)
        })
}


export async function deleteLike(email, article){
    var post = {'email': email, 'post_id': article.post_id} //Post that was unliked

    //Send psot to backend to be removed from likes
    await axios.post('http://127.0.0.1:5000/removelikedpost', post)
    .then(response => {
    console.log('Unliked ' + article.title)
    })
    .catch(error => {
    console.log(error)
    })
}
