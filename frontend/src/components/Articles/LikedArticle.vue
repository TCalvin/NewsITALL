<template>
    <div class="row">
      <div class="col-9">
        <a v-bind:href="post.URL" target="_blank">{{post.title}}</a>
        <br>
      </div>

      <div class="col-3">
        <b-button @click="$bvModal.show(post.title)" type="danger" outline icon>
         <font-awesome-icon :icon="['fas', 'ban']"/>
        </b-button>
      </div>

      <!-- Remove -->
      <b-modal v-bind:id='post.title' title="Remove" hide-footer>
          <p>Are you sure you want to remove "<b>{{post.title}}</b>" from your liked posts?</p>
          <b-button block @click="removePost(post.title)" variant='danger'>Remove</b-button>
      </b-modal>
    </div>
</template>

<script>

import axios from 'axios'
import {deleteLike} from '@/Utilities/articles.js'

export default {
  name: 'LikedArticle',
  props: ['post', 'email'],
  data(){
    return{
    }
  },
  methods: {

    /**
     * Called when a liked post is removed
     */
    removePost(title){

      deleteLike(this.email, this.post)
      .then(response => {
        this.$bvModal.hide(title)
        this.$emit('interface')
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
