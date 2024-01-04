
import Header from '../components/Header'
import PageTitle from '../components/PageTitle'
import Loading from '../components/Loading'
import Footer from '../components/Footer'



<template>
  <main>
    <Header/>
      <b-container class="mt-5" v-if="is_logged === true && is_company_set === true && loaded===true" >
        <b-row>
          <b-col v-bind:class="{'disabled-container' : azienda.report_is_sent || azienda.report_attempts <= 0 }" bg-variant="info" offset-xl="1" xl="10">
            <PageTitle name="Dati Azienda:"/>
            <b-container class="bg-light rounded p-3 mb-5">
              <b-row class="p-2">
                <b-col xl="3">
                  <b>Ragione Sociale:  </b>
                </b-col>
                <b-col xl="6">
                  {{azienda.ragione_sociale}}
                </b-col>
              </b-row>
              <b-row class="p-2">
                <b-col xl="3">
                  <b>Partita IVA: </b>
                </b-col>
                <b-col xl="6">
                  {{azienda.partita_iva}}
                </b-col>
              </b-row>
              <b-row class="p-2">
                <b-col xl="3">
                  <b>PEF:  </b>
                </b-col>
                <b-col xl="6">
                  {{azienda.pef_mis_o_ric}}
                </b-col>
              </b-row>
            </b-container>
            <PageTitle name="File Azienda:"/>
                <b-container disabled="true" class="bg-light rounded p-3 mb-5">
                  <b-row class="pb-4">
                    <b-col>
                      <p class="font-1">
                        In questa sezione è richiesto il file del <b>bilancio depositato</b> riferito all'anno 2022.<br>

                        Per quanto attiene i <b>CESPITI</b> l’utente deve scaricare e compilare il file excel che si intende riferito alla totalità dei beni impiegati nella conduzione degli appalti in tutti i Comuni, precisando per ogni bene le percentuali di impiego riferite a ciascun Comune (colonna S e successive).
                      </p>
                    </b-col>
                  </b-row>

                  <b-row class="p-2">
                    <b-col offset-xl="1" xl="4">
                      <p>Cespiti (<b-link href="/files/Ammortamenti_Cespiti.xlsx">Scarica Modello</b-link>)
                      </p>
                    </b-col>
                    <b-col cols="11" xl="5">
                      <p>
                        <b-form-file v-model="upload.cespiti"  placeholder="File Excel" drop-placeholder="Rilascia qui"></b-form-file>
                        <font v-if="azienda.cespiti != ''">
                          {{azienda.cespiti}}
                        </font>
                      </p>
                    </b-col>
                    <b-col cols="1" xl="1" class="pt-2 p-0">
                      <b-icon v-if="azienda.cespiti !== '' || upload.cespiti.length != 0 " class="h4 p-0 b-0 m-0" variant="success" icon="check-circle-fill"></b-icon>
                      <b-icon v-if="azienda.cespiti === '' && upload.cespiti.length === 0" class="h4 p-0 b-0 m-0" variant="danger" icon="x-circle-fill"></b-icon>
                    </b-col>
                  </b-row>


                  <b-row class="p-2">
                    <b-col offset-xl="1" xl="4">
                      <p>
                        Bilancio Depositato 2022
                      </p>
                    </b-col>
                    <b-col cols="11" xl="5">
                      <p>
                        <b-form-file v-model="upload.bilancio_depositato_anno1" placeholder="File" drop-placeholder="Rilascia qui"></b-form-file>
                        <font v-if="azienda.bilancio_depositato_anno1 != '' ">
                          {{azienda.bilancio_depositato_anno1}}
                        </font>
                      </p>
                    </b-col>
                    <b-col cols="1" xl="1" class="pt-2 p-0">
                      <b-icon v-if="azienda.bilancio_depositato_anno1 !== '' || upload.bilancio_depositato_anno1.length != 0" class="h4 p-0 b-0 m-0" variant="success" icon="check-circle-fill"></b-icon>
                      <b-icon v-if="azienda.bilancio_depositato_anno1 === '' && upload.bilancio_depositato_anno1.length === 0" class="h4 p-0 b-0 m-0" variant="danger" icon="x-circle-fill"></b-icon>
                    </b-col>
                  </b-row>

                  <b-row class="p-2">
                    <b-col offset-xl="10" xl="2">
                      <p>
                        <b-button @click="updateFiles(upload)" variant="infowaste" block> Salva </b-button>
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
                      <b-col xl="3" sm="12" class="mt-1 mb-1 rounded">
                        <h6>Regione</h6>
                      </b-col>

                      <b-col xl="3" sm="12" class="mt-1 mb-1 rounded">
                        <h6>Provincia</h6>
                      </b-col>

                      <b-col xl="4" sm="12" class="mt-1 mb-1 rounded">
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
          <Footer :visible="loaded"/>


          <b-container v-if="loaded === false" >
            <Loading/>
          </b-container>

          <b-container v-show="is_logged === false && is_company_set === false && loaded === true" class="mb-3">
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

          <b-container v-show="is_logged === true && is_company_set === false && loaded === true" class="mb-3">
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

    methods:
    {

        async updateFiles(azienda)
        {
            var formData = new FormData();
            var upload = false

            if(azienda.cespiti == '[object File]')
            {
              upload = true
              azienda.cespiti = new File([azienda.cespiti],azienda.cespiti.name)
              formData.append("cespiti", azienda.cespiti,azienda.cespiti.name);
            }
            if(azienda.bilancio_depositato_anno1 == '[object File]')
            {
              upload = true

              azienda.bilancio_depositato_anno1 = new File([azienda.bilancio_depositato_anno1],azienda.bilancio_depositato_anno1.name)
              formData.append("bilancio_depositato_anno1", azienda.bilancio_depositato_anno1,azienda.bilancio_depositato_anno1.name);
            }
            if(azienda.bilancio_depositato_anno2 == '[object File]')
            {
              upload = true
              azienda.bilancio_depositato_anno2 = new File([azienda.bilancio_depositato_anno2],azienda.bilancio_depositato_anno2.name)
              formData.append("bilancio_depositato_anno2", azienda.bilancio_depositato_anno2,azienda.bilancio_depositato_anno2.name);
            }
            if (upload)
            {
              this.$axios.post('/upload_company_files', formData, {
                   headers: {
                     'Content-Type': "multipart/form-data; charset='utf-8';",

                   },
              }).then((response) => {
                location.reload()
                })
            }else {
              location.reload()
            }

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
                })

                .then(function (response) {
                    console.log(response);
                    if(response.data == "OK")
                    {
                      window.location.reload()
                    }else {

                      alert(response.data)
                    }

                })
                .catch(function (error) {
                    console.log(error);
                });

              }
            },

            async delCom(comune_azienda) {
                  try {
                    this.$axios.post('/del_comune_azienda', {
                      comune_azienda: comune_azienda,

                    })
                    window.location.reload()

                  } catch (e) {
                    console.log(e);

                  }
                }



    },

    mounted()
    {

      try {

        this.loaded=false

        this.$axios.$get(`/is_logged`)
        .then((response) => {
          this.is_logged = response
          if (this.is_logged === true)
          {
            this.utente = this.$axios.$get(`/get_user_data`);
          }
          this.$axios.$get(`/role`)
            .then((response) => {
              this.role = response
              this.$axios.$get(`/is_company_set`)
                .then((response) => {
                  this.is_company_set = response
                  this.$axios.$get(`/comuni_italiani/elenco/regioni/`)
                  .then((response) => {
                    this.regioni_req = response
                    this.$axios.$get(`/comuni_italiani/elenco/province/regione/`+16)
                    .then((response) => {
                      this.province_req = response
                      this.$axios.$get(`/get_dati_comuni`)
                      .then((response) => {
                        this.comuni_azienda= response
                        this.$axios.$get(`/get_company_data`)
                        .then((response) => {
                          this.azienda = response
                          this.loaded = true
                        })
                      })
                    })
                  })
                })
              })
            })

      } catch (e) {

        console.log(e)

      }

    },

    data() {
      return {
        regioni_req: [] ,province_req: [] , comuni_req: [] ,
        comuni_azienda: [] ,
        azienda:[],
        utente:[],
        is_logged:undefined,
        is_company_set:undefined,
        role:'Normal',
        loaded:false,
        upload:
        {
          cespiti:[],
          bilancio_depositato_anno1:[],
          bilancio_depositato_anno2:[],
        },
        luogo: {
                 reg: '16',
                 prov: '0',
                 com: '0',
               },
      }
    }
  }
  </script>
