<template>
  <div class="container">
    <DiscoverFeed v-bind:email="email"/>
  </div>
</template>


<script>

// @ is an alias to /src
import DiscoverFeed from '@/components/Feeds/DiscoverFeed.vue'
import {validate} from '@/Utilities/protect.js'

export default {
  name: 'discover',
  props: ['email'],
  components: {
    DiscoverFeed
  },
  mounted(){
    this.$emit('interface')
  }
}
</script>