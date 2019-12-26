<template>
  <card class="card" :title="title">
    <div>
      <ul class="list-unstyled team-members">
          <div v-bind:key="index" v-for="(post, index) in posts">
            <li>
              <LikedArticle v-bind:email="email" @interface="getLikedPosts" v-bind:post="post"/>
            </li>
          </div>
      </ul>
    </div>
  </card>
</template>
<script>

import LikedArticle from '@/components/Articles/LikedArticle.vue'
import {getUserLikes} from '@/Utilities/profilePosts.js'

export default {
  name: "LikedPosts",
  components:{
    LikedArticle // A Liked Article
  },
  props: ['email'],

  data() {
    return {
      title: "Liked Posts",
      posts: [] // liked posts
    }
  },
  methods: {

    /**
     * Gets liked posts from the backend 
     */
    async getLikedPosts(){

      //Get posts based on a specific user
      getUserLikes(this.email).then(response => {
        this.posts = response
      })
    }
  },

  /**
   * Called when component is mounted
   */
  mounted(){
      this.getLikedPosts()
  }
};
</script>
<style>
</style>
