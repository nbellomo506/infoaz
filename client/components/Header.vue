
<style scoped>
  .grey{

    background-color: #c0c1c2

  }
</style>
<template>
  <main>
      <div>
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
        </div>


        <b-container fluid class="bg-infowaste p-3 m-0 b-0">
          <b-row v-if="is_logged == true">
            <b-col class="pt-1 pb-1" cols="12" offset-xl="1" xl="1" offset-lg="2" lg="2">
              <b-button class="shadow-sm" v-if="this.$route.name !== 'home'" block :to="locations.home" variant="white">
                <b-icon class="text-dark" icon="house-fill">
                </b-icon>
                Home
              </b-button>
            </b-col>

            <b-col class="pt-1 pb-1" cols="12" offset-xl="8" xl="1" offset-lg="4" lg="2">
              <b-dropdown class="shadow" block variant="white" text="Menu">
                <b-dropdown-item :to="locations.home" v-if="this.$route.name !== 'home'">Home</b-dropdown-item>
                <b-dropdown-item :to="locations.anagrafica" v-if="this.$route.name !== 'anagrafica' && (is_logged === true ) ">Anagrafica</b-dropdown-item>
                <b-dropdown-item :to="locations.admin" variant="infowaste" v-if="this.$route.name !== 'admin' && is_logged === true && role==='Admin'">Admin</b-dropdown-item>
                <b-dropdown-item class="bg-danger" @click="logout()">
                  <b-container class="p-0 m-0 b-0">
                    <b-row>
                      <b-col cols="8">
                        <font class="text-white">
                          Esci
                        </font>
                      </b-col>
                      <b-col cols="2">
                        <b-icon class="text-white" icon="box-arrow-right"></b-icon>
                      </b-col>
                    </b-row>
                  </b-container>
                </b-dropdown-item>
              </b-dropdown>
            </b-col>

          </b-row>
        </b-container>

      </main>
  </template>


  <script>
  import axios from '@nuxtjs/axios'

  export default {
    mounted () {

      this.$axios.defaults.withCredentials = true;

      var pages = ["home","anagrafica","admin","login"]
      var i = 0
      var page = ""
      do
      {
        if (this.$route.name == 'compila_dati_comune-id')
        {
          page = pages[i]
          this.locations[page] = "../../"+page
          //alert(this.locations.page)

        }
          else {

            page = pages[i]
            this.locations[page] = "./"+page
            //alert(this.locations.page)

          }
          i++

      }while (i < pages.length)

      this.$axios.$get(`/is_logged`)
        .then((response) => {
          this.is_logged = response
          if (this.is_logged === false && ( this.$route.name === 'home'
            || this.$route.name === 'anagrafica' || this.$route.name === 'compila_dati_comune-id'
            || this.$route.name === 'admin')
          )
          {
            if (typeof window !== 'undefined')
            {
              // 👉️ can use window here
              console.log(this.locations.login)
              window.location.replace(this.locations.login)
            }
          }

          if (this.is_logged === true && this.$route.name === 'login')
          {
            if (typeof window !== 'undefined')
            {
              // 👉️ can use window here
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
        locations:
        {
          home:'home',
          anagrafica:'anagrafica',
          admin:'admin',
          login:'login'
        }

      }
    },

    methods:
    {

      logout()
      {
          try {

            this.$axios.post('/logout')

          } catch (e) {

            console.log(e)

          }
          //window.location.replace(this.locations.login)
          window.location.reload()
      }

    }

  }
</script>
