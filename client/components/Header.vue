
<style scoped>

</style>
<template>
  <main>
      <div>
          <b-container fluid class="bg-light p-3">
            <b-row align-v="center" class="ml-5">
              <b-col xl="3">
                <b-img class="ml-5" fluid src="../static/img/logo_greenext.png" width="178" height="66"> </b-img>
              </b-col>
              <b-col xl="3">
                <b-img fluid src="../static/img/logo_innovambiente.png" width="308.95" height="66"></b-img>
              </b-col>
              <b-col offset-xl="3" xl="3">
                <b-img src="../static/img/logo_infowaste.png" width="232" height="99"> </b-img>
              </b-col>
            </b-row>
          </b-container>
        </div>

        <b-container fluid class="bg-infowaste p-3 m-0 b-0">
          <b-row>
            <b-col offset-xl="2" xl="2">
              <b-button v-if="is_logged === true" class="shadow-sm" :to="locations.home" variant="white">
                <b-icon class="text-dark" icon="house-fill">
                </b-icon>
                Home
              </b-button>
            </b-col>
            <b-col offset-xl="4" xl="1">
              <b-button block class="shadow-sm" :to="locations.admin" variant="white" v-if="is_logged === true && role==='Admin'">
                Admin
              </b-button>
            </b-col>
            <b-col xl="2" v-if="is_logged === true">
              <b-button @click="logout()" class="shadow-sm" variant="white" >
                Esci <b-icon class="text-danger" icon="box-arrow-right"></b-icon>
              </b-button>
            </b-col>
            <b-col xl="2" v-if="!is_logged && this.$route.name !== 'login'">
              <b-button class="shadow-sm" :to="locations.login" variant="white">
                Accedi
                <b-icon class="text-dark" icon="box-arrow-in-right">
                </b-icon>
              </b-button>
            </b-col>
          </b-row>
        </b-container>
      </main>
  </template>


  <script>
  import axios from '@nuxtjs/axios'

  export default {
    mounted () {

    let userAgent = navigator.userAgent;
       let browserName;

       if(userAgent.match(/firefox|fxios/i || /safari/i || /opr\//i))
       {
         this.browserAlert = true

       }else {
         this.browserAlert = false

       }

      this.$axios.defaults.withCredentials = true;

      if (this.$route.name == "compila_dati_comune-id")
      {

        for (let location in this.locations)
        {
          this.locations[location] = "./../../" + this.locations[location]
        }

      }


      this.$axios.$get(`/is_logged`)
        .then((response) => {
          this.is_logged = response
          if (this.is_logged === false && (this.$route.name !== 'new_password' && this.$route.name !== 'password_reset' && this.$route.name !== 'login' && this.$route.name !== 'registrazione' && this.$route.name !== 'game' && this.$route.name !== 'game2'))
          {
              window.location.replace(this.locations.login)
          }

          if (this.is_logged === true && this.$route.name === 'login')
          {
            if (typeof window !== 'undefined')
            {
              window.location.replace("./home")
            }
          }

        })

        this.$axios.$get(`/role`)
          .then((response) => {
            this.role = response
          })

        this.$axios.$get(`/is_company_set`)
          .then((response) => {
            this.is_company_set = response
          })

    },


    data() {
      return {

        is_logged:false,
        is_company_set:false,
        role:'Normal',
        browserAlert:undefined,
        locations:
        {
          home:'home',
          anagrafica:'anagrafica',
          admin:'admin',
          login:'login',
          credits:'credits'
        }

      }
    },

    methods:
    {

      logout()
      {
          try {

            this.$axios.post('/logout')
            .then((response) => {
              window.location.reload()
            })
          } catch (e) {

            console.log(e)

          }
          //window.location.replace(this.locations.login)
      }

    }

  }
</script>
