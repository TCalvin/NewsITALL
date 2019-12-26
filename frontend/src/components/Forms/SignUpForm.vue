<template>
    <div class="container">

        <!-- Sign Up Success Alert -->
        <b-alert variant="success" dismissible fade :show="showSuccessAlert" @dismissed="showSuccessAlert=false">
            {{this.message}}
        </b-alert>

        <b-alert variant="danger" dismissible fade :show="showErrorAlert" @dismissed="showErrorAlert=false">
            {{this.message}}
        </b-alert>

        <!-- Sign Up Form -->
        <b-form @submit="onSubmit">

            <!-- Email -->
            <b-form-group id="EmailGroup" label="Email address:" label-for="signupEmail" description="We'll never share your email with anyone else.">
                <b-form-input name="form.email" id="signupEmail" v-model="form.email" type="email" required placeholder="Enter email"></b-form-input>
            </b-form-group>

            <!-- Password-->
            <b-form-group id="PasswordGroup" label="Password:" label-for="signupPassword" description="Don't share your password with anyone.">
                <b-form-input name="form.password" id="signupPassword" :state="passwordValidation" v-model="form.password" type="password" aria-describedby="password-help-block" required placeholder="Enter password"></b-form-input>
            </b-form-group>
            <b-form-invalid-feedback :state="passwordValidation">
              Your password must be 8-20 characters long, contain letters and numbers, and must not contain spaces, special characters, or emojis.
            </b-form-invalid-feedback>
            <b-form-valid-feedback :state="passwordValidation">
              Looks Good.
            </b-form-valid-feedback>
            <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
  </div>
</template>

<script>
import axios from 'axios'
import {register} from '@/Utilities/registration.js'
import {login} from '@/Utilities/login.js'

export default {
  name: 'SignUp',
  data(){
    return{
        message: '',
        form:{
            email: '',
            password: ''
        },
        showSuccessAlert: false,
        showErrorAlert: false,
        valid: false
    }
  },
  methods: {
    onSubmit (e) {

        e.preventDefault()

        if(this.valid){

          register(this.form.email, this.form.password)
          .then(response => {

            this.message = response.message
            if(response.success){
              this.showSuccessAlert=true
              setTimeout(this.registerSuccess, 2000)
            }else{
              this.showErrorAlert=true
            }
          })
        }else{
          this.message = 'Password is invalid'
          this.showErrorAlert=true
        }
    },
    registerSuccess(){
      login(this.form.email, this.form.password)
      .then(response => {
          this.$emit('interface')
          this.$router.go()
        })
    }
  },
  
  computed: {
    passwordValidation(){
      var letterRegex = this.form.password.match(/[a-zA-Z]/)
      var numberRegex = this.form.password.match(/[1-9][0-9]*/)
      var spaceRegex = this.form.password.match(/[ \t\n\r]/)
      var specialRegex = this.form.password.match(/[!-/:-@[-`{-~]/)

      this.valid = this.form.password.length > 7 && this.form.password.length < 21 && letterRegex != null && numberRegex != null && spaceRegex == null && specialRegex == null
      return this.valid
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
  color: #08dce4;
}
div{
    margin-top: 20px;
}
</style>
