import axios from 'axios'

export async function search(search){
    var articles = []
    //Sends search term to backend
    await axios.post('http://localhost:5000/searchterm', {'term': search})

    //Matching articles are returned and updated on frontend
    .then(response => {
        articles = response.data.result
    })
    .catch(err => {
        console.log(err)
    })

    return articles
}

export async function userSearch(search, email){
    var articles = []
    //Sends search term to backend
    await axios.post('http://localhost:5000/usersearchterm', {'email': email, 'term': search})

    //Matching articles are returned and updated on frontend
    .then(response => {
        articles = response.data.result
    })
    .catch(err => {
        console.log(err)
    })

    return articles
}

