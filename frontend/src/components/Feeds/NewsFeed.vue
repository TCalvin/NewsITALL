<template>
  <div class="row">

    <div v-if="view == 'list'">

      <!-- Articles -->
      <div class="row" v-bind:key="article.id" v-for="article in articles">
          <Article v-bind:view="view" v-bind:email="email" v-bind:article="article"/>
      </div>
    </div>
    <div class="row" v-if="view == 'tile'">
        <div class="col-md-6 col-xl-4" v-bind:key="article.id" v-for="article in articles">
          <TileArticle v-bind:view="view" v-bind:email="email" v-bind:article="article"/>
        </div>
    </div>
  </div>
</template>

<script>

import Article from '@/components/Articles/Article.vue';
import TileArticle from '@/components/Articles/TileArticle.vue'

export default {
  name: 'NewsFeed',
  components: {
      Article,
      TileArticle
  },
  props:  ["articles", "email", "view"], //Props
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
