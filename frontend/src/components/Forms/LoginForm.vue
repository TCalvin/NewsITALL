<template>
    <div class="container">

      <!-- Logged in Successfully Alert -->
        <b-alert variant="success" dismissible fade :show="showSuccessAlert" @dismissed="showDismissibleAlert=false">
            {{this.message}}
        </b-alert>

        <b-alert variant="danger" dismissible fade :show="showErrorAlert" @dismissed="showDismissibleAlert=false">
            {{this.message}}
        </b-alert>

        <!-- Login form -->
        <b-form @submit="onSubmit">

            <!-- Email Address -->
            <b-form-group id="EmailGroup" label="Email address:" label-for="loginEmail">
                <b-form-input id="loginEmail" name="email" v-model="form.email" type="email" required placeholder="Enter email"></b-form-input>
            </b-form-group>

            <!-- Password -->
            <b-form-group id="PasswordGroup" label="Password:" label-for="loginPassword" description="Don't share your password with anyone.">
                <b-form-input id="loginPassword" name="password" v-model="form.password" type="password" aria-describedby="password-help-block" required placeholder="Enter password"></b-form-input>
            </b-form-group>

            <!-- Submit -->
            <b-button type="submit" variant="primary">
              <font-awesome-icon :icon="['fas', 'sign-in-alt']"/>
            </b-button>
        </b-form>
  </div>
</template>

<script>
import axios from 'axios'
import {login} from '@/Utilities/login.js'
export default {
  name: 'LogIn',
  methods: {

    /**
     * Called When submit button is pushed
     */
    onSubmit (e) {
      e.preventDefault()
        login(this.form.email, this.form.password)
        .then(response => {
          this.message = response.message
          if(response.success){
            this.showSuccessAlert=true
            setTimeout(this.loginSuccess, 2000)
          }
          else{
            this.showErrorAlert=true
          }
          
          //this.$router.go()
        })
        
    },
    loginSuccess(){
        this.$emit('interface')
        this.$router.go()
    }
  },
  data(){
    return{
        message: String,
        form:{
            email: '',
            password: ''
        },
        showSuccessAlert: false,
        showErrorAlert: false
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
