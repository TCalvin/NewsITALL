<template>
  <div>
    <Feed @interface="validate" v-bind:email="email"/>
  </div>
</template>
<script>
import Feed from '@/components/Feeds/Feed.vue'

export default {
  components: {
    Feed
  },
  props: ['email'],
  mounted(){
    this.validate()
  },
  methods:{
    validate(){
      this.$emit('interface')
    }
  }
}
</script>
<style>
</style>
