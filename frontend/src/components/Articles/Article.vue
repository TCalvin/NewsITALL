<template>
  <div>
    <!--Stats cards-->
        <stats-card v-bind:view="view">
          <div v-if="article.video == ''"  align="left" :class="`icon-success`" slot="header">
             <img v-bind:src="article.img" height=100% width=75%/> 
          </div>
          <div v-if="article.video != ''"  align="left" :class="`icon-success`" slot="header">
             <iframe width=75% height=100% v-bind:src="article.video" frameborder="0" allowfullscreen/>
          </div>
          <div class="numbers" align="right" slot="content">
            <a v-bind:href="article.URL" target="_blank"><h4 v-bind:class="sentimentColor">{{article.title}}</h4></a>

            <p class="black" v-html="article.summary"/>
          </div>
          <div class="stats row" slot="footer">
            Interests:
            <div class="interest-padding" v-bind:key="index" v-for="(interest, index) in article.interests">
              <b-badge pill>{{interest}}</b-badge>
            </div>
            <div class="col" align="right">
              <b-button v-if="email != ''" v-bind:pressed='article.liked' @click='onLikeClick' variant="outline-success" pill>
                <font-awesome-icon :icon="['fas', 'heart']"/>
              </b-button>
              <b-button v-if="email != ''" v-bind:pressed='article.disliked' @click='onDislikeClick' variant="outline-danger" pill>
                <font-awesome-icon :icon="['fas', 'heart-broken']"/>
              </b-button>
              <b-button @click="$bvModal.show(article.title)" pill>
                <font-awesome-icon :icon="['fas', 'book-reader']"/>
              </b-button>

              <!-- Reader View Modal -->
              <b-modal v-bind:id='article.title' scrollable v-bind:title="article.title" hide-footer>
                {{article.text}} 
              </b-modal>
            </div>
          </div>
        </stats-card>
  </div>
</template>

<script>

import axios from 'axios'
import { StatsCard, ChartCard } from "@/components/index";
import Chartist from 'chartist';
import {addDislike, removeDislike, addLike, deleteLike} from '@/Utilities/articles.js'

export default {
  name: 'Article',
  components: {
    StatsCard,
    ChartCard
  },
  props: ['article', 'email', 'view'] /*The article to be displayed*/,
  data(){
    return{
      sentimentColor: ''
    }
  },
  mounted(){
    this.getSentimentColor()
  },
  methods: {

    /**
     * Called when the like button is pressed
     */
    onLikeClick(){

      //Executed when the article was not liked
      if(!this.article.liked){

        removeDislike(this.email, this.article)
        .then(response => {
          this.article.disliked = false
        })

        addLike(this.email, this.article)
        .then(response => {
          this.article.liked = true
        })

      //the article was previously liked
      }else{
        deleteLike(this.email, this.article)
        .then(response => {
          this.article.liked = false
        })
      }

      //Set article variables to update frontend
      this.article.disliked = false
    },

    /**
     * Called when the dislike button is pressed
     */
    onDislikeClick(){

      //Executed when article was not previously disliked
      if(!this.article.disliked){
        deleteLike(this.email, this.article)
        .then(response => {
          this.article.liked = false
        })

        addDislike(this.email, this.article)
        .then(response => {
          this.article.disliked = true
        })

      //Article was already disliked
      }else{
        removeDislike(this.email, this.article)
        .then(response => {
          this.article.disliked = false
        })
      }

      //Set article variables to update frontend
      this.article.liked = false
    },

    getSentimentColor(){
      if(this.article.sentiment_score == 0){
        this.sentimentColor = 'reallynegative'
      }else if(this.article.sentiment_score > 0 && this.article.sentiment_score < 3){
        this.sentimentColor = 'negative'
      }else if(this.article.sentiment_score > 2 && this.article.sentiment_score < 5){
        this.sentimentColor = 'barelynegative'
      }else if(this.article.sentiment_score > 4 && this.article.sentiment_score < 7){
        this.sentimentColor = 'barelypositive'
      }else if(this.article.sentiment_score > 6 && this.article.sentiment_score < 9){
        this.sentimentColor = 'positive'
      } else if (this.article.sentiment_score == 9){
        this.sentimentColor = 'reallypositive'
      }else{
        this.sentimentColor = ''
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.barelypositive{
  color: #7EF07E
}
.positive{
  color: #4BBD47
}
.reallypositive{
  color: #188A14
}
.barelynegative{
  color: #F0867A
}
.negative{
  color: #BD5347
}
.reallynegative{
  color: #8A2014
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
.black{
  color: black
}
.yellow{
  color: yellow
}
.interest-padding{
  padding-left: .5em
}
</style>
