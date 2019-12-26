<template>
  <div class="content">
    <div class="container-fluid">
        <transition name="fade" mode="out-in">
          <!-- your content here -->
          <router-view @interface="validate" v-bind:email="email"></router-view>
        </transition>
    </div>
  </div>
</template>
<script>
export default {
  props: ['email'],
  mounted(){
    this.validate()
  },
  methods: {
    validate(){
      this.$emit('interface')
    }
  }
};
</script>
<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.1s;
}

.fade-enter,
  .fade-leave-to
  /* .fade-leave-active in <2.1.8 */

 {
  opacity: 0;
}
</style>
