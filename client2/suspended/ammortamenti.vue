
import Header from '../components/Header'
import PageTitle from '../components/PageTitle'
import TownSelect from '../components/TownSelect'



<template>
  <main>
    <Header/>
      <b-container class="mt-5">

        <b-row>
          <b-col bg-variant="info" offset-xl="1" xl="10">
            <PageTitle name="Ammortamenti" description="I campi in rosso sono obbligatori"/>

              <b-container class="bg-light rounded pt-3">
                <b-row :class="custom_row">
                  <b-col>
                      Gestore
                  </b-col>
                  <b-col>
                        <b-form-input v-model="add.amm.gestore" type="text" maxlength="4"></b-form-input>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                      Cespiti gestore/Cespiti Proprietari diversi dal gestore
                  </b-col>
                  <b-col>
                    <b-form-select>
                      <option  v-for="cesp in opts.cesps"  :value="cesp.value" >
                         {{ cesp.text }}
                      </option>
                    </b-form-select>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                      Categoria immobilizzazione
                  </b-col>

                  <b-col>
                    <b-form-select block v-model="imm_id" @change="updateCategImm(imm_id)">
                      <option  v-for="categ_imm in categ_imms"  :value="categ_imm.id" >
                         {{ categ_imm.testo }}
                      </option>
                    </b-form-select>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                    Categoria Cespiti Specifici
                  </b-col>
                  <b-col>
                    <b-form-select block>
                      <option  v-for="cesp_spec in cesp_specs"  :value="cesp_spec.testo">
                         {{ cesp_spec.testo }}
                      </option>
                    </b-form-select>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                      Anno Cespite
                  </b-col>
                  <b-col>
                      <b-form-input type="text" maxlength="4"></b-form-input>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                      Cic,t
                  </b-col>
                  <b-col>
                    <b-form-input type="text" maxlength="4"></b-form-input>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                      FACI,c,2017
                  </b-col>
                  <b-col>
                    <b-form-input type="text" maxlength="4"></b-form-input>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                      CFPc,t
                  </b-col>
                  <b-col>
                    <b-form-input type="text" maxlength="4"></b-form-input>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                      FACFP,c,2017
                  </b-col>
                  <b-col>
                    <b-form-input type="text" maxlength="4"></b-form-input>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                      Anno dismissioni
                  </b-col>
                  <b-col>
                      <b-form-input type="text" v-model="add.amm.anno_dimissioni" maxlength="4"></b-form-input>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col xl="2" offset-xl="10">
                    <b-button class="btn btn-success" @click="addAmm(add.amm)">Aggiungi</b-button>
                  </b-col>
                </b-row>
              </b-container>

              <b-container v-for="ammortamenti in ammortamenti_azienda" class="bg-light rounded pt-3 mt-5">
                <b-row :class="custom_row">
                  <b-col>
                      Gestore
                  </b-col>
                  <b-col>
                        <b-form-input type="text" v-model="ammortamenti.gestore" ></b-form-input>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                      Cespiti gestore/Cespiti Proprietari diversi dal gestore
                  </b-col>
                  <b-col>
                    <b-form-select>
                      <option v-for="cesp in opts.cesps"  :value="cesp.value" >
                         {{ cesp.text }}
                      </option>
                    </b-form-select>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                      Categoria immobilizzazione
                  </b-col>
                  <b-col>
                    <b-form-select block v-model="imm_id" @change="updateCategImm(imm_id)">
                      <option  v-for="categ_imm in categ_imms"  :value="categ_imm.id" >
                         {{ categ_imm.testo }}
                      </option>
                    </b-form-select>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                    Categoria Cespiti Specifici
                  </b-col>
                  <b-col>
                    <b-form-select block>
                      <option  v-for="cesp_spec in cesp_specs"  :value="cesp_spec.testo">
                         {{ cesp_spec.testo }}
                      </option>
                    </b-form-select>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                      Anno Cespite
                  </b-col>
                  <b-col>
                      <b-form-input type="text" v-model="ammortamenti.anno" maxlength="4"></b-form-input>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                      Cic,t
                  </b-col>
                  <b-col>
                    <b-form-input type="number" v-model="ammortamenti.cic" step="0.1" max="100"></b-form-input>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                      FACI,c,2017
                  </b-col>
                  <b-col>
                    <b-form-input type="number" v-model="ammortamenti.faci" step="0.1" max="100"></b-form-input>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                      CFPc,t
                  </b-col>
                  <b-col>
                    <b-form-input type="number" v-model="ammortamenti.cfp" step="0.1" max="100"></b-form-input>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                      FACFP,c,2017
                  </b-col>
                  <b-col>
                    <b-form-input type="number" v-model="ammortamenti.facfp" step="0.1" max="100"></b-form-input>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col>
                      Anno dismissioni
                  </b-col>
                  <b-col>
                      <b-form-input type="text" v-model="ammortamenti.anno_dimissioni" maxlength="4"></b-form-input>
                  </b-col>
                </b-row>
                <b-row :class="custom_row">
                  <b-col xl="2" offset-xl="8">
                    <b-button block class="btn btn-primary">Salva</b-button>
                  </b-col>
                  <b-col xl="2">
                    <b-button block class="btn btn-danger">Elimina</b-button>
                  </b-col>
                </b-row>
              </b-container>
            </b-col>
          </b-row>
        </b-container>

      </main>
    </template>

  <script>
  import axios from 'axios'

  export default {

    async asyncData({ $axios, params })
      {
        try
        {
          let categ_imms = await $axios.$get(`/categ_imm/`);
          let ammortamenti_azienda = await $axios.$get(`/ammortamenti/`);
          //let province_req = await $axios.$get(`/comuni_italiani/elenco/province/regione/`+1);
          //let comuni_req = await $axios.$get(`/comuni_italiani/elenco/comuni/provincia/`+1);
          return { categ_imms,ammortamenti_azienda};
        }
              catch (e)
              {

                return { categ_imms: [],ammortamenti_azienda: []};


              }
        },

    methods:
    {
        async updateCategImm(categ_imm_id)
        {
              let cesp_specs = await this.$axios.$get(`/categ_cesp_spec/?categ_imm=`+categ_imm_id);
              this.cesp_specs = cesp_specs

        },

        async addAmm(amm)
        {

                this.$axios.post('/ammortamenti/', {
                  azienda: 1,
                  gestore: amm.gestore,
                  tipo_cesp: amm.tipo_cesp,
                  categ_imm: amm.categ_imm,
                  cst_cesp_spec:amm.cst_cesp_spec,
                  anno: amm.anno,
                  cic:amm.cic,
                  faci: amm.faci,
                  cfp: amm.cfp,
                  facfp: amm.facfp,
                  anno_dimissioni: amm.anno_dimissioni
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

            },
    },

    data() {
      return {


        add:{

          amm:{

            gestore: "default",
            tipo_cesp: "",
            categ_imm: "",
            cst_cesp_spec:"",
            anno: "",
            cic:0,
            faci: 0,
            cfp: 0,
            facfp: 0,
            anno_dimissioni: 0

          },

        },
        custom_row:"pt-2 pb-2",
        categ_imms: [] ,
        ammortamenti_azienda: [] ,
        cesp_specs: [],

        opts:{

                cesps:[
                  {text:'Cespiti Gestore',value:'Cespiti Gestore'},
                  {text:'Cespiti proprietari diversi dal Gestore  - Proprietario 1',value:'Cespiti proprietari diversi dal Gestore  - Proprietario 1'},
                  {text:'Cespiti proprietari diversi dal Gestore  - Proprietario 2',value:'Cespiti proprietari diversi dal Gestore  - Proprietario 2'},
                  {text:'Cespiti proprietari diversi dal Gestore  - Proprietario 3',value:'Cespiti proprietari diversi dal Gestore  - Proprietario 3'},
                  {text:'Leasing',value:'Leasing'}
                ],


        },

      }
    }
  }
  </script>
