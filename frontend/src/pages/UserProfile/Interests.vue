<template>
    <!-- Interests section -->
    <card title="Interests" class="card">

      <!-- Add Interest Components -->
       <b-form @submit="onSubmit">

            <!-- Interest -->
            <b-form-group id="text" label-for="tags">
                <b-form-input id="tags" name="tags" v-model="form.tags" required placeholder="Topic, Tag, Interest, etc"></b-form-input>
            </b-form-group>

            <!-- Submit -->
            <b-button type="submit" variant="primary">Add Interest</b-button>
        </b-form>
        <div>
          <ul class="list-unstyled team-members">
            <div v-bind:key="index" v-for="(interest, index) in interests">
              
                <Interest @interface="getTags" v-bind:email="email" v-bind:interest="interest"/>
              
            </div>
          </ul>
        </div>
    </card>
</template>
<script>

import {addTags, getTags} from '@/Utilities/profilePosts.js'
import Interest from './Interest.vue'

export default {
  components:{
    Interest
  },
  name: 'Interests',
  props: ['email'],
  data(){
    return{
        message: String,
        interests: [],
        form:{
            tags: ''
        }
    }
  },
  mounted(){
    this.getTags()
  },
  methods: {
    onSubmit(e){
        e.preventDefault();
        addTags(this.email, this.form.tags)
        .then(response =>{
            this.getTags()
        }).catch(error => {

        })
    },
    async getTags(){
      getTags(this.email)
      .then(response => {
        this.interests = response
      })
      .catch(error => {
        
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
div{
    margin-top: 20px;
}
</style>
