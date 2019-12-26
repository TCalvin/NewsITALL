<template>
   <card class="card" :title="title">
    <div>
      <ul class="list-unstyled team-members">
          <div v-bind:key="index" v-for="(post, index) in posts">
            <li>
              <DislikedArticle v-bind:email="email" @interface="getDislikedPosts" v-bind:post="post"/>
            </li>
          </div>
      </ul>
    </div>
  </card>
</template>

<script>

import DislikedArticle from '@/components/Articles/DislikedArticle.vue'
import {getUserDislikes} from '@/Utilities/profilePosts.js'

export default {
  name: 'DislikedPosts',
  components:{
      DislikedArticle
  },
  props: ['email'],
  data(){
    return{
      title: "Disliked Posts",
      posts: [] //Disliked posts to be displayed
    }
  },
  mounted(){
      this.getDislikedPosts() //Retrieve users disliked posts from the backend
  },
  methods: {

    /**
     * Called when component mounts and child component changes dislikes
     */
    async getDislikedPosts(){

      getUserDislikes(this.email)
      .then(response => {
        this.posts = response
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
