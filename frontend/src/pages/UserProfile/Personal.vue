<template>
  <card class="card" title="Edit Profile">
    <div>
      <form @submit="onSubmit">
        <div class="row">
          <div class="col-md-4">
            <fg-input type="email"
                      label="Email"
                      v-model="form.email">
            </fg-input>
          </div>
          <div class="col-md-4">
            <fg-input type="password"
                      label="Password"
                      v-model="form.password">
            </fg-input>
          </div>
          <div class="col-md-4">
            <fg-input type="text"
                      label="Phone"
                      v-model="form.phone">
            </fg-input>
          </div>
        </div>
        <div class="text-center">
          <b-button type="submit" variant="primary" round>Update Info</b-button>
        </div>
        <div class="clearfix"></div>
      </form>
    </div>
  </card>
</template>
<script>

import axios from 'axios'
import {getUserInfo, updateUserInfo} from '@/Utilities/user.js'

export default {
  name: 'personal',
  props:  ['email'],
  data(){
    return{
      form: {
        email: this.email,
        password: '',
        phone: ''
      },
    }
  },
  mounted(){
    this.getPersonalInfo()
  },
  methods: {
    onSubmit (e) {
      e.preventDefault()

      //Edit user
      updateUserInfo(this.email, this.form.email, this.form.password, this.form.phone)
      .then(response => {
        this.email = this.form.email
      })
    },
    getPersonalInfo(){
      getUserInfo(this.email)
      .then(response => {
        this.form.password = response.password
        this.form.phone = response.phone
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}
</script>
<style>
</style>
