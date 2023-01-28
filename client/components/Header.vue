
<style scoped>
  .grey{

    background-color: #c0c1c2

  }
</style>
<template>
  <main>
    <link rel="stylesheet" href="./css/index.css">

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


          <b-container fluid class="bg-infowaste" hidden>
            <b-row class="pt-3 pb-3">
              <!--<b-col v-if="is_logged === true" class="text-white pt-1 mb-1" sm="6" xl="2">
                <b-button class="p-2 h-100" onclick="history.back()" v-if="this.$route.name === 'anagrafica' || this.$route.name === 'admin'" type="button" block variant="light" name="button">
                  <b-icon class="h4 p-0 b-0 m-0" variant="dark" icon="arrow-left">
                  </b-icon>
                  Indietro
                </b-button>
              </b-col>-->
              <b-col v-if="is_logged === true" class="text-white mt-1" sm="6" offset-xl="1" xl="2">
                <b-dropdown block size="lg"  variant="light" toggle-class="text-decoration-none" no-caret>
                  <template #button-content>
                    <b-icon class="h4 p-0 b-0 m-0" variant="dark" icon="list"></b-icon>
                  </template>
                  <b-dropdown-item :to="locations.home" v-if="this.$route.name !== 'home'">Home</b-dropdown-item>
                  <b-dropdown-item :to="locations.anagrafica" v-if="this.$route.name !== 'anagrafica' && (is_logged === true ) ">Anagrafica</b-dropdown-item>
                  <b-dropdown-item :to="locations.admin" v-if="this.$route.name !== 'admin' && is_logged === true && role==='Admin'">Admin</b-dropdown-item>

                  <b-dropdown-item :to="locations.login" @click="findPath('login')" class="bg-danger" >
                    <font class="text-white">
                      Esci
                    </font>
                  </b-dropdown-item>
                </b-dropdown>
              </b-col>
            </b-row>
          </b-container>
        </div>

        <b-navbar style="text-align:center;display:inherit;font-size:large" type="dark" variant="infowaste">
          <div v-if="is_logged === true">

            <b-collapse id="nav-collapse" is-nav>
              <b-navbar-nav class="ml-auto">

                  <b-nav-item-dropdown class="text-light" right>
                    <!-- Using 'button-content' slot -->
                    <template #button-content>
                      Menu
                    </template>
                      <b-dropdown-item :to="locations.home"  v-if="this.$route.name !== 'home'">Home</b-dropdown-item>
                      <b-dropdown-item :to="locations.anagrafica" v-if="this.$route.name !== 'anagrafica' && (is_logged === true ) ">Anagrafica</b-dropdown-item>
                      <b-dropdown-item :to="locations.admin" variant="infowaste" v-if="this.$route.name !== 'admin' && is_logged === true && role==='Admin'">Admin</b-dropdown-item>
                      <b-dropdown-item :to="locations.login" class="bg-danger"  @click="findPath('login')">
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
                  </b-nav-item-dropdown>
                </b-navbar-nav>
            </b-collapse>
          </div>
        </b-navbar>
      </main>
  </template>
  <script>
  import axios from '@nuxtjs/axios'

  export default {
    mounted () {

      this.$axios.defaults.withCredentials = true;

      this.$axios.$get(`/is_logged`)
        .then((response) => {
          this.is_logged = response
        })

        this.$axios.$get(`/role`)
          .then((response) => {
            this.role = response
          })

          this.$axios.$get(`/is_company_set`)
            .then((response) => {
              this.is_company_set = response
            })

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

        }else {

          page = pages[i]
          this.locations[page] = "./"+page
          //alert(this.locations.page)

        }
        i++

      }while (i < pages.length)

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

      findPath(page)
      {

        if(page == 'login')
        {
          this.$axios.post('/logout')
          window.location.replace(this.locations.login)


        }



      }

    }

  }
</script>
