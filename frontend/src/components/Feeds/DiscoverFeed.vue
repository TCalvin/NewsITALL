<template>
  <div>
    <div>

      <!-- Search components -->
      <b-input-group class="mt-3">

        <!-- Search bar -->
        <b-form-input v-model="search"></b-form-input>

        <!-- Search button -->
        <b-button @click="searchData" variant="success">Search</b-button>

      </b-input-group>
    </div>

    <div class="row">
      <div class="col-sm-8 feed-title">
        <h1>Search Results</h1>
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

    <NewsFeed v-bind:view="view" v-if="articles.length != 0" v-bind:email="email" v-bind:articles="articles"/>
    <h2 align="center" v-if="articles.length == 0">No Results</h2>
  </div>
</template>

<script>

import NewsFeed from './NewsFeed.vue'
import {search, userSearch} from '@/Utilities/search.js'

export default {
  name: 'DiscoverFeed',
  components: {
    NewsFeed, //Will be the search results in this case 
  },
  props: ['email'],
  data(){ 
    return {
      search: '', //The search term
      articles: [], //Resulting articles from a search
      view: 'tile'
    }
  },

  /**
   * Called when component has mounted
   */
  mounted () {
    
  },
  methods: {




    /**
     * Called when search is submitted
     */
    searchData(){

      /**
       * No user is logged in
       */
      if(this.email == ''){

        search(this.search)
        .then(response => {
          this.articles = response
        })
      }
      else{

       userSearch(this.search, this.email)
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
div{
  margin-top: 20px;
}
</style>
