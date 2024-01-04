h
import Header from '../components/Header'
import PageTitle from '../components/PageTitle'
import FieldTitle from '../components/FieldTitle'
import Loading from '../components/Loading'
import Footer from '../components/Footer'



<template>
  <main>
    <Header/>
      <div class="p-0 m-0 b-0">
        <b-container class="pb-5" v-if="is_logged === true && role === 'Admin' && loaded===true">
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
                          <b-col class="p-1" xl="4">
                            <select class="w-100 custom-select" v-model="utente.azienda" :key="utente.email" >
                              <option :selected="utente.azienda === azienda.id" v-for="azienda in aziende" :key="azienda.id" :value="azienda.id">
                                  {{ azienda.ragione_sociale }}
                              </option>
                            </select>
                          </b-col>
                          <b-col class="p-1" xl="4">
                            <b-button block @click="assignAzienda(utente.id,utente.azienda)" variant="success" name="button">Salva</b-button>
                          </b-col>
                          <b-col class="p-1" xl="4">
                            <b-button block v-b-modal.confirmDeleteUser @click="setUsertoDelete(utente.id)" variant="danger" name="button">Elimina</b-button>
                          </b-col>
                          <b-modal id="confirmDeleteUser" title="Conferma" cancel-title="Annulla" cancel-variant="secondary" ok-variant="danger" @ok="deleteUser()" ok-title="Si">
                              Sei sicuro di voler cancellare l'utente e tutti i dati ad esso correlati?
                          </b-modal>
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
                          <b-col class="p-1" xl="4">
                            <select class="w-100 custom-select" v-model="utente.azienda" :key="utente.email" >
                              <option :selected="utente.azienda === azienda.id" v-for="azienda in aziende" :key="azienda.id" :value="azienda.id">
                                  {{azienda.ragione_sociale}}
                              </option>
                            </select>
                          </b-col>
                          <b-col class="p-1" xl="4">
                            <b-button block @click="assignAzienda(utente.id,utente.azienda)" variant="success" name="button">Cambia</b-button>
                          </b-col>
                          <b-col class="p-1" xl="4">
                            <b-button block @click="dissociateUser(utente.id,utente.azienda)" variant="danger" name="button">Dissocia</b-button>
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
                      {{azienda.ragione_sociale}}<br>
                      {{azienda.partita_iva}}
                    </b-col>
                    <b-col xl="4">
                      <b-form-radio-group v-model="azienda.pef_mis_o_ric" :options="pef_opts"></b-form-radio-group>
                    </b-col>
                    <b-col offset-xl="1" xl="2">
                      <b-button block @click="savePEF(azienda)" variant="success" name="button">Salva</b-button>
                    </b-col>
                    <b-col v-if="azienda.ragione_sociale !== 'infowaste'" xl="2">
                      <b-button block v-b-modal.confermaEliminaAzienda @click="setAziendaDaEliminare(azienda.id)" variant="danger" name="button">
                        <b-icon class="h4 p-0 b-0 m-0" variant="white" icon="trash"></b-icon>
                      </b-button>
                    </b-col>
                    <b-modal id="confermaEliminaAzienda" title="Conferma" cancel-title="Annulla" cancel-variant="secondary" ok-variant="danger" @ok="del_azienda()" ok-title="Si">
                        Sei sicuro di voler cancellare l'azienda e tutti i dati ad essa correlati?
                    </b-modal>
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
          <Footer :visible="loaded"/>

          <b-container v-if="loaded === false">
            <Loading/>
          </b-container>

          <b-container v-if="loaded === true && (is_logged === false || role==='Normal') " class="mb-3">
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


    mounted()
    {
      try {
        this.$axios.$get(`/is_logged`)
        .then((response) => {
          this.is_logged = response
          this.$axios.$get(`/role`)
          .then((response) => {
            this.role = response
            this.$axios.$get(`/get_utenti`)
            .then((response) => {
            this.utenti = response

                      for (var i = 0; i < this.utenti.length; i++)
                      {
                          var data = []
                          var orario = []

                            for (var j = 0; this.utenti[i].request_date[j] != 'T'; j++)
                            {
                              data[j] = this.utenti[i].request_date[j]
                            }

                            j++
                            var k = 0

                              while (j < this.utenti[i].request_date.length )
                              {
                                  if (this.utenti[i].request_date[j] == '+' || this.utenti[i].request_date[j] == '.' || this.utenti[i].request_date[j] == 'Z')
                                  {

                                    j = this.utenti[i].request_date.length
                                  }
                                      else
                                      {
                                        orario[k] = this.utenti[i].request_date[j]
                                      }
                                  j++
                                  k++
                              }

                          data = data.join('')
                          data.toString()

                          orario = orario.join('')
                          orario.toString()

                          this.utenti[i].data = data
                          this.utenti[i].orario = orario
                        }

                        for (var i = 0; i < this.utenti.length; i++)
                        {
                          if (this.utenti[i].azienda !== null && this.utenti[i].is_assigned === true)
                          {
                            this.utenti_azienda.push(this.utenti[i])
                          }
                            else
                                {
                                  this.utenti_non_azienda.push(this.utenti[i])
                                }
                        }
                        this.$axios.$get(`/get_aziende`)
                        .then((response) => {
                          this.aziende = response
                          this.loaded=true

                })
              })
            })
          })

      } catch (e) {
          console.log(e)
      }

    },

    methods:
    {

        orderUsers(by,assigned)
        {

            if (assigned)
            {
              this.utenti_azienda = this.utenti_azienda.sort((t1,t2) => t1[by] < t2[by] ? -1 : 1)
            }
            else {
              this.utenti_non_azienda = this.utenti_non_azienda.sort((t1,t2) => t1[by] < t2[by] ? -1 : 1)
            }

        },

        assignAzienda(user_id,azienda_id)
        {
          this.$axios.post('/assign_azienda', {
            user_id:user_id,
            azienda_id:azienda_id
          })
          .then((response) => {
            window.location.reload()
          })
        },

        deleteUser()
        {
          this.$axios.post('/deleteUser', {
            user_id:this.userToDelete,
          })
          .then((response) => {
            window.location.reload()
          })
        },

        dissociateUser(user_id,azienda_id)
        {
          this.$axios.post('/dissociateUser', {
            user_id:user_id,
            azienda_id:azienda_id
          })
          .then((response) => {
            window.location.reload()
          })
        },

        add_azienda(azienda)
        {
          if (azienda.ragione_sociale && azienda.partita_iva && azienda.pef_mis_o_ric)
          {

            this.$axios.post('/add_azienda', {

              ragione_sociale:azienda.ragione_sociale,
              partita_iva:azienda.partita_iva,
              pef_mis_o_ric:azienda.pef_mis_o_ric,

            })
            .then((response) => {
              window.location.reload()
            })
          }
        },

        del_azienda(azienda)
        {
          this.$axios.post('/del_azienda', {

            id:this.aziendaDaEliminare

          })
          .then((response) => {
            window.location.reload()
          })
        },

        setAziendaDaEliminare(azienda_id)
        {
          this.aziendaDaEliminare = azienda_id
        },

        setUsertoDelete(user)
        {
          this.userToDelete = user
        },

        savePEF(azienda)
        {
          this.$axios.post('/savePEF', {
            azienda:azienda.id,
            pef:azienda.pef_mis_o_ric
          })
          .then((response) => {
            window.location.reload()
          })
        }

    },


    data()
    {

        return {
                    utenti:[],
                    utenti_azienda:[],
                    utenti_non_azienda:[],
                    aziende:[],
                    aziendaDaEliminare:undefined,
                    userToDelete:undefined,
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
                    is_logged:undefined,
                    role:undefined,
                    loaded:false,

                }

            }


  };
  </script>
