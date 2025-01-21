
<style scoped>

</style>
<template>
  <main>
        <div>
          <b-container fluid class="bg-light p-3">
            <b-row align-v="center" class="ml-0">
              <b-col offset-xl="1" xl="3">
                <b-img src="../static/img/logo_infowaste.png" width="232" height="99"> </b-img>
              </b-col>
            </b-row>
          </b-container>
        </div>

        <b-container fluid class="bg-infowaste m-0 b-0 p-0">
          <b-row>
            <b-col v-if="loaded === true" class="text-center pt-3 pb-3 pr-xl-0 pe-sm-0" offset-xl="2" xl="1" offset-sm="3" sm="6">
              <b-button v-if="is_logged === true" class="shadow-sm w-100" :to="locations.home" variant="white">
                Home
                <b-icon class="text-dark" icon="house-fill"></b-icon>
              </b-button>
            </b-col>
            <b-col v-if="loaded === true" class="text-center pt-3 pb-3" offset-xl="4" xl="1" offset-sm="3" sm="6">
              <b-button v-b-modal="'help-tab'" class="shadow-sm w-100 pl-0 pr-0" variant="warning" v-if="is_logged === true">
                Help
                <b-icon class="text-dark" icon="patch-question">
                </b-icon>
              </b-button>
            </b-col>
            <b-col v-if="loaded === true" offset-xl="0" xl="1" class="text-center pt-3 pb-3" offset-sm="3" sm="6">
              <b-button block class="shadow-sm w-100" :to="locations.admin" variant="white" v-if="is_logged === true && role==='Admin'">
                Admin
              </b-button>
            </b-col>
            <b-col v-if="loaded === true" class="text-center pt-3 pb-3" offset-xl="0" xl="1" offset-sm="3" sm="6">
              <b-button v-if="is_logged === true" @click="logout()" class="shadow-sm w-100" variant="white" >
                Esci <b-icon class="text-danger" icon="box-arrow-right"></b-icon>
              </b-button>
            </b-col>
            <b-col class="pt-3 pb-3" xl="2" v-if="!is_logged && this.$route.name !== 'login' && loaded === true">
              <b-button class="shadow-sm" :to="locations.login" variant="white">
                Accedi
                <b-icon class="text-dark" icon="box-arrow-in-right">
                </b-icon>
              </b-button>
            </b-col>
          </b-row>
        </b-container>
        <meta name="google" value="notranslate">
        <b-modal id="help-tab" cancel-variant="danger" title="Messaggio" ok-variant="infowaste" @ok="askHelp" cancel-title="Annulla" ok-title="Invia">
          Verrà inviata un'email ad assistenza@bintobit.com
          <b-form-input v-model="help_message"></b-form-input>
        </b-modal>
      </main>
  </template>


  <script>
  import axios from '@nuxtjs/axios'

  export default {
    mounted () {


    this.loaded = false
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

          this.$axios.$get(`/role`)
          .then((response) => {
            this.role = response
            this.$axios.$get(`/is_company_set`)
              .then((response) => {
              this.is_company_set = response
              this.loaded = true
          })

          })

        })
    },


    data() {
      return {

        is_logged:false,
        loaded:false,
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
        },
        help_message:""

      }
    },

    methods:
    {

      logout(){
          try {

            this.$axios.post('/logout')
            .then((response) => {
              window.location.reload()
            })
          } catch (e) {

            console.log(e)

          }
          //window.location.replace(this.locations.login)
      },

      askHelp(){
        this.$axios.post('/askHelp', {
          message: this.help_message,
          section: this.$route.name,
        })
      }

    }

  }
</script>
