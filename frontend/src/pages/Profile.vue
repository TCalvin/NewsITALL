<template>
    <div class="row">
       <div v-if="email == ''">
        <h1>You need to log in.</h1>
      </div>
      <div v-if="email != ''" class="col-xl-4 col-lg-5 col-md-6">
        <Interests v-bind:email="email"/>
      </div>
      <div v-if="email != ''" class="col-xl-8 col-lg-7 col-md-6">
        <personal v-bind:email="email"/>
        <liked-posts v-bind:email="email"/>
        <disliked-posts v-bind:email="email"/>
      </div>
    </div>
</template>
<script>
import Personal from "./UserProfile/Personal.vue"
import UserCard from "./UserProfile/UserCard.vue"
import LikedPosts from "./UserProfile/LikedPosts.vue"
import DislikedPosts from "./UserProfile/DislikedPosts.vue"
import Interests from "./UserProfile/Interests.vue"

export default {
  components: {
    Personal,
    UserCard,
    LikedPosts,
    DislikedPosts,
    Interests
  },
  props: ['email'],
  mounted(){
    this.$emit('interface')
  }
};
</script>
<style>
</style>
