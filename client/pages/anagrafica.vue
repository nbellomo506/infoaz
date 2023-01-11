
import Header from '../components/Header'
import PageTitle from '../components/PageTitle'
import TownSelect from '../components/TownSelect'



<template>
  <main>
    <Header/>
      <b-container class="mt-5" v-if="is_logged === true && is_company_set === true" >
        <b-row>
          <b-col bg-variant="info" offset-xl="1" xl="10">
            <PageTitle name="Dati Azienda:"/>
            <b-container class="bg-light rounded p-3 mb-5">
              <b-row>
                <b-col class="border-top" xl="12">
                  <h6>PEF:</h6>{{azienda.pef_mis_o_ric}}
                </b-col>
                <b-col class="border-top" xl="12">
                  <h6>Ragione Sociale:</h6>{{azienda.ragione_sociale}}
                </b-col>
                <b-col class="border-top border-bottom" xl="12">
                  <h6>Partita IVA: </h6>{{azienda.partita_iva}}
                </b-col>
              </b-row>
            </b-container>

            <PageTitle name="File Azienda:"/>
                <b-container class="bg-light rounded p-3 mb-5">
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
                        <b-form-file v-model="azienda.ammortamenti"  placeholder="File Excel" drop-placeholder="Rilascia qui"></b-form-file>
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
                        <b-form-file v-model="azienda.bilancio_depositato_anno1" placeholder="File" drop-placeholder="Rilascia qui"></b-form-file>
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
                        <b-form-file v-model="azienda.bilancio_depositato_anno2" placeholder="File" drop-placeholder="Rilascia qui"></b-form-file>
                      </p>
                    </b-col>
                  </b-row>

                  <b-row class="p-2">
                    <b-col offset-xl="9" xl="2">
                      <p>
                        <b-button @click="updateFiles(azienda)" variant="info" block> Salva </b-button>
                      </p>
                    </b-col>
                  </b-row>
                </b-container>

                <PageTitle name="Comuni su cui opera l'azienda:"/>
                  <b-container class="bg-light rounded p-3 mb-5">
                    <b-row class="mt-2 mb-4">
                      <b-col xl="3" sm="12" class="mt-1 mb-1">
                        <b-select block v-model="luogo.reg" @change=updateReg(luogo.reg)>
                          <option v-for="regione in regioni_req.regioni" :key="regione.codice_regione" :value="regione.codice_regione" >
                             {{ regione.name }}
                          </option>
                        </b-select>
                      </b-col>
                      <b-col xl="3" sm="12" class="mt-1 mb-1">
                        <b-select block v-model="luogo.prov" @change=updateProv(luogo.prov)>
                          <option  v-for="provincia in province_req.province" :key="provincia.id" :value="provincia.codice_provincia">
                              {{ provincia.name }}
                          </option>
                        </b-select>
                      </b-col>
                      <b-col xl="4" sm="12" class="mt-1 mb-1">
                        <b-select block v-model="luogo.com" >
                          <option v-for="comune in comuni_req.comuni" :key="comune.id" :value="comune.id">
                              {{ comune.name }}
                          </option>
                        </b-select>
                      </b-col>
                      <b-col xl="2" sm="6" class="mt-1 mb-1">
                        <b-button block variant="success" @click=addCom(luogo.com)>Aggiungi</b-button>
                      </b-col>
                    </b-row>

                    <b-row class="m-0 mt-5 mb-4 ">
                      <b-col xl="3" sm="12" class="mt-1 mb-1 bg-white rounded">
                        <h6>Regione</h6>
                      </b-col>

                      <b-col xl="3" sm="12" class="mt-1 mb-1 bg-white rounded">
                        <h6>Provincia</h6>
                      </b-col>

                      <b-col xl="4" sm="12" class="mt-1 mb-1 bg-white rounded">
                        <h6>Comune</h6>
                      </b-col>
                    </b-row>
                    <b-row class="m-0 border rounded mt-2 mb-4" v-for="comune_azienda,index in comuni_azienda" :key="comune_azienda.id">
                      <b-col xl="3" sm="12" class="pt-2 border-right mt-1 mb-1">
                      {{comune_azienda.nome_regione}}
                      </b-col>

                      <b-col xl="3" sm="12" class="pt-2 border-right mt-1 mb-1">
                       {{comune_azienda.nome_provincia}}
                      </b-col>

                      <b-col xl="4" sm="12" class="pt-2 mt-1 mb-1">
                      {{comune_azienda.nome_comune}}
                      </b-col>
                      <b-col xl="2" sm="6" class="mt-1 mb-1 p-2">
                        <b-button block @click=delCom(comune_azienda.id) variant="danger">Elimina</b-button>
                      </b-col>
                    </b-row>
                  </b-container>




              </b-col>
            </b-row>
          </b-container>

          <b-container v-if="is_logged === false && is_company_set === false" class="mb-3">
            <b-row>
              <b-col offset-xl="1" xl="10">
                <b-container class="mb-3 mt-5">
                  <b-row>
                    <b-col xl="12">
                      <h1>Attenzione</h1>
                      <p>
                        <a href="./login">Accedi</a>
                        per visualizzare il contenuto
                      </p>
                    </b-col>
                  </b-row>
                </b-container>
              </b-col>
            </b-row>
          </b-container>

          <b-container v-if="is_logged === true && is_company_set === false" class="mb-3">
            <b-row>
              <b-col offset-xl="1" xl="10">
                <b-container class="mb-3 mt-5">
                  <b-row>
                    <b-col xl="12">
                      <h1>Attenzione</h1>
                      <p>
                        Ciao {{utente.nome}} , la tua richiesta di accesso è stata inviata ma i gestori non ti hanno ancora associato l'azienda.<br>
                        Pertanto non hai accesso ai dati inseriti dalla tua azienda

                      </p>
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
  import axios from 'axios'

  export default {
    async asyncData({ $axios, params })
      {

        try
        {
          $axios.defaults.withCredentials = true;

          let is_logged = await $axios.$get(`/is_logged`);
          let is_company_set = await $axios.$get(`/is_company_set`);
          let role = await $axios.$get(`/role`);
          let regioni_req = await $axios.$get(`/comuni_italiani/elenco/regioni/`);
          let province_req = await $axios.$get(`/comuni_italiani/elenco/province/regione/`+16);
          let comuni_azienda = await $axios.$get(`/get_dati_comuni`);
          let azienda = await $axios.$get(`/get_company_data`);

            if(is_logged)
            {
              var utente = await $axios.$get(`/get_user_data`);

            }

          return { is_logged,utente,is_company_set,role,regioni_req,province_req,comuni_azienda,azienda};
        }
              catch (e)
              {
                console.log(e);
                return {is_logged:false, regioni_req: [],province_req: [],comuni_req: [],comuni_azienda:[],azienda:[]};


              }
        },


    methods:
    {

        async updateFiles(azienda)
        {
            var formData = new FormData();
            azienda.ammortamenti = new File([azienda.ammortamenti],azienda.ammortamenti.name)
            azienda.bilancio_depositato_anno1 = new File([azienda.bilancio_depositato_anno1],azienda.bilancio_depositato_anno1.name)
            azienda.bilancio_depositato_anno2 = new File([azienda.bilancio_depositato_anno2],azienda.bilancio_depositato_anno2.name)

            formData.append("ammortamenti", azienda.ammortamenti,azienda.ammortamenti.name);
            formData.append("bilancio_depositato_anno1", azienda.bilancio_depositato_anno1,azienda.bilancio_depositato_anno1.name);
            formData.append("bilancio_depositato_anno2", azienda.bilancio_depositato_anno2,azienda.bilancio_depositato_anno2.name);

            this.$axios.put('aziende/1/', formData, {
                 headers: {
                   'Content-Type': "multipart/form-data; charset='utf-8';",

                 }
            })

        },

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

                this.$axios.post('/add_comune_azienda', {
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
        regioni_req: [] ,province_req: [] , comuni_req: [] ,
        comuni_azienda: [] ,
        is_logged:false,
        is_company_set:false,
        role:'Normal',


        luogo: {
                 reg: '16',
                 prov: '0',
                 com: '0',
               },
      }
    }
  }
  </script>
