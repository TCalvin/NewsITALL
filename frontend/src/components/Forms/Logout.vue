<template>
    <div class="container">

        <!-- Logout -->
        Logging Out...
        
  </div>
</template>

<script>
import {logout} from '@/Utilities/logout.js'
export default {
  name: 'LogOut',
  mounted(){
    setTimeout(this.logout(), 2000)
  },
  methods: {
    logout(){
        logout()
        this.$emit('interface')
        this.$router.go()
    }
  },
  data(){
    return{

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
div{
    margin-top: 20px;
}
</style>
