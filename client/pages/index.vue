
import Header from '../components/Header'
import PageTitle from '../components/PageTitle'
import FieldTitle from '../components/FieldTitle'
import CostiSmaltimento from '../components/CostiSmaltimento'



<template>
  <main>
    <Header/>
      <div class="p-0 m-0 b-0">
        <b-container class="pb-5 ">
          <b-row>
            <b-col class="border-left border-bottom border-right rounded pt-5" offset-xl="1" xl="10">
              <PageTitle :name="`Comune di ${dati_comune.nome_comune}`" description="I campi in rosso sono obbligatori"/>
                <b-row>
                  <b-col :class="container_specs">
                    <FieldTitle num="" name="pef_mis_o_ric" description="PEF" req="yes"/>

                      <b-form-radio-group v-model="dati_comune.pef_mis_o_ric" :options="opts.tipo2">
                      </b-form-radio-group>
                  </b-col>
                </b-row>
                  <b-container class="p-0 m-0 b-0" name="calc_o_mis" v-show="dati_comune.pef_mis_o_ric === 'MISURATO'">
                    <hr>
                      <b-row>
                        <b-col :class="container_specs">
                        <FieldTitle num=""  name="ris_ula_o_ore" description="Per ciascuno dei servizi elencati, le risorse umane impiegate sono indicate in:" />
                            <b-form-radio-group v-model="dati_comune.ris_ula_o_ore" :options="opts.tipo3"></b-form-radio-group>
                        </b-col>
                      </b-row>
                      <b-row>
                        <b-col :class="container_specs">
                          <FieldTitle num=""  letter="a" name="tot_app" description="Totale per la conduzione dell'appalto" />
                          <input class="form-control" v-model="dati_comune.tot_app" type="number" >
                        </b-col>
                        <b-col :class="container_specs">
                          <FieldTitle num=""  letter="b" name="app_servizi" description="Di cui per impiegati e addetti ai servizi generali" />
                          <input class="form-control" v-model="dati_comune.app_servizi" type="number">
                        </b-col>
                      </b-row>
                      <b-row>
                        <b-col :class="container_specs">
                          <FieldTitle num=""  letter="c" name="app_rifiuti_diff" description="Di cui per addetti alla raccolta e trasporto dei rifiuti differenziati" />
                          <input class="form-control" v-model="dati_comune.app_rifiuti_diff" type="number">
                        </b-col>
                        <b-col :class="container_specs">
                          <FieldTitle num=""  letter="d" name="app_rifiuti_indiff" description="Di cui per addetti alla raccolta e trasporto dei rifiuti indifferenziati" />
                          <input class="form-control" v-model="dati_comune.app_rifiuti_indiff" type="number">
                        </b-col>
                      </b-row>
                      <b-row>
                        <b-col :class="container_specs" xl="12">
                          <FieldTitle num=""  letter="e"  name="app_igiene" description="Di cui per addetti ai servizi di spazzamento e igiene urbana" />
                          <input class="form-control" v-model="dati_comune.app_igiene" type="number">
                        </b-col>
                      </b-row>
                    <hr>
                  </b-container>

                    <b-row>
                      <b-col :class="container_specs">
                        <FieldTitle num=""  name="altri_gestori_flag" req="yes" description="Oltre al Comune e all'impresa operano altri Gestori nel medesimo Comune / Ambito Tariffario?" />
                        <b-form-radio-group v-model="dati_comune.altri_gestori_flag" :options="opts.tipo1"></b-form-radio-group>
                      </b-col>
                      <b-col :class="container_specs" v-show="dati_comune.altri_gestori_flag === true" >
                        <FieldTitle num=""  letter="a" name="altri_gestori"  description="Per quali servizi operano gli altri Gestori" />
                        <input class="form-control" v-model="dati_comune.altri_gestori" type="text">
                      </b-col>
                    </b-row>

                    <b-row>
                      <b-col :class="container_specs">
                        <FieldTitle num=""   name="appalto_attuale_data" description="L'appalto con la configurazione attuale è stato avviato il" />
                        <input class="form-control" v-model="dati_comune.appalto_attuale_data" type="date">
                      </b-col>

                      <b-col :class="container_specs">
                        <FieldTitle num=""   name="impresa_op_com_data" description="L'impresa opera nel Comune / Ambito Tariffario da" />
                        <input class="form-control" v-model="dati_comune.impresa_op_com_data" type="date">
                      </b-col>
                    </b-row>

                    <b-row>
                      <b-col :class="container_specs">
                        <FieldTitle num=""   name="valore_can" description="Valore del canone contrattuale IVA ESCLUSA nell'anno corrente" />
                        <input class="form-control" v-model="dati_comune.valore_can" type="number">

                      </b-col>

                      <b-col :class="container_specs">
                        <FieldTitle num=""   name="adeg_contr_flag" description="E' previsto l'adeguamento contrattuale del canone su base annua?" />
                        <b-form-radio-group v-model="dati_comune.adeg_contr_flag" :options="opts.tipo1"></b-form-radio-group>
                      </b-col>
                    </b-row>

                    <b-row>
                      <b-col :class="container_specs" xl="12">
                        <FieldTitle num=""   name="ricavi_conai_flag" description="I ricavi dai sistemi di compliance (ricavi CONAI e altri) competono all'impresa o al Comune?" />
                        <b-form-radio-group v-model="dati_comune.ricavi_conai_flag" :options="opts.tipo1"></b-form-radio-group>
                      </b-col>
                    </b-row>

                    <b-row>
                      <b-col :class="container_specs" xl="12">
                        <FieldTitle num=""  name="impresa_cts_flag" description="L'impresa sostiene costi CTS relativi al Trattamento e Smaltimento Rifiuti?" />
                        <b-form-radio-group v-model="dati_comune.impresa_cts_flag" :options="opts.tipo1"></b-form-radio-group>
                      </b-col>
                    </b-row>

                    <b-row>
                      <b-col :class="container_specs" xl="12">
                        <FieldTitle num=""  name="impresa_ctr_flag" description="L'impresa sostiene costi CTR relativi al Trattamento e Riciclo  Rifiuti?" />
                        <b-form-radio-group v-model="dati_comune.impresa_ctr_flag" :options="opts.tipo1"></b-form-radio-group>
                      </b-col>
                    </b-row>

                    <b-row>
                      <b-col :class="container_specs" xl="12">
                        <FieldTitle num=""   name="" description="Sono inclusi nel contratto e a carico dell'impresa anche i servizi di spazzamento e igiene ambientale?" />
                        <b-form-radio-group v-model="dati_comune.spazz_e_ig_flag" :options="opts.tipo1"></b-form-radio-group>

                      </b-col>
                    </b-row>

                    <b-row>
                      <b-col :class="container_specs">
                        <FieldTitle num=""   name="serv_exra_arera_flag" description="Sono presenti nel contratto anche servizi non inseriti del perimetro definito da ARERA?" />
                        <b-form-radio-group v-model="dati_comune.serv_exra_arera_flag" :options="opts.tipo1"></b-form-radio-group>
                      </b-col>
                      <b-col :class="container_specs" v-show="dati_comune.serv_exra_arera_flag == true">
                        <FieldTitle num=""  letter="a" name="serv_exra_arera" description="Servizi non inseriti nel perimetro" />
                        <input class="form-control" v-model="dati_comune.serv_exra_arera" >
                      </b-col>
                    </b-row>

                    <b-row>
                      <b-col :class="container_specs">
                        <FieldTitle num=""   name="" description="L'impresa ha in essere 'lavori in corso' per come definiti da ARERA?" />
                        <b-form-radio-group v-model="dati_comune.lav_in_corso_flag" :options="opts.tipo1"></b-form-radio-group>
                      </b-col>
                      <b-col :class="container_specs" >
                        <div v-show="dati_comune.lav_in_corso_flag == true">
                          <FieldTitle num=""  letter="a" name="" description="Descrizione dei lavori in corso" />
                          <input class="form-control" v-model="dati_comune.lav_in_corso" >
                        </div>
                      </b-col>
                    </b-row>

                    <b-row>
                      <b-col :class="container_specs">
                        <FieldTitle num=""   name="" description="Sono previste varizioni nelle attività gestionali?" />
                        <b-form-radio-group v-model="dati_comune.var_gest_flag" :options="opts.tipo1"></b-form-radio-group>
                      </b-col>
                      <b-col :class="container_specs" >
                        <div v-show="dati_comune.var_gest_flag == true">
                          <FieldTitle num=""  letter="a" name="" description="Descrizione delle variazioni nella attività gestionali" />
                          <input class="form-control" v-model="dati_comune.var_gest" >
                        </div>
                      </b-col>
                    </b-row>

                    <b-row>
                      <b-col :class="container_specs">
                        <FieldTitle num=""   name="miglior_qual_flag" description="Sono previsti miglioramenti nei livelli di qualità?" />
                        <b-form-radio-group v-model="dati_comune.miglior_qual_flag" :options="opts.tipo1"></b-form-radio-group>
                      </b-col>
                      <b-col :class="container_specs">
                        <div v-show="dati_comune.miglior_qual_flag == true">
                          <FieldTitle num=""  letter="a" name="miglior_qual" description="Descrizione dei miglioramenti previsti" />
                          <input class="form-control" v-model="dati_comune.miglior_qual" >
                        </div>

                      </b-col>
                    </b-row>

                    <b-row>
                      <b-col :class="container_specs">
                        <FieldTitle num=""   name="costi_tqrif_flag" description="Sono previsti maggiori costi per la implementazione del TQRIF?" />
                        <b-form-radio-group v-model="dati_comune.costi_tqrif_flag" :options="opts.tipo1"></b-form-radio-group>
                      </b-col>

                      <b-col :class="container_specs">
                        <div v-show="dati_comune.costi_tqrif_flag == true">
                          <FieldTitle num=""  letter="a" name="costi_tqrif" description="Importo dei costi previsti per il TQRIF" />
                          <input class="form-control" v-model="dati_comune.costi_tqrif"   type="number">
                        </div>

                      </b-col>
                    </b-row>

                  <b-container class="m-0 p-0 b-0">
                    <hr>
                    <h3>Dati tecnici dell'appalto</h3>
                    <b-row>
                      <b-col :class="container_specs" xl="12">
                        <FieldTitle num=""  req="yes" name="tons" description="Quantitativi totali rifiuti raccolti [ton]" />
                      </b-col>
                    </b-row>
                    <b-row>
                      <b-col xl="4" >
                        <FieldTitle num=""  letter="a" req="yes" name="" description="2020" />
                        <input class="form-control" v-model="dati_comune.ton_anno_1" type="number">
                      </b-col>
                      <b-col xl="4">
                        <FieldTitle num=""  letter="b" req="yes" name="" description="2021" />
                        <input class="form-control" v-model="dati_comune.ton_anno_2" type="number">
                      </b-col>
                      <b-col xl="4">
                        <FieldTitle num=""  letter="c" req="yes" name="" description="2022" />
                        <input class="form-control" v-model="dati_comune.ton_anno_3" type="number">
                      </b-col>
                    </b-row>
                  </b-container>
                  <hr>
                  <b-container class="m-0 mt-4 p-0 b-0">
                    <b-row>
                      <b-col :class="container_specs" xl="12">
                        <FieldTitle num=""   name="tons" req="yes" description="Percentuali raccolta differenziata" />
                      </b-col>
                    </b-row>
                    <b-row>
                      <b-col xl="4" >
                        <FieldTitle num=""  letter="a" req="yes" name="" description="2020" />
                        <input class="form-control" v-model="dati_comune.xcent_raccolta_anno_1" type="number">
                      </b-col>
                      <b-col xl="4">
                        <FieldTitle num=""  letter="b" req="yes" name="" description="2021" />
                        <input class="form-control" v-model="dati_comune.xcent_raccolta_anno_2" type="number">
                      </b-col>
                      <b-col xl="4">
                        <FieldTitle num=""  letter="c" req="yes" name="" description="2022" />
                        <input class="form-control" v-model="dati_comune.xcent_raccolta_anno_3" type="number">
                      </b-col>
                    </b-row>
                  </b-container>
                  <hr>
                    <b-row>
                      <b-col :class="container_specs" xl="12">
                        <FieldTitle num=""  name="tons" req="yes" description="Percentuali media delle impurità riscontrate nell'ultima annualità nelle frazioni differenziate" />
                        <input  class="form-control" v-model="dati_comune.xcent_media_imp" type="number">
                      </b-col>
                    </b-row>

                    <b-row>
                      <b-col xl="3" class="mt-4 pl-3 pr-3">
                        <FieldTitle num=""  letter="a" req="yes" name="" description="Rifiuti organici" />
                        <input class="form-control" v-model="dati_comune.xcent_media_imp_org" type="number">
                      </b-col>
                      <b-col xl="3" class="mt-4 pl-3 pr-3">
                        <FieldTitle num=""  letter="b" req="yes" name="" description="Carta e cartone" />
                        <input class="form-control" v-model="dati_comune.xcent_media_imp_cart" type="number">
                      </b-col>

                    <b-col xl="6">
                      <b-container class="m-0 p-0 b-0">
                        <b-row class="m-0 p-0 b-0">
                          <b-col offset-xl="4" xl="4">
                            <b>Imballaggi</b>
                          </b-col>
                        </b-row>

                        <b-row class="m-0 p-0 b-0">
                          <b-col xl="4" class="p-0 pr-2">
                            <FieldTitle num=""  letter="c" req="yes" name="" description="Plastica" />
                            <input class="form-control" v-model="dati_comune.xcent_media_imp_plastica" type="number">
                          </b-col>
                          <b-col xl="4" class="p-0 pr-2">
                            <FieldTitle num=""  letter="d" req="yes" name="" description="Metallo" />
                            <input class="form-control" v-model="dati_comune.xcent_media_imp_metallo" type="percent">
                          </b-col>
                          <b-col xl="4" class="p-0 pr-2">
                            <FieldTitle num=""  letter="e" req="yes" name="" description="Vetro" />
                            <input class="form-control" v-model="dati_comune.xcent_media_imp_vetro" type="number">
                          </b-col>
                        </b-row>
                      </b-container>
                    </b-col>

                    </b-row>
                    <hr>

                  <b-container class="m-0 mt-4 p-0 b-0">
                    <h3>Documenti riferiti all'appalto</h3>
                    <b-row>
                      <b-col :class="container_specs">
                        <FieldTitle num=""  req="yes"  name="" description="Contabilità di commessa anno 2020 (in excel)" />
                        <b-form-file
                          v-model="file1"
                          :state="Boolean(file1)"
                          placeholder="File Excel"
                          drop-placeholder="Rilascia qui..."
                        ></b-form-file>
                      </b-col>

                      <b-col :class="container_specs">
                        <FieldTitle num=""  req="yes" name="" description="Contabilità di commessa anno 2021 (in excel)" />
                        <b-form-file
                          v-model="file2"
                          :state="Boolean(file2)"
                          placeholder="File Excel"
                          drop-placeholder="Rilascia qui..."
                        ></b-form-file>

                      </b-col>
                    </b-row>

                    <b-row>
                      <b-col :class="container_specs">
                        <FieldTitle num=""  req="yes" name="" description="Contratto d'appalto vigente" />
                        <b-form-file
                          v-model="file3"
                          :state="Boolean(file3)"
                          placeholder="File PDF"
                          drop-placeholder="Rilascia qui..."
                        ></b-form-file>
                      </b-col>
                      <b-col :class="container_specs">
                        <FieldTitle num=""  req="yes" name="" description="Ultimo PEF validato dall'ETC (Delibera + Relazione con allegati in file .zip)" />
                        <b-form-file
                          v-model="file4"
                          :state="Boolean(file4)"
                          placeholder="File .zip"
                          drop-placeholder="Rilascia qui..."
                        ></b-form-file>
                      </b-col>
                    </b-row>
                  </b-container>

                    <!--
                    <b-row>
                      <b-col :class="container_specs">
                        <FieldTitle num=""   name="" description="" />
                      </b-col>
                    </b-row>

                    <b-row>
                      <b-col :class="container_specs">
                        <FieldTitle num=""   name="" description="" />
                      </b-col>
                    </b-row> -->


            </b-col>
          </b-row>
        </b-container>

        <b-container fluid style="width:1400px" class="border-rounded mb-5 pb-5">
          <h3>Costi Smaltimento / Trattamento</h3>
          <b-row>

            <b-col xl="1">
              Anno
            </b-col>

            <b-col xl="2">
              Impianto di smaltimento
            </b-col>

            <b-col xl="2">
              Codice CER/Tipo di rifiuto
            </b-col>

            <b-col xl="1">
              Tipologia costo
            </b-col>

            <b-col xl="1">
              Quantitativi conferiti [ton]
            </b-col>

            <b-col xl="2">
            Prezzo unitario con IVA
            </b-col>

            <b-col xl="2">
            Importo IVA Inclusa
            </b-col>
          </b-row>

          <b-row class="bg-light p-3">
            <b-col class="p-0 pl-1" xl="1">
              <select class="form-control" v-model="add.anno">
                <option value="2020">2020</option>
                <option value="2021">2021</option>
              </select>
            </b-col>

            <b-col xl="2">
              <textarea class="form-control" v-model="add.imp_smalt" ></textarea>
              <b-alert class="mt-2" v-if="add.msg.imp_smalt.length > 0" variant="danger" dismissible show> {{add.msg.imp_smalt}} </b-alert>

            </b-col>

            <b-col xl="2">
              <textarea class="form-control" v-model="add.tipo_rifiuto" ></textarea>
              <b-alert class="mt-2" v-if="add.msg.tipo_rifiuto.length > 0" variant="danger" dismissible show> {{add.msg.tipo_rifiuto}} </b-alert>

            </b-col>

            <b-col class="p-0 pl-1" xl="1">
              <select class="form-control" v-model="add.tipo_costo" >
                <option value="CTS">CTS</option>
                <option value="CTR">CTR</option>
              </select>
            </b-col>

            <b-col xl="1">
              <input class="form-control" min="0" @change=calcoloImporto() v-model="add.tons" type="number">
            </b-col>

            <b-col xl="2">
              <input class="form-control" min="0" @change=calcoloImporto() v-model="add.prezzo_unitario" type="number">
            </b-col>

            <b-col xl="2">
              <input class="form-control" min="0" v-model="add.importo" type="number">
            </b-col>

            <b-col xl="1">
              <b-button @click="aggiungiExtra()" variant="infowaste-2" name="button">
                Aggiungi
              </b-button>
            </b-col>

          </b-row>


          <b-row class="border rounded p-3"  v-for="(extra,index) in costi_smaltimento" v-bind:class = "(index % 2==0)?'bg-white':'bg-light'" :key="extra.id">
            <b-col class="p-0 pl-1" xl="1">
              <select class="form-control" v-model="extra.anno">
                <option value="2020">2020</option>
                <option value="2021">2021</option>
              </select>
            </b-col>

            <b-col xl="2">
              <textarea class="form-control" v-model="extra.imp_smalt">{{extra.imp_smalt}}</textarea>
            </b-col>

            <b-col xl="2">
              <textarea class="form-control" v-model="extra.tipo_rifiuto">{{extra.tipo_rifiuto}}</textarea>
            </b-col>

            <b-col class="p-0 pr-1" xl="1">
              <select class="form-control" v-model="extra.tipo_costo" >
                <option value="CTS">CTS</option>
                <option value="CTR">CTR</option>
              </select>
            </b-col>

            <b-col xl="1">
              <input class="form-control" min="0" type="number" @change="extra.importo = extra.tons * extra.prezzo_unitario" v-model="extra.tons">
            </b-col>

            <b-col xl="2">
              <b-input class="form-control" min="0" type="number" @change="extra.importo = extra.tons * extra.prezzo_unitario" v-model="extra.prezzo_unitario"></b-input>
            </b-col>

            <b-col xl="2">
              <input class="form-control" min="0" type="number" v-model="extra.importo">
            </b-col>

            <b-col xl="1">
              <b-container class="pr-2 mb-5">
                <b-row>
                  <b-col xl="5 p-0">
                    <button type="button" @click=modificaExtra(extra) class="btn btn-success" name="button">
                      <b-icon icon="save"></b-icon>
                    </button>

                  </b-col>
                  <b-col class="offset-xl-2 p-0" xl="5">
                    <button type="button" @click=eliminaExtra(extra.id) class="btn btn-danger" name="button">
                      <b-icon icon="trash"></b-icon>
                    </button>
                  </b-col>
                </b-row>
              </b-container>
            </b-col>
          </b-row>
        </b-container>
      </div>





        <div class="bg-light fixed-bottom p-2">
          <b-container class="container">
            <b-row class="row">
              <b-col class="col-2">
                <b-button to="../../home" block variant="infowaste">
                    Indietro
                </b-button>
              </b-col>

              <b-col class="col-1 offset-4">
                <b-button v-b-modal="'help-tab'" block variant="link">
                    Help
                </b-button>
              </b-col>

              <b-col class="col-1 offset-4">
                <b-button block @click="saveDatiComune(dati_comune)" variant="infowaste">
                    Salva
                </b-button>
              </b-col>
            </b-row>
          </b-container>
        </div>


        <!-- The modal -->
        <b-modal id="help-tab" cancel-title="Annulla" ok-title="Invia">
          <h5>Messaggio</h5>
          <b-form-input></b-form-input>
        </b-modal>

      </main>
  </template>

  <script id="xlsx" src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>

  <script>
  import axios from 'axios'
  //import xlsx from 'xlsx';

  export default {


    async asyncData({ $axios, params })
    {

        try {
          let dati_comune = await $axios.$get(`/dati_comuni/` + params.id);
          let costi_smaltimento = await $axios.$get(`/costi_smaltimento/?daticomune=` + params.id);

          return { dati_comune , costi_smaltimento};
        } catch (e) {

          return {
            dati_comune: [],costi_smaltimento:[]
            };
          }

    },


    methods:
    {
        exportExcel()
        {
          var XLSX = require("xlsx")
          console.log(XLSX)
          alert(XLSX)

          const workbook = XLSX.utils.book_new()
          const worksheet = XLSX.utils.json_to_sheet(this.dati_comune)

          XLSX.utils.book_append_sheet(workbook, worksheet, "Dati Comune")
          XLSX.writeFile(workbook, "aa.xlsx")
        },

        aggiungiExtra()
        {

            if(this.add.imp_smalt == "")
            {
              this.add.msg.imp_smalt = "Campo obbligatorio"
            }else {
              this.add.msg.imp_smalt = ""

            }

            if(this.add.tipo_rifiuto == "")
            {
              this.add.msg.tipo_rifiuto = "Campo obbligatorio"
            }else {
              this.add.msg.tipo_rifiuto = ""

            }

            if(this.add.tipo_rifiuto.length > 0 && this.add.imp_smalt.length > 0)
            {
                this.$axios.post('/costi_smaltimento/', {

                  daticomune:this.dati_comune.id,
                  imp_smalt: this.add.imp_smalt,
                  tipo_rifiuto: this.add.tipo_rifiuto,
                  tipo_costo: this.add.tipo_costo,
                  anno: this.add.anno,
                  tons: this.add.tons,
                  prezzo_unitario: this.add.prezzo_unitario,
                  importo: this.add.importo

                })
                location.reload();

            }


        },

        modificaExtra(extra)
        {

          this.$axios.put('/costi_smaltimento/'+extra.id+'/', {

            daticomune:this.dati_comune.id,
            imp_smalt: extra.imp_smalt,
            tipo_rifiuto: extra.tipo_rifiuto,
            tipo_costo: extra.tipo_costo,
            anno: extra.anno,
            tons: extra.tons,
            prezzo_unitario: extra.prezzo_unitario,
            importo: extra.importo,

          })
          //location.reload();

        },

        eliminaExtra(id)
        {
          this.$axios.delete('/costi_smaltimento/'+id, {})
          location.reload();

        },

        calcoloImporto()
        {
            this.add.importo = this.add.tons * this.add.prezzo_unitario
        },






        saveDatiComune(dati_comune)
        {

          this.exportExcel(dati_comune)


          if(dati_comune.altri_gestori_flag == false)
          {
            dati_comune.altri_gestori=""
          }

          if(dati_comune.serv_exra_arera_flag == false)
          {
            dati_comune.serv_exra_arera=""
          }

          if(dati_comune.lav_in_corso_flag == false)
          {
            dati_comune.lav_in_corso=""
          }

          if(dati_comune.var_gest_flag == false)
          {
            dati_comune.var_gest=""
          }

          if(dati_comune.miglior_qual_flag == false)
          {
            dati_comune.miglior_qual=""
          }


          this.$axios.put('/dati_comuni/'+this.dati_comune.id+'/', {

            pef_mis_o_ric: dati_comune.pef_mis_o_ric,
            ris_ula_o_ore: dati_comune.ris_ula_o_ore,
            tot_app: dati_comune.tot_app,
            app_servizi: dati_comune.app_servizi,
            app_rifiuti_diff:dati_comune.app_rifiuti_diff,
            app_rifiuti_indiff:dati_comune.app_rifiuti_indiff,
            app_igiene:dati_comune.app_igiene,
            altri_gestori_flag: dati_comune.altri_gestori_flag,
            altri_gestori: dati_comune.altri_gestori,
            appalto_attuale_data: dati_comune.appalto_attuale_data,
            impresa_op_com_data: dati_comune.impresa_op_com_data,
            valore_can: dati_comune.valore_can,
            adeg_contr_flag: dati_comune.adeg_contr_flag,
            ricavi_conai_flag: dati_comune.ricavi_conai_flag,
            impresa_cts_flag: dati_comune.impresa_cts_flag,
            impresa_ctr_flag: dati_comune.impresa_ctr_flag,
            spazz_e_ig_flag: dati_comune.spazz_e_ig_flag,
            serv_exra_arera_flag: dati_comune.serv_exra_arera_flag,
            serv_exra_arera: dati_comune.serv_exra_arera,
            lav_in_corso_flag: dati_comune.lav_in_corso_flag,
            lav_in_corso: dati_comune.lav_in_corso,
            var_gest_flag: dati_comune.var_gest_flag,
            var_gest: dati_comune.var_gest,
            miglior_qual_flag: dati_comune.miglior_qual_flag,
            miglior_qual: dati_comune.miglior_qual,
            costi_tqrif_flag: dati_comune.costi_tqrif_flag,
            costi_tqrif: dati_comune.costi_tqrif,
            ton_totali: dati_comune.ton_totali,
            ton_anno_1: dati_comune.ton_anno_1,
            ton_anno_2: dati_comune.ton_anno_2,
            ton_anno_3: dati_comune.ton_anno_3,
            xcent_raccolta_diff: dati_comune.xcent_raccolta_diff,
            xcent_raccolta_anno_1: dati_comune.xcent_raccolta_anno_1,
            xcent_raccolta_anno_2: dati_comune.xcent_raccolta_anno_2,
            xcent_raccolta_anno_3: dati_comune.xcent_raccolta_anno_3,
            xcent_media_imp: dati_comune.xcent_media_imp,
            xcent_media_imp_org: dati_comune.xcent_media_imp_org,
            xcent_media_imp_cart: dati_comune.xcent_media_imp_cart,
            xcent_media_imp_plastica: dati_comune.xcent_media_imp_plastica,
            xcent_media_imp_metallo: dati_comune.xcent_media_imp_metallo,
            xcent_media_imp_vetro: dati_comune.xcent_media_imp_vetro

          })

          .then(function (response) {
              console.log(response);
          })
          .catch(function (error) {
              console.log(error);
          });


        }
    },


    data() {

        return {
                  add:
                  {
                      imp_smalt:"",
                      tipo_rifiuto:"",
                      tipo_costo:"CTS",
                      anno:"2020",
                      tons:0,
                      prezzo_unitario:0,
                      importo:0,
                      msg:{

                        imp_smalt:"",
                        tipo_rifiuto:"",

                      }

                  },

                  container_specs:'col-xl-6 col-sm-12 p-2 pl-3 pr-3 mt-4 mb-4',
                  file1: null,
                  file2: null,
                  file3: null,
                  file4: null,
                  opts: {

                    tipo1:[
                      { text: 'Si', value: true },
                      { text: 'No', value: false }
                    ],

                    tipo2:[
                      { text: 'CALCOLATO', value: 'CALCOLATO' },
                      { text: 'MISURATO', value: 'MISURATO' }
                    ],

                    tipo3:[
                      { text: 'ULA', value: 'ULA' },
                      { text: 'ORE LAVORATE', value: 'ORE LAVORATE' }
                    ],

                  },
                  dim:6,
                }

            }


  };
  </script>
