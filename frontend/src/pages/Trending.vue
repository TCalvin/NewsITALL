<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-8 feed-title">
        <h1>Trending News</h1>
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
    <NewsFeed v-bind:view="view" v-bind:email="email" v-bind:articles="articles"/>
  </div>
</template>
<script>


import NewsFeed from '@/components/Feeds/NewsFeed.vue'
import {getTrending, getUserTrending} from '@/Utilities/trending.js'

export default {
  components: {
    NewsFeed
  },
  props: ['email'],
  data(){
    return{
      articles: [],
      view: 'tile'
    }
  },
  mounted(){
    this.$emit('interface')
    this.getTrending()
  },
  methods: {

    /**
     * Called when page is loaded
     */
    getTrending(){

      /**
       * No user is logged in
       */
      if(this.email == ''){

        getTrending()
        .then(response => {
          this.articles = response
        })
      }
      else{

       getUserTrending(this.email)
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
