<template>
  <nav class="navbar navbar-expand-lg navbar-light">
    <div class="container-fluid">
      <a class="navbar-brand" v-bind:href="pathName">{{routeName}}</a>
      <button class="navbar-toggler navbar-burger"
              type="button"
              @click="toggleSidebar"
              :aria-expanded="$sidebar.showSidebar"
              aria-label="Toggle navigation">
        <span class="navbar-toggler-bar"></span>
        <span class="navbar-toggler-bar"></span>
        <span class="navbar-toggler-bar"></span>
      </button>

      <div class="collapse navbar-collapse">

        <ul class="navbar-nav ml-auto">

          <li class="nav-item" v-if="email!=''" v-b-modal.logoutModal>
            <a href="#" class="nav-link">
               <font-awesome-icon :icon="['fas', 'sign-out-alt']"/>
              <p>
                Logout
              </p>
            </a>
          </li>

          <b-modal id="logoutModal" title="Log Out" hide-footer>
            <LogOut @interface="validate"/> 
          </b-modal>

          <li class="nav-item" v-if="email==''" v-b-modal.loginModal>
            <a href="#" class="nav-link">
               <font-awesome-icon :icon="['fas', 'sign-in-alt']"/>
              <p>
                Login
              </p>
            </a>
          </li>

          <!-- Log In Modal -->
          <b-modal id="loginModal" title="Log In" hide-footer>
            <LogIn @interface="validate"/> 
          </b-modal>

          <li class="nav-item" v-if="email==''" v-b-modal.signupModal>
            <a href="#" class="nav-link">
              <font-awesome-icon :icon="['fas', 'user-plus']"/>
              <p>
                Register
              </p>
            </a>
          </li>

          <!-- Sign Up Modal -->
          <b-modal id="signupModal" title="Sign Up" hide-footer>
            <SignUp @interface="validate"/>
          </b-modal>
        </ul>
      </div>
    </div></nav>
</template>
<script>

import LogIn from '@/components/Forms/LoginForm.vue'
import LogOut from '@/components/Forms/Logout.vue'
import SignUp from '@/components/Forms/SignUpForm.vue'


export default {
  computed: {
    routeName() {
      const { name } = this.$route;
      return this.capitalizeFirstLetter(name);
    },
    pathName() {
      return "#" + this.$route.path;
    }
  },
  components: {
    LogIn,
    SignUp,
    LogOut
  },
  props: ['email'],
  data() {
    return {
      activeNotifications: false
    };
  },
  methods: {
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    toggleNotificationDropDown() {
      this.activeNotifications = !this.activeNotifications;
    },
    closeDropDown() {
      this.activeNotifications = false;
    },
    toggleSidebar() {
      this.$sidebar.displaySidebar(!this.$sidebar.showSidebar);
    },
    hideSidebar() {
      this.$sidebar.displaySidebar(false);
    },
    validate(){
       this.$emit('interface')
    }
  }
};
</script>
<style>
</style>
