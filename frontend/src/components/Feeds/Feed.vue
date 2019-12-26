<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-8 feed-title">
        <h1 v-if="email == ''">Latest News</h1>
        <h1 v-if="email != ''">Your News</h1>
      </div>
      <div class="col-sm-4 show-buttons">
        <div>
          <b-button @click='onListClick'>
            <font-awesome-icon :icon="['fas', 'list']"/>
          </b-button>
          <b-button @click='onTileClick'>
            <font-awesome-icon :icon="['fas', 'th']"/>
          </b-button>
        </div>
      </div>
    </div>

    <!-- List of articles -->
    <NewsFeed @interface="validate" v-bind:view="view" v-bind:email="email" v-bind:articles="articles"/>
  </div>
</template>

<script>

import {getAllPosts, getUserPosts} from '@/Utilities/feed.js'
import NewsFeed from './NewsFeed.vue'

export default {
  name: 'Feed',
  props: ['email'],
  components: {
    NewsFeed //A users new feed
  },
  data(){ 
    return {
      articles: [], //Articles for a users feed,
      view: 'tile'
    }
  },
  mounted () {

    //validate user
    this.validate()
    this.getPosts()

  },
  methods: {


    validate(){
      this.$emit('interface')
    },
    /**
     * Called when page is loaded
     */
    getPosts(){

      /**
       * No user is logged in
       */
      console.log(this.email)
      if(this.email == ''){

        getAllPosts()
        .then(response => {
          this.articles = response
        })
      }
      else{
       console.log("User specific posts")
       getUserPosts(this.email)
       .then(response => {
         this.articles = response
       })
      }
    },

    onListClick(){
      this.view="list"
    },
    onTileClick(){
      this.view="tile"
    }


  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.show-buttons {
  display: flex;
  align-items: center;
  justify-content: right;
}
.feed-title{
  display: flex;
  align-items: center;
  justify-content: left;
}
</style>
