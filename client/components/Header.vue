
<style scoped>
  .grey{

    background-color: #c0c1c2

  }
</style>
<template>
  <main>
    <link rel="stylesheet" href="./css/index.css">

      <div>




               <!--<<b-img fluid src="logo_innovambiente.png" width="308.95" height="66"> </b-img>
              <b-img fluid src="logo_greenext.png" width="178" height="66"> </b-img>-->

          <b-container fluid class="grey p-3">
            <b-row class="ml-5">
              <b-col class="mt-2" xl="3">
                <b-img fluid src="../static/img/logo_innovambiente.png" width="308.95" height="66"></b-img>
              </b-col>

              <b-col xl="3" class="mt-3">
                <b-img class="ml-5" fluid src="../static/img/logo_greenext.png" width="178" height="66"> </b-img>
              </b-col>

              <b-col  offset-xl="3" xl="3">
                <b-img src="../static/img/logo_infowaste.png" width="232" height="99"> </b-img>
              </b-col>
            </b-row>
          </b-container>

          <!--
              <b-img fluid src="../static/img/logo_innovambiente.png" width="308.95" height="66"> </b-img>
              <b-img class="ml-5" fluid src="../static/img/logo_greenext.png" width="178" height="66"> </b-img>



            <b-navbar-nav class="ml-auto">
                  <b-img src="../static/img/logo_infowaste.png" width="232" height="99"> </b-img>
            </b-navbar-nav>
            -->


          <b-container fluid class="bg-infowaste">
            <b-row class="pt-3 pb-3">
              <b-col class="text-white" xl="2" offset-xl="10">
                <b-dropdown size="lg" v-if="is_logged === true" variant="light" toggle-class="text-decoration-none" no-caret>
                    <template #button-content>
                      <b-icon class="h4 p-0 b-0 m-0" variant="dark" icon="person-circle"></b-icon>
                      <span class="sr-only">Search</span>
                    </template>
                    <b-dropdown-item href="#">Action</b-dropdown-item>
                    <b-dropdown-item href="#">Another action</b-dropdown-item>
                    <b-dropdown-item href="#">Something else here</b-dropdown-item>
                    <b-dropdown-item class="bg-danger" @click="logout()" href="#"><font class="text-white">Esci</font></b-dropdown-item>
                  </b-dropdown>
              </b-col>
            </b-row>
          </b-container>


      </div>
    </main>
</template>
<script>
  import axios from '@nuxtjs/axios'

  export default {
    mounted () {
      this.$axios.defaults.withCredentials = true;

      this.$axios
        .$get(`/is_logged`)
        .then(response => (this.is_logged = response))
    },

    /*async asyncData({ $axios, params })
      {
        try {
          $axios.defaults.withCredentials = true;
          let is_logged = await $axios.$get(`/is_logged`);
          console.log(is_logged)

          return { is_logged };

        } catch (e) {

            console.log(e)
            return { is_logged: false };
      }
    },*/

    data() {
      return {

        is_logged:false,

      }
    },

    methods:
    {

      async logout()
      {

        this.$axios.post('/logout')
        window.location.replace("./login")

      }

    }

  }
</script>
