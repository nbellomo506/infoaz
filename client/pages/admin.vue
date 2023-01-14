
import Header from '../components/Header'
import PageTitle from '../components/PageTitle'
import FieldTitle from '../components/FieldTitle'
import CostiSmaltimento from '../components/CostiSmaltimento'



<template>
  <main>
    <Header/>


      <div class="p-0 m-0 b-0">
        <b-container class="pb-5" v-if="is_logged === true && role === 'Admin'">
          <b-row>
            <b-col class="border rounded mt-5 pt-3 pb-3" xl="11">
              <PageTitle name="Pannello Admin"/>
                <b-container>
                  <b-row>
                    <b-col xl="12">
                      <h3>Utenti non associati ad azienda</h3>
                    </b-col>
                  </b-row>
                  <b-row class="border bg-light">
                    <b-col xl="2">
                      Nome Completo
                    </b-col>
                    <b-col xl="3">
                      Email
                    </b-col>
                    <b-col xl="2">
                      Partita IVA - Ragione Sociale
                    </b-col>
                    <b-col xl="2">
                      Data Richiesta
                    </b-col>
                    <b-col xl="3">
                      <b>Azienda</b>
                    </b-col>
                  </b-row>
                  <b-row class="border pt-3 pb-2" v-for="utente in utenti" :key="utente.id" v-if="utente.is_assigned === false">
                    <b-col xl="2">
                      {{utente.nome}} {{utente.cognome}}
                    </b-col>
                    <b-col xl="3">
                      {{utente.email}}
                    </b-col>
                    <b-col xl="2">
                      {{utente.p_iva}} - <br> {{utente.ragione_sociale}}
                    </b-col>
                    <b-col xl="2">
                      {{utente.request_date}}
                    </b-col>
                    <b-col xl="3">
                      <b-container class="b-0 m-0 p-0">
                        <b-row>
                          <b-col xl="6">
                            <select class="w-100 custom-select" v-model="utente.azienda" :key="utente.email" >
                              <option :selected="utente.azienda === azienda.id" v-for="azienda in aziende" :key="azienda.id" :value="azienda.id">
                                  {{ azienda.ragione_sociale }}
                              </option>
                            </select>
                          </b-col>
                          <b-col xl="6">
                            <b-button block @click="assignAzienda(utente.id,utente.azienda)" variant="success" name="button">Salva</b-button>
                          </b-col>
                        </b-row>
                      </b-container>
                    </b-col>
                  </b-row>
                  <b-row class="mt-5">
                    <b-col xl="12">
                      <h3>Utenti associati ad azienda</h3>
                    </b-col>
                  </b-row>
                  <b-row class="border bg-light">
                    <b-col xl="2">
                      Nome Completo
                    </b-col>
                    <b-col xl="3">
                      Email
                    </b-col>
                    <b-col xl="2">
                      Partita IVA - Ragione Sociale
                    </b-col>
                    <b-col xl="2">
                      Data Richiesta
                    </b-col>
                    <b-col xl="3">
                      <b>Azienda</b>
                    </b-col>
                  </b-row>
                  <b-row class="pt-3 pb-2 border" :key="utente.id" v-for="utente in utenti" v-if="utente.is_assigned === true ">
                    <b-col xl="2">
                      {{utente.nome}} {{utente.cognome}}
                    </b-col>
                    <b-col xl="3">
                      {{utente.email}}
                    </b-col>
                    <b-col xl="2">
                      {{utente.p_iva}} - <br> {{utente.ragione_sociale}}
                    </b-col>
                    <b-col xl="2">
                      {{utente.request_date}}
                    </b-col>
                    <b-col xl="3">
                      <b-container class="b-0 m-0 p-0">
                        <b-row>
                          <b-col xl="6">
                            <select class="w-100 custom-select" v-model="utente.azienda" :key="utente.email" >
                              <option :selected="utente.azienda === azienda.id" v-for="azienda in aziende" :key="azienda.id" :value="azienda.id">
                                  {{ azienda.ragione_sociale }}
                              </option>
                            </select>
                          </b-col>
                          <b-col xl="6">
                            <b-button block @click="assignAzienda(utente.id,utente.azienda)" variant="success" name="button">Salva</b-button>
                          </b-col>
                        </b-row>
                      </b-container>
                    </b-col>
                  </b-row>
                  <b-row class="mt-5">
                    <b-col xl="12">
                      <h3>Aziende</h3>
                    </b-col>
                  </b-row>
                  <b-row class="border bg-light">
                    <b-col xl="3">
                      <b>Azienda</b>
                    </b-col>
                    <b-col xl="3">
                      <b>PEF</b>
                    </b-col>
                  </b-row>
                  <b-row class="pt-3 pb-2 border" :key="azienda.partita_iva" v-for="azienda in aziende">
                    <b-col xl="3">
                      {{azienda.ragione_sociale}}
                    </b-col>
                    <b-col xl="5">
                      <b-form-radio-group v-model="azienda.pef_mis_o_ric" :options="pef_opts"></b-form-radio-group>
                    </b-col>
                    <b-col offset-xl="2" xl="2">
                      <b-button block @click="savePEF(azienda)" variant="success" name="button">Salva</b-button>
                    </b-col>
                  </b-row>
                  <b-row class="mt-5">
                    <b-col xl="12">
                      <h3>Aggiungi azienda</h3>
                    </b-col>
                  </b-row>
                  <b-row class="border bg-light">
                    <b-col xl="3">
                      Ragione Sociale
                    </b-col>
                    <b-col xl="3">
                      Partita IVA
                    </b-col>
                    <b-col xl="4">
                      PEF
                    </b-col>
                  </b-row>
                  <b-row class="border bg-light">
                    <b-col xl="3">
                      <b-form-input v-model="new_azienda.ragione_sociale" required>
                      </b-form-input>
                    </b-col>
                    <b-col xl="3">
                      <b-form-input v-model="new_azienda.partita_iva" required>
                      </b-form-input>
                    </b-col>
                    <b-col xl="4">
                      <b-form-radio-group v-model="new_azienda.pef_mis_o_ric" required :options="pef_opts">
                      </b-form-radio-group>
                    </b-col>
                    <b-col xl="2">
                      <b-button class="w-100" @click="add_azienda(new_azienda)" variant="success">
                        Aggiungi
                      </b-button>
                    </b-col>
                  </b-row>
                </b-container>
              </b-col>
            </b-row>
          </b-container>

          <b-container v-if="is_logged === false || role==='Normal'" class="mb-3">
            <b-row>
              <b-col offset-xl="1" xl="10">
                <b-container class="mb-3 mt-5">
                  <b-row>
                    <b-col xl="12">
                      <h1>Attenzione</h1>
                      <p>
                        <a v-if="is_logged === false" href="./login">Accedi</a>
                        <a v-else="role==='Normal'" >Accedi</a>

                        come Admin per visualizzare il contenuto
                      </p>
                    </b-col>
                  </b-row>
                </b-container>
              </b-col>
            </b-row>
          </b-container>
        </div>
      </main>
  </template>

  <script>
  import axios from 'axios'
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'

  export default {


    async asyncData({ $axios, params })
      {
        try {
          $axios.defaults.withCredentials = true;
          let is_logged = await $axios.$get(`/is_logged`);
          let role = await $axios.$get(`/role`);

            if(is_logged == true && role == "Admin")
            {
              var utenti = await $axios.$get(`/get_utenti`);
              var aziende = await $axios.$get(`/get_aziende`);

            }

          return {is_logged,role,aziende,utenti};

        } catch (e) {

            console.log(e)
            return {is_logged:false,aziende:[],utenti:[]};
      }


    },


    methods:
    {

        assignAzienda(user_id,azienda_id)
        {
          this.$axios.$put('/assign_azienda', {
            user_id:user_id,
            azienda_id:azienda_id
          })
          window.location.reload()
        },

        add_azienda(azienda)
        {
          if (azienda.ragione_sociale && azienda.partita_iva && azienda.pef_mis_o_ric)
          {
            /*
            this.$axios.defaults.baseURL = "https://graph.microsoft.com/beta";
            this.$axios.defaults.Authorization = "EwCIA8l6BAAUkj1NuJYtTVha+Mogk+HEiPbQo04AARDrO9kFUC9jhcZ//8amrgiUW48oS3XR8X2D2+v2dvI0GFKV/ue4VtXGSVobMtMpDaPzirGm5cZCuWXy9aJuTGZTlXvV86d9Ec4uywz3TqGn+pvOpnfZREUIZjx7Yz82DCw1Kc89CaFWOiTl7LEqnJOZA4h8XrLHDAjAJhb5BFlfiGztTw3QwZZ72BNrg6Uwhx/M/x0lQKzG0T3lVX5vLbrsHKsT3wScTi3AU0UEbfQeEaZX8FQ0i+GKCQLi/ZIsyp2JSPXc3N0HKyq9/F8lRCmBa5Eac8qyeDCg0cHdFJGzb1LkcAEVHSDu04wmCfQgTU84xh3LXa0pIplRCWw3GkEDZgAACMpBitlfwN1AWAKz8QFooVSyeSPhBjvWiL1xuNhkIoXOZSu8eTCh1jbZBa0yH3XWmOFMLLL0Lp/Tdya9y087Ex5e3fn1BOyQlSkkLn7YB/uEoP9ZGTesK8ePJimvZv5mmrvJdtRQ8eYDhrc0j4N3BGMV0fF951/ogrbaQtHF3Jx/QTWsqKQmPmuKiG0qqsTTOaZiM+Gh74s+gTrsBRbeauDj7q3vs7KkB8wttqbTk7Yp+cd28Oi4fxGdoF7gVe18EtxVm5Gm7abrzSIy6V7CXn3YusjmmeyTDiUva2tmTvXJ6HsPYXHu9E5oUX7rAhtfoUiFSCPjJpGDsrnq31gzzDOvErdHeg6c3qirloqc+T+EgRqjrlWuOWoXWDpsmmuIn+NLOG0FEEDZKXyCqE5ZXz3tcTIEcf+x47mT+6TLzHXrK4XJuqaUM6f9F3IMgGeEp6nepCLIPYJEdSKTP2PnjRRG51ZEk1yzvMznvZus/DVtZD96GFwIvx2etUjVvkzDKEK4puFVBLt0I0ODwIt0Ip8bxOrxjEKwucqfMzi7eIdVUQtvDWNvJPpUC612jYXk9ohCj9BK7JesKLwrYbgb8OmunjRxJef+sAfYyul07hTC/dpyqSq7YU3mIs6RRg8g0qhiVgYLoDHG47yuWmojaCAH6+x+bCgX9jc1VgD1lVIYQRLl0unKN+q5gerl0m5hyrChytiL/UMSTd7p82L1qPYKBiG3zPdYOCHb6qZudWgp4MAivlpoemncIvdu1wxWQ3pXTTjseEFH5zmC/5gq/Lw1kBFlArgO92zEP0aN2AejRjWUAg=="
            const options = {
                headers: {
                    Authorization: `Bearer ${this.$axios.defaults.Authorization}`
                },

                  name: azienda.ragione_sociale,
                  folder: {}

            };

            var we = this.$axios.$get('/me/',options)
            .then(response => {

                console.log(response);
                if(response.status >= 200 && response.status <= 208)
                {
                    alert("ottimo")
                }
            })

            .catch(error => {

                console.log(error);
                alert(error)

            });
            */
            this.$axios.defaults.baseURL = "http://localhost:8000/api";

            this.$axios.$post('/add_azienda', {

              ragione_sociale:azienda.ragione_sociale,
              partita_iva:azienda.partita_iva,
              pef_mis_o_ric:azienda.pef_mis_o_ric,

            })



              //window.location.reload()
          }
        },

        savePEF(azienda)
        {
          this.$axios.$put('/savePEF', {
            azienda:azienda.id,
            pef:azienda.pef_mis_o_ric
          })

          window.location.reload()
        }

    },


    data() {

        return {

                    new_azienda:
                    {
                      ragione_sociale:'',
                      partita_iva:'',
                      pef_mis_o_ric:''
                    },

                    pef_opts:[
                      { text: 'CALCOLATO', value: 'CALCOLATO' },
                      { text: 'MISURATO', value: 'MISURATO' }
                    ],
                    is_logged:false,
                    role:false
                }

            }


  };
  </script>
