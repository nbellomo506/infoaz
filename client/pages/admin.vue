h
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
                    <b-col xl="2" >
                      Nome Completo
                      <b-button @click="orderUsers('nome',false)" type="button" variant="light" name="button">
                        <b-icon icon="sort-down-alt"></b-icon>
                      </b-button>
                    </b-col>
                    <b-col xl="3">
                      Contatti
                      <b-button @click="orderUsers('email',false)" type="button" variant="light" name="button">
                        <b-icon icon="sort-down-alt"></b-icon>
                      </b-button>
                    </b-col>
                    <b-col xl="2">
                      Partita IVA - Ragione Sociale
                      <b-button @click="orderUsers('ragione_sociale',false)" type="button" variant="light" name="button">
                        <b-icon icon="sort-down-alt"></b-icon>
                      </b-button>
                    </b-col>
                    <b-col xl="2">
                      Data Richiesta
                      <b-button @click="orderUsers('request_date',false)" type="button" variant="light" name="button">
                        <b-icon icon="sort-down-alt"></b-icon>
                      </b-button>
                    </b-col>
                    <b-col xl="3">
                      <b>Azienda</b>
                    </b-col>
                  </b-row>
                  <b-row class="border pt-3 pb-2" v-for="utente in utenti_non_azienda" :key="utente.id">
                    <b-col xl="2">
                      {{utente.nome}} {{utente.cognome}}
                    </b-col>
                    <b-col xl="3">
                      {{utente.email}} <br> {{utente.telefono}}
                    </b-col>
                    <b-col xl="2">
                      {{utente.p_iva}} <br> {{utente.ragione_sociale}}
                    </b-col>
                    <b-col xl="2">
                      {{utente.data}}
                      <br>
                      {{utente.orario}}
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
                    <b-col xl="2" >
                      Nome Completo
                      <b-button @click="orderUsers('nome',true)" type="button" variant="light" name="button">
                        <b-icon icon="sort-down-alt"></b-icon>
                      </b-button>
                    </b-col>
                    <b-col xl="3">
                      Contatti
                      <b-button @click="orderUsers('email',true)" type="button" variant="light" name="button">
                        <b-icon icon="sort-down-alt"></b-icon>
                      </b-button>
                    </b-col>
                    <b-col xl="2">
                      Partita IVA - Ragione Sociale
                      <b-button @click="orderUsers('ragione_sociale',true)" type="button" variant="light" name="button">
                        <b-icon icon="sort-down-alt"></b-icon>
                      </b-button>
                    </b-col>
                    <b-col xl="2">
                      Data Richiesta
                      <b-button @click="orderUsers('request_date',true)" type="button" variant="light" name="button">
                        <b-icon icon="sort-down-alt"></b-icon>
                      </b-button>
                    </b-col>
                    <b-col xl="3">
                      <b>Azienda</b>
                    </b-col>
                  </b-row>
                  <b-row class="pt-3 pb-2 border" :key="utente.id" v-for="utente in utenti_azienda">
                    <b-col xl="2">
                      {{utente.nome}} {{utente.cognome}}
                    </b-col>
                    <b-col xl="3">
                      {{utente.email}} <br> {{utente.telefono}}
                    </b-col>
                    <b-col xl="2">
                      {{utente.p_iva}} <br> {{utente.ragione_sociale}}
                    </b-col>
                    <b-col xl="2">
                      {{utente.data}}
                      <br>
                      {{utente.orario}}
                    </b-col>
                    <b-col xl="3">
                      <b-container class="b-0 m-0 p-0">
                        <b-row>
                          <b-col xl="6">
                            <select class="w-100 custom-select" v-model="utente.azienda" :key="utente.email" >
                              <option :selected="utente.azienda === azienda.id" v-for="azienda in aziende" :key="azienda.id" :value="azienda.id">
                                  {{azienda.ragione_sociale}}
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
                    <b-col xl="4">
                      <b-form-radio-group v-model="azienda.pef_mis_o_ric" :options="pef_opts"></b-form-radio-group>
                    </b-col>
                    <b-col offset-xl="1" xl="2">
                      <b-button block @click="savePEF(azienda)" variant="success" name="button">Salva</b-button>
                    </b-col>
                    <b-col v-if="azienda.ragione_sociale !== 'infowaste'" xl="2">
                      <b-button block @click="del_azienda(azienda)" variant="danger" name="button">
                        <b-icon class="h4 p-0 b-0 m-0" variant="white" icon="trash"></b-icon>
                      </b-button>
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
                      <b-form-input maxlength="11" v-model="new_azienda.partita_iva" required>
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
                        <a v-else="role==='Normal'" >Accedi</a> come Admin per visualizzare il contenuto
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
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>

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

                  for (var i = 0; i < utenti.length; i++)
                  {
                      var data = []
                      var orario = []

                        for (var j = 0; utenti[i].request_date[j] != 'T'; j++)
                        {
                          data[j] = utenti[i].request_date[j]
                        }

                        j++
                        var k = 0

                          while (j < utenti[i].request_date.length )
                          {
                              if (utenti[i].request_date[j] == '+' || utenti[i].request_date[j] == '.' || utenti[i].request_date[j] == 'Z')
                              {
                                j = utenti[i].request_date.length
                              }
                                  else
                                  {
                                    orario[k] = utenti[i].request_date[j]
                                  }
                              j++
                              k++
                          }

                      data = data.join('')
                      data.toString()

                      orario = orario.join('')
                      orario.toString()

                      utenti[i].data = data
                      utenti[i].orario = orario

                  }

              var utenti_non_azienda = []
              var utenti_azienda = []

              for (var i = 0; i < utenti.length; i++)
              {
                if (utenti[i].azienda !== null && utenti[i].is_assigned === true)
                {
                  utenti_azienda.push(utenti[i])
                }
                  else
                      {
                        utenti_non_azienda.push(utenti[i])
                      }
              }

              var aziende = await $axios.$get(`/get_aziende`);

            }

          return {is_logged,role,aziende,utenti,utenti_azienda,utenti_non_azienda};

        } catch (e) {

            console.log(e)
            return {is_logged:false,aziende:[],utenti:[]};
      }


    },


    methods:
    {

        async orderUsers(by,assigned)
        {

            if (assigned)
            {
              this.utenti_azienda = this.utenti_azienda.sort((t1,t2) => t1[by] < t2[by] ? -1 : 1)
            }
            else {
              this.utenti_non_azienda = this.utenti_non_azienda.sort((t1,t2) => t1[by] < t2[by] ? -1 : 1)
            }

        },

        async assignAzienda(user_id,azienda_id)
        {
          this.$axios.post('/assign_azienda', {
            user_id:user_id,
            azienda_id:azienda_id
          })
          location.reload()
        },

        async add_azienda(azienda)
        {
          if (azienda.ragione_sociale && azienda.partita_iva && azienda.pef_mis_o_ric)
          {

            this.$axios.post('/add_azienda', {

              ragione_sociale:azienda.ragione_sociale,
              partita_iva:azienda.partita_iva,
              pef_mis_o_ric:azienda.pef_mis_o_ric,

            })

              location.reload()
          }
        },

        async del_azienda(azienda)
        {
          this.$axios.post('/del_azienda', {

            id:azienda.id

          })
          location.reload()

        },

        async savePEF(azienda)
        {
          this.$axios.post('/savePEF', {
            azienda:azienda.id,
            pef:azienda.pef_mis_o_ric
          })

          location.reload()
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
                    nome:"nome",
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
