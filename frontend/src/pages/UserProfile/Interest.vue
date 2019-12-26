<template>
    <div class="row">
      <div class="col-9">
        {{interest}}
        <br>
      </div>

      <div class="col-3">
        <b-button @click="$bvModal.show(interest)" type="danger" outline icon>
         <font-awesome-icon :icon="['fas', 'ban']"/>
        </b-button>
      </div>

      <!-- Remove -->
      <b-modal v-bind:id='interest' title="Remove" hide-footer>
          <p>Are you sure you want to remove "<b>{{interest}}</b>" from your interests?</p>
          <b-button block @click="removeTags(interest)" variant='danger'>Remove</b-button>
      </b-modal>
    </div>
</template>

<script>

import {removeTags} from '@/Utilities/profilePosts.js'

export default {
  name: 'Interest',
  props: ['interest', 'email'],
  data(){
    return{
    }
  },
  methods: {

    /**
     * Called when a liked post is removed
     */
    removeTags(interest){

      removeTags(this.email, this.interest)
      .then(response => {
        this.$bvModal.hide(interest)
        this.$emit('interface')
      }).catch({
          
      })
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
</style>
