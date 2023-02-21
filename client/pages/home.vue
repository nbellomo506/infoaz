
import Header from '../components/Header'





<template>
  <main>
    <Header/>
      <b-container v-if="is_logged === true && is_company_set === true"  class="mt-5 mb-5">
        <b-row>
          <b-col offset-xl="1" xl="10">
            <b-container class="mb-3">
              <b-row>
                <b-col xl="6">
                  <h1>Benvenut* {{utente.nome}}</h1>
                  <h3 v-if="azienda.report_is_sent === false && azienda.report_attempts > 0">Compilazione in corso</h3>
                  <h3 v-if="azienda.report_is_sent === true && azienda.report_attempts > 0">Report Inviato</h3>
                  <h3 class="text-danger" v-if="azienda.report_attempts <= 0">Report non modificabile</h3>
                </b-col>
                <b-col xl="6" class="border rounded">
                  <h3>Legenda</h3>
                  <b-container class="p-2 pb-4">
                    <b-row>
                      <b-col xl="6">
                        <hr>
                        <b-icon class="h4 p-0 b-0 m-0" variant="success" icon="check-circle-fill"></b-icon>
                        Completo
                      </b-col>
                      <b-col xl="6">
                        <hr>
                        <b-icon class="h4 p-0 b-0 m-0" variant="danger" icon="x-circle-fill"></b-icon>
                        Incompleto
                      </b-col>
                    </b-row>
                  </b-container>
                </b-col>
              </b-row>
            </b-container>



              <b-list-group vertical  v-bind:class="{'disabled-container' : azienda.report_attempts <= 0 }">
                <b-container  class="p-4 pl-1 rounded bg-light" >
                  <a href="anagrafica">
                      Anagrafica
                  </a>
                </b-container>
                <b-container class="p-4 pl-1 mt-2 rounded bg-light" v-for="(dati_comune,index) in dati_comuni" :key="dati_comune.id">
                  <b-row>
                    <b-col xl="11" cols="10">
                      <a :href="`/compila_dati_comune/${dati_comune.id}/`">
                          <b>{{index+1}}. </b>{{dati_comune.nome_comune}}
                      </a>
                    </b-col>
                    <b-col xl="1" cols="2">
                      <div v-if="dati_comune.completed == true">
                        <b-icon class="h4 p-0 b-0 m-0" variant="success" icon="check-circle-fill"></b-icon>
                      </div>
                      <div v-if="dati_comune.completed == false">
                        <b-icon class="h4 p-0 b-0 m-0" variant="danger" icon="x-circle-fill"></b-icon>
                      </div>
                    </b-col>
                  </b-row>
                </b-container>
              </b-list-group>
            </b-col>
          </b-row>

          <b-row class="mb-5">
            <b-col class="mt-4 " offset-xl="1" xl="10">
              <p class="font-1">
                <b>SUPPORTO PEF</b> è un servizio a disposizione delle imprese che operano nel settore della gestione dei rifiuti urbani per la compilazione del PEF (Piano Economico Finanziario) secondo le disposizioni di ARERA (MTR-2).<br>
                L’attività di compilazione e caricamento dei dati in piattaforma è preceduta da una fase di assessment condotta dai nostri tecnici in modo da definire lo scenario che può esser basato su <b>PEF CALCOLATO</b> (i driver attraverso cui ripartire i costi sono elaborati prendendo a riferimento valori il più possibile oggettivi) ovvero su <b>PEF MISURATO</b> (i driver sono individuati dall’utente sulla base di un set messo a disposizione dall’applicazione che li elabora attingendo dall’ERP aziendale <b>WMS / INNOVAMBIENTE</b>).<br>
                In entrambi i casi l’elaborazione fa riferimento ai dati di bilancio, alla contabilità di commessa e dati tecnici che dovranno essere caricati e imputati negli appositi campi dell’applicazione.<br>

                L’utente dopo essere accreditato compila la sezione <b>ANAGRAFICA</b> e dichiara i Comuni presso i quali opera con conseguente obbligo di presentazione del PEF.<br>

                Terminata questa fase, l’utente procede alla compilazione e caricamento dei dati per ogni Comune, scegliendolo fra quelli dichiarati e visibili nella HOMEPAGE.<br>

                Completata la fase di compilazione e caricamento dei dati Comune per Comune, è possibile segnalare il termine dell’attività premendo il pulsante <b>INVIA DATI</b>. L’opzione INVIA DATI è reversibile nel caso in cui sia necessario procedere ad ulteriori modiche ed aggiornamenti.<br>

                L’attività di consulenza e assistenza condotta dai nostri tecnici viene avviata al completamento dell’attività di caricamento e compilazione svolta dall’utente e quindi alla ricezione dell’input conferito attraverso il tasto INVIA DATI.<br>
              </p>
            </b-col>
          </b-row>
          <b-row>
            <b-col class="mb-5" bg-variant="info" offset-xl="7" xl="4">
              <b-button v-if="azienda.report_is_sent == false && azienda.report_attempts > 0" :disabled="!is_ready || azienda.report_attempts === 0" @click=inviaReport() block>
                Invia dati
              </b-button>
              <b-button v-if="azienda.report_is_sent == true && azienda.report_attempts > 0" @click="riprendiReport()" :disabled=" azienda.report_attempts === 0" block>
                Riprendi Elaborazione
              </b-button>
            </b-col>
          </b-row>
        </b-container>

        <b-container v-if="is_logged === false" class="mb-3">
          <b-row>
            <b-col offset-xl="1" xl="10">
              <b-container class="mb-3 mt-5">
                <b-row>
                  <b-col xl="12">

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
      <table v-for="(dati_comune,index) in dati_comuni" :id="`tab${index}`" border="1" hidden>
        <tr>
          <td>
            <h6>{{index+1}}. Comune:</h6>
          </td>
          <td>{{dati_comune.nome_comune}}</td>
        </tr>
        <tr align="center">
          <td colspan="2"><b>Dati Generali</b></td>
        </tr>
        <tr>
          <td>PEF</td>
          <td>{{azienda.pef_mis_o_ric}}</td>
        </tr>

        <tr>
          <td>Per ciascuno dei servizi elencati, le risorse umane impiegate sono indicate in:</td>
          <td>{{dati_comune.ris_ula_o_ore}}</td>
        </tr>

        <tr>
          <td>Totale per la conduzione dell'appalto</td>
          <td>{{dati_comune.tot_app}}</td>
        </tr>

        <tr>
          <td>Di cui per impiegati e addetti ai servizi generali</td>
          <td>{{dati_comune.app_servizi}}</td>
        </tr>

        <tr>
          <td>Di cui per addetti alla raccolta e trasporto dei rifiuti differenziati</td>
          <td>{{dati_comune.app_rifiuti_diff}}</td>
        </tr>

        <tr>
          <td>Di cui per addetti alla raccolta e trasporto dei rifiuti indifferenziati</td>
          <td>{{dati_comune.app_rifiuti_indiff}}</td>
        </tr>

        <tr>
          <td>Di cui per addetti ai servizi di spazzamento e igiene urbana</td>
          <td>{{dati_comune.app_igiene}}</td>
        </tr>

        <tr>
          <td>Oltre al Comune e all'impresa operano altri Gestori nel medesimo Comune / Ambito Tariffario?</td>
          <td>{{dati_comune.altri_gestori_flag}}</td>
          <td>{{dati_comune.altri_gestori}}</td>
        </tr>

        <tr>
          <td>L'appalto con la configurazione attuale è stato avviato il</td>
          <td>{{dati_comune.appalto_attuale_data}}</td>
        </tr>

        <tr>
          <td>L'impresa opera nel Comune / Ambito Tariffario da</td>
          <td>{{dati_comune.impresa_op_com_data}}</td>
        </tr>

        <tr>
          <td>Valore del canone contrattuale IVA ESCLUSA nell'anno corrente</td>
          <td>{{dati_comune.valore_can}}</td>
        </tr>

        <tr>
          <td>E' previsto l'adeguamento contrattuale del canone su base annua?</td>
          <td>{{dati_comune.adeg_contr_flag}}</td>
          <td>{{dati_comune.adeg_contr}}</td>
        </tr>

        <tr>
          <td>I ricavi dai sistemi di compliance (ricavi CONAI e altri) competono all'impresa o al Comune?</td>
          <td>{{dati_comune.ricavi_conai}}</td>
        </tr>

        <tr>
          <td>L'impresa sostiene costi CTS relativi al Trattamento e Smaltimento Rifiuti?</td>
          <td>{{dati_comune.impresa_cts_flag}}</td>
          <td>{{dati_comune.impresa_cts}}</td>
        </tr>

        <tr>
          <td>L'impresa sostiene costi CTR relativi al Trattamento e Riciclo Rifiuti?</td>
          <td>{{dati_comune.impresa_ctr_flag}}</td>
          <td>{{dati_comune.impresa_ctr}}</td>
        </tr>

        <tr>
          <td>Sono inclusi nel contratto e a carico dell'impresa anche i servizi di spazzamento e igiene ambientale?</td>
          <td>{{dati_comune.spazz_e_ig_flag}}</td>
          <td>{{dati_comune.spazz_e_ig}}</td>
        </tr>

        <tr>
          <td>Sono presenti nel contratto anche servizi non inseriti del perimetro definito da ARERA?</td>
          <td>{{dati_comune.serv_exra_arera}}</td>
        </tr>

        <tr>
          <td>L'impresa ha in essere 'lavori in corso' per come definiti da ARERA?</td>
          <td>{{dati_comune.lav_in_corso}}</td>
        </tr>

        <tr>
          <td>Sono previste varizioni nelle attività gestionali?</td>
          <td>{{dati_comune.var_gest}}</td>
        </tr>

        <tr>
          <td>Sono previsti miglioramenti nei livelli di qualità?</td>
          <td>{{dati_comune.miglior_qual}}</td>
        </tr>

        <tr>
          <td>Sono previsti maggiori costi per la implementazione del TQRIF?</td>
          <td>{{dati_comune.costi_tqrif}}</td>
        </tr>


        <tr align="center">
          <td colspan="2"><b>Dati tecnici dell'appalto</b></td>
        </tr>


        <tr align="center">
          <td colspan="2">Quantitativi totali rifiuti raccolti [ton]</td>
        </tr>


        <tr>
          <td>2020</td>
          <td>{{dati_comune.ton_anno_1}} ton</td>
        </tr>


        <tr>
          <td>2021</td>
          <td>{{dati_comune.ton_anno_2}} ton</td>
        </tr>


        <tr>
          <td>2022</td>
          <td>{{dati_comune.ton_anno_3}} ton</td>
        </tr>

        <tr align="center">
          <td colspan="2">Percentuali raccolta differenziata</td>
        </tr>

        <tr>
          <td>2020</td>
          <td>{{dati_comune.xcent_raccolta_anno_1}}</td>
        </tr>


        <tr>
          <td>2021</td>
          <td>{{dati_comune.xcent_raccolta_anno_2}}</td>
        </tr>


        <tr>
          <td>2022</td>
          <td>{{dati_comune.xcent_raccolta_anno_3}}</td>
        </tr>


        <tr>
          <td>Percentuali media delle impurità riscontrate nell'ultima annualità nelle frazioni differenziate</td>
          <td>{{dati_comune.xcent_media_imp}}</td>
        </tr>


        <tr>
          <td>Rifiuti organici</td>
          <td>{{dati_comune.xcent_media_imp_org}}</td>
        </tr>


        <tr>
          <td>Carta e cartone</td>
          <td>{{dati_comune.xcent_media_imp_cart}}</td>
        </tr>

        <tr align="center">
          <td colspan="2">Imballaggi</td>
        </tr>

        <tr>
          <td>Plastica</td>
          <td>{{dati_comune.xcent_media_imp_plastica}}</td>
        </tr>


        <tr>
          <td>Metallo</td>
          <td>{{dati_comune.xcent_media_imp_metallo}}</td>
        </tr>



        <tr>
          <td>Vetro</td>
          <td>{{dati_comune.xcent_media_imp_vetro}}</td>
        </tr>

        <tr align="center">
          <td colspan="2"><b>Documenti riferiti all'appalto</b></td>
        </tr>


        <tr>
          <td>Contabilità di commessa anno 2020 (in excel)</td>
          <td>{{dati_comune.cont_commessa_anno1}}</td>
        </tr>

        <tr>
          <td>Contabilità di commessa anno 2021 (in excel)</td>
          <td>{{dati_comune.cont_commessa_anno2}}</td>
        </tr>

        <tr>
          <td>Contratto d'appalto vigente</td>
          <td>{{dati_comune.contratto_appalto}}</td>
        </tr>

        <tr>
          <td>Ultimo PEF validato dall'ETC (Delibera + Relazione con allegati in file .zip)</td>
          <td>{{dati_comune.ultimo_pef}}</td>
        </tr>
        <tr align="center">
          <td colspan="7"><b>Costi Smaltimento / Trattamento</b></td>
        </tr>

        <tr>
          <td>Anno</td><td>Impianto di smaltimento</td>
          <td>Codice CER/Tipo di rifiuto</td>
          <td>Tipologia costo</td>
          <td>Quantitativi conferiti [ton]</td>
          <td>Prezzo unitario con IVA</td>
          <td>Importo IVA Inclusa</td>
        </tr>
      </table>
    </main>
  </template>


  <script>

  import axios from '@nuxtjs/axios'
  import xls from 'xlsx'

  export default {

      /*async asyncData({ $axios, params })
        {
          try {

            $axios.defaults.withCredentials = true;

            let is_logged = await $axios.$get(`/is_logged`);
            let is_company_set = await $axios.$get(`/is_company_set`);

            if(is_logged === true)
            {

              var utente = await $axios.$get(`/get_user_data`);

                if(is_company_set === true)
                {
                  var dati_comuni = await $axios.$get(`/get_dati_comuni`);
                  var azienda = await $axios.$get(`/get_company_data`);
                }

            }

            let role = await $axios.$get(`/role`);



            return { is_logged,is_company_set,role,utente,dati_comuni,azienda};

          } catch (e) {

              console.log(e)
              return { dati_comuni: [] ,azienda:[],is_logged:false,is_company_set:false};
        }
      },*/

      mounted () {

        this.$axios.defaults.withCredentials = true

        this.$axios.$get(`/is_logged`)
        .then((response) => {
          this.is_logged=response
        })

        this.$axios.$get(`/is_company_set`)
        .then((response) => {
          this.is_company_set=response
        })


        if(this.is_logged === true)
        {

          this.$axios.$get(`/get_user_data`)
          .then((response) => {
            this.utente=response
          })

            if(this.is_company_set === true)
            {
              this.$axios.$get(`/get_dati_comuni`)
              .then((response) => {
                this.dati_comuni = response
              })

              this.$axios.$get(`/get_company_data`)
              .then((response) => {
                this.azienda = response
              })
            }
        }

        this.$axios.$get(`/role`)
        .then((response) => {
          this.role = response
        })

        /*if (this.is_logged === false)
        {
          if (typeof window !== 'undefined')
          {
            // 👉️ can use window here
            window.location.replace("./login")
          }
        }*/

        var i = 0

        if (this.dati_comuni)
        {
          if (this.dati_comuni.length > 0)
          {
            this.is_ready = true
            if(this.is_logged && this.is_company_set)
            {
              while(i < this.dati_comuni.length)
              {
                if(this.dati_comuni[i].completed == false)
                {
                  this.is_ready = false
                  i = this.dati_comuni.length
                }
                i++
              }
            }
          }else {
            this.is_ready = false

          }
        }
      },


    data() {
      return {

        dati_comuni:[],
        azienda:[],
        utente:[],
        is_ready:false,
        role:'Normal',
        is_logged:true,
        is_company_set:true

      }
    },

    methods:
    {
        async riprendiReport()
        {
          this.$axios.post('/update_report')
          location.reload()
        },

        async inviaReport()
        {

          if(this.dati_comuni.length >= 1)
          {


            var XLSX = require("xlsx");
            var workbook = XLSX.utils.book_new();
            const nome_azienda = this.azienda.ragione_sociale

            workbook.Props =
            {
              Title:nome_azienda
            }

            var i = 0
            while(i < this.dati_comuni.length)
            {

                var costi_smaltimento = await this.$axios.post(`/get_costi_smaltimento` ,{id: this.dati_comuni[i].id})
                .then((costi_smaltimento) => {
                  return costi_smaltimento.data;
                });

                var j = 0
                if(costi_smaltimento.length >= 1)
                {
                    var contenuto = ""
                      while(j < costi_smaltimento.length)
                      {
                        contenuto = contenuto + "<tr><td>"+ costi_smaltimento[j].anno +"</td>";
                        contenuto = contenuto + "<td>"+ costi_smaltimento[j].imp_smalt +"</td>";
                        contenuto = contenuto + "<td>"+ costi_smaltimento[j].tipo_rifiuto +"</td>";
                        contenuto = contenuto + "<td>"+ costi_smaltimento[j].tipo_costo +"</td>";
                        contenuto = contenuto + "<td>"+ costi_smaltimento[j].tons +"</td>";
                        contenuto = contenuto + "<td>"+ costi_smaltimento[j].prezzo_unitario +"</td>";
                        contenuto = contenuto + "<td>"+ costi_smaltimento[j].importo +"</td></tr>";

                        j++
                      }

                }
              document.getElementById('tab'+i).insertAdjacentHTML("beforeend", contenuto)

              var tabella = document.getElementById('tab'+i)

              var worksheet = XLSX.utils.table_to_sheet(tabella)
              XLSX.utils.book_append_sheet(workbook, worksheet, this.dati_comuni[i].nome_comune)
              i++
            }

            var file = XLSX.write(workbook,{booktype:"xlsx",type:"array"});
            //var file = XLSX.writeFile(workbook,nome_azienda + ".xlsx",{booktype:"xlsx",type:"binary"});
            file = new File([file], nome_azienda + ".xlsx")

            var formData = new FormData();

            formData.append("export_daticomuni", file , nome_azienda + ".xlsx");


            this.$axios.post('/upload_company_files', formData, {
                 headers: {
                   'Content-Type': "multipart/form-data; charset='utf-8';",

                 },
            })

            .then((response) => {
              if(response.status >= 200 && response.status <= 208)
              {
                  this.$axios.post('/update_report')
                  alert("Report Inviato")
                  location.reload()
              }
            })
            .catch((error) => {

             if (error.response)
             {

                 // The request was made and the server responded with a status code
                 // that falls out of the range of 2xx
                 alert(error.response.data)
                 location.reload()

             }

           });
          }
      }

    }
  }
  </script>
