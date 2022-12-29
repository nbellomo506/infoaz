
import Header from '../components/Header'
import PageTitle from '../components/PageTitle'
import TownSelect from '../components/TownSelect'



<template>
  <main>
    <Header/>
      <b-container class="mt-5">
        <b-row>
          <b-col bg-variant="info" offset-xl="1" xl="10">

            <PageTitle name="Dati Azienda" description="I campi in rosso sono obbligatori"/>

                <b-container class="bg-light rounded p-3">

                  <b-row>
                    <b-col>
                      <h2>File Azienda:</h2>
                    </b-col>
                  </b-row>

                  <b-row class="pb-4">
                    <b-col>
                      <p>
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                      </p>
                    </b-col>
                  </b-row>

                  <b-row class="p-2">
                    <b-col offset-xl="1" xl="4">
                      <p>Ammortamenti (<b-link href="/files/Ammortamenti.xlsx">Scarica Modello</b-link>)
                      </p>
                    </b-col>
                    <b-col xl="6">
                      <p>
                        <b-form-file  placeholder="File Excel" drop-placeholder="Rilascia qui"></b-form-file>
                      </p>
                    </b-col>
                  </b-row>

                  <b-row class="p-2">
                    <b-col offset-xl="1" xl="4">
                      <p>
                        Bilancio Depositato 2020
                      </p>
                    </b-col>
                    <b-col xl="6">
                      <p>
                        <b-form-file  placeholder="File" drop-placeholder="Rilascia qui"></b-form-file>
                      </p>
                    </b-col>
                  </b-row>

                  <b-row class="p-2">
                    <b-col offset-xl="1" xl="4">
                      <p>
                        Bilancio Depositato 2021
                      </p>
                    </b-col>
                    <b-col xl="6">
                      <p>
                        <b-form-file  placeholder="File" drop-placeholder="Rilascia qui"></b-form-file>
                      </p>
                    </b-col>
                  </b-row>

                  <b-row class="p-2">
                    <b-col offset-xl="9" xl="2">
                      <p>
                        <b-button variant="info" block> Salva </b-button>
                      </p>
                    </b-col>
                  </b-row>

                  <b-row>
                    <b-col>
                      <h2>Comuni su cui opera l'azienda:</h2>
                    </b-col>
                  </b-row>

                  <b-row class="mt-2 mb-4">
                    <b-col xl="3" sm="12" class="mt-1 mb-1">
                      <b-select block v-for="regioni in regioni_req"  v-model="luogo.reg" v-if="typeof regioni === 'object'" @change=updateReg(luogo.reg)>
                        <option v-for="regione in regioni"  :value="regione.codice_regione" >
                           {{ regione.name }}
                        </option>
                      </b-select>
                    </b-col>
                    <b-col xl="3" sm="12" class="mt-1 mb-1">
                      <b-select block v-for="province in province_req" v-model="luogo.prov" v-if="typeof province === 'object'" @change=updateProv(luogo.prov)>
                        <option  v-for="provincia in province"  :value="provincia.codice_provincia">
                            {{ provincia.name }}
                        </option>
                      </b-select>
                    </b-col>
                    <b-col xl="4" sm="12" class="mt-1 mb-1">
                      <b-select block v-for="comuni in comuni_req" v-model="luogo.com" v-if="typeof comuni === 'object'">
                        <option v-for="comune in comuni" :value="comune.id">
                          {{ comune.name }}
                        </option>
                      </b-select>
                    </b-col>
                    <b-col xl="2" sm="6" class="mt-1 mb-1">
                      <b-button block variant="success" @click=addCom(luogo.com)>Aggiungi</b-button>
                    </b-col>
                  </b-row>

                  <b-row class="m-0 mt-2 mb-4">
                    <b-col xl="3" sm="12" class="mt-1 mb-1">
                      <h6>Regione</h6>
                    </b-col>

                    <b-col xl="3" sm="12" class="mt-1 mb-1">
                      <h6>Provincia</h6>
                    </b-col>

                    <b-col xl="4" sm="12" class="mt-1 mb-1">
                      <h6>Comune</h6>
                    </b-col>
                  </b-row>
                  <b-row class="m-0 mt-2 mb-4" v-for="comune_azienda,index in comuni_azienda" :key="comune_azienda">
                    <b-col xl="3" sm="12" class="mt-1 mb-1">
                    {{comune_azienda.nome_regione}}
                    </b-col>

                    <b-col xl="3" sm="12" class="mt-1 mb-1">
                     {{comune_azienda.nome_provincia}}
                    </b-col>

                    <b-col xl="4" sm="12" class="mt-1 mb-1">
                    {{comune_azienda.nome_comune}}
                    </b-col>
                    <b-col xl="2" sm="6">
                      <b-button block @click=delCom(comune_azienda.id) variant="danger">Elimina</b-button>
                    </b-col>
                  </b-row>

                </b-container>
              </b-col>
            </b-row>
          </b-container>
        </main>
      </template>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>

  <script>
  import axios from '@nuxtjs/axios'

  export default {
    async asyncData({ $axios, params })
      {
        try
        {
          let regioni_req = await $axios.$get(`/comuni_italiani/elenco/regioni/`);

          let comuni_azienda = await $axios.$get(`/dati_comuni/`);
          //let province_req = await $axios.$get(`/comuni_italiani/elenco/province/regione/`+1);
          //let comuni_req = await $axios.$get(`/comuni_italiani/elenco/comuni/provincia/`+1);
          return { regioni_req,comuni_azienda};
        }
              catch (e)
              {
                console.log(e);
                return { regioni_req: [],comuni_azienda:[]};


              }
        },


    methods:
    {


        async updateReg(reg)
        {
              let province_req = await this.$axios.$get(`/comuni_italiani/elenco/province/regione/`+reg);
              this.province_req = province_req
              this.comuni_req = 0
        },

        async updateProv(prov)
        {
              let comuni_req = await this.$axios.$get(`/comuni_italiani/elenco/comuni/provincia/`+prov);
              this.comuni_req = comuni_req
        },

        async addCom(comune)
        {
            if(comune > 0)
            {

                this.$axios.post('/dati_comuni/', {
                  azienda: 1,
                  comune: comune,
                  /*pef_mis_o_ric: "",
                  ris_ula_o_ore: "",
                  tot_app: 0,
                  app_servizi: 0,
                  app_rifiuti_diff: 0,
                  app_rifiuti_indiff: 0,
                  app_igiene: 0,
                  altri_gestori_flag: false,
                  altri_gestori: "",
                  appalto_attuale_data: "1970-01-01",
                  impresa_op_com_data: "1970-01-01",
                  valore_can: 0,
                  adeg_contr_flag: false,
                  ricavi_conai_flag: true,
                  impresa_cts_flag: false,
                  impresa_ctr_flag: true,
                  spazz_e_ig_flag: false,
                  serv_exra_arera_flag: true,
                  serv_exra_arera: "",
                  lav_in_corso_flag: false,
                  lav_in_corso: "",
                  var_gest_flag: false,
                  var_gest: "",
                  miglior_qual_flag: false,
                  miglior_qual: "",
                  costi_tqrif_flag: false,
                  costi_tqrif: 0*/
                })

                .then(function (response) {
                    console.log(response);
                })
                .catch(function (error) {
                    console.log(error);
                });

                window.location.reload()
                console.log("updated")
              }
            },

            async delCom(com) {
                  try {
                    await this.$axios.$delete(`/dati_comuni/${com}/`); // delete recipe
                    let newDatiComuni = await this.$axios.$get("/dati_comuni/"); // get new list of recipes
                    window.location.reload()

                  } catch (e) {
                    console.log(e);

                  }
                }



    },




    data() {
      return {
        regioni_req: [] ,province_req: [] , comuni_req: [] , comuni_azienda: [] ,
        az:
        {
          rag_soc:'',
          partita_iva:''
        },
        luogo: {
                 reg: '1',
                 prov: '1',
                 com: '1',
               },
      }
    }
  }
  </script>
