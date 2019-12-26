<template>
  <div v-if="email != ''" class="container">
<<<<<<< HEAD
    <Personal v-bind:email="email"/>
    <Interests/>
=======
    <Personal/>
    <Interests v-bind:email="email"/>
>>>>>>> feature/user_interests
    <Accounts/>
    <LikedPosts v-bind:email="email"/>
    <DislikedPosts v-bind:email="email"/>
  </div>
</template>


<script>
// @ is an alias to /src
import Personal from '@/components/Personal.vue'
import Interests from '@/components/Interests.vue'
import Accounts from '@/components/Accounts.vue'
import LikedPosts from '@/components/LikedPosts.vue'
import DislikedPosts from '@/components/DislikedPosts.vue'
import {validate} from '@/Utilities/protect.js'

export default {
  name: 'profile',
  props: ['email'],
  components: {
    Personal,
    Interests,
    Accounts,
    LikedPosts,
    DislikedPosts
  },
  mounted(){
    this.$emit('interface')
  }
}
</script>