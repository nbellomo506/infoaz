
import Header from '../components/Header'
import Field from '../components/Field'





<template>
  <main>
    <Header/>
      <b-container class="mt-5 mb-5">
        <b-row>
          <b-col bg-variant="info" offset-xl="1" xl="10">

            <h1>Benvenuto</h1>
            <h3>Compilazione in corso</h3>

              <b-list-group vertical>
                <b-container class="p-4 pl-1 rounded bg-light" >
                  <a href="anagrafica">
                      Dati Azienda
                  </a>
                </b-container>

                <b-container class="p-4 pl-1 mt-2 rounded bg-light" v-for="(dati_comune,index) in dati_comuni">
                  <b-row>
                    <b-col xl="11">
                      <a :href="`/compila_dati_comune/${dati_comune.id}/`">
                          <b>{{index+1}}. </b>{{dati_comune.nome_comune}}
                      </a>
                    </b-col>
                    <b-col xl="1">
                      <b-icon v-if="dati_comune.sent == 1" class="h3" variant="success" icon="bookmark-check-fill"></b-icon>
                      <b-icon v-else="dati_comune.sent == 1" class="h3" variant="danger" icon="bookmark-x-fill"></b-icon>
                    </b-col>
                  </b-row>

                </b-container>
              </b-list-group>
            </b-col>
          </b-row>



        <b-row>
          <b-col class="mt-4" offset-xl="1" xl="10">
            <p dir="ltr" style="line-height:1.295;text-align: justify;margin-top:0pt;margin-bottom:8pt;"><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">SUPPORTO PEF</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp;&egrave; un servizio a disposizione delle imprese che operano nel settore della gestione dei rifiuti urbani per la compilazione del&nbsp;</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">PEF (Piano Economico Finanziario)</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp;secondo le disposizioni di ARERA (</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">MTR-2</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">). Il servizio si svolge nel rispetto della normativa sulla privacy e sulla gestione dei dati sensibili.</span></p>
            <p dir="ltr" style="line-height:1.295;text-align: justify;margin-top:0pt;margin-bottom:8pt;"><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">L&rsquo;utente dopo essere accreditato compila la sezione&nbsp;</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">ANAGRAFICA</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp;e dichiara i Comuni presso i quali opera con conseguente obbligo di presentazione del PEF.</span></p>
            <p dir="ltr" style="line-height:1.295;text-align: justify;margin-top:0pt;margin-bottom:8pt;"><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Terminata questa fase, l&rsquo;utente procede alla compilazione del PEF riferito al singolo Comune, scegliendolo fra quelli dichiarati, ed individuando una delle due possibili opzioni con cui intende procedere:&nbsp;</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">PEF CALCOLATO</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp;ovvero&nbsp;</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">PEF MISURATO</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">. In entrambi i casi l&rsquo;elaborazione fa riferimento ai dati di bilancio, alla contabilit&agrave; di commessa e dati tecnici che dovranno essere caricati e imputati negli appositi campi dell&rsquo;applicazione.</span></p>
            <p dir="ltr" style="line-height:1.295;text-align: justify;margin-top:0pt;margin-bottom:8pt;"><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Nel caso del&nbsp;</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">PEF CALCOLATO</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp;i driver attraverso cui ripartire i costi sono elaborati prendendo a riferimento valori il pi&ugrave; possibile oggettivi (ad es. numero di abitanti per Comune). Nel caso del&nbsp;</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">PEF MISURATO</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">, invece, i driver sono individuati dall&rsquo;utente sulla base di un set messo a disposizione dall&rsquo;applicazione che li elabora attingendo dall&rsquo;ERP aziendale (</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">WMS / INNOVAMBIENTE</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">): numero di ore lavorate per servizio, numero di chilometri percorsi, numero di contenitori distribuiti&hellip;</span></p>
            <p dir="ltr" style="line-height:1.295;text-align: justify;margin-top:0pt;margin-bottom:8pt;"><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">In entrambi i casi l&rsquo;attivit&agrave; di elaborazione prevede l&rsquo;erogazione di un&nbsp;</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">SERVIZIO DI ASSISTENZA</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp;nell&rsquo;utilizzo dell&rsquo;applicazione e &ndash; se richiesto &ndash; di un&nbsp;</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">SERVIZIO DI CONSULENZA</span><span style="font-size:12pt;font-family:Calibri,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&nbsp;per la revisione dei dati e la stesura della relazione di accompagnamento.</span></p>
          </b-col>
        </b-row>

        <b-row>
          <b-col class="mb-5" bg-variant="info" offset-xl="8" xl="4">
            <b-button @click=inviaReport() block>Invia dati</b-button>
          </b-col>
        </b-row>
      </b-container>

<table v-for="(dati_comune,index) in dati_comuni" :id="`tab${index}`" hidden>
  <tr>
    <td>
      <h6>{{index+1}}. Comune:</h6>
    </td>
    <td>{{dati_comune.nome_comune}}</td>
  </tr>

  <tr>
    <td>PEF</td>
    <td>{{dati_comune.pef_mis_o_ric}}</td>
  </tr>

  <tr>
    <td>Oltre al Comune e all'impresa operano altri Gestori nel medesimo Comune / Ambito Tariffario?</td>
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
  </tr>

  <tr>
    <td>I ricavi dai sistemi di compliance (ricavi CONAI e altri) competono all'impresa o al Comune?</td>
    <td>{{dati_comune.ricavi_conai_flag}}</td>
  </tr>
  <tr>
    <td>L'impresa sostiene costi CTS relativi al Trattamento e Smaltimento Rifiuti?</td>
    <td>{{dati_comune.impresa_cts_flag}}</td>
  </tr>
  <tr>
    <td>L'impresa sostiene costi CTR relativi al Trattamento e Riciclo Rifiuti?</td>
    <td>{{dati_comune.impresa_ctr_flag}}</td>
  </tr>
  <tr>
    <td>Sono inclusi nel contratto e a carico dell'impresa anche i servizi di spazzamento e igiene ambientale?</td>
    <td>{{dati_comune.spazz_e_ig_flag}}</td>
  </tr>
  <tr>
    <td>Sono presenti nel contratto anche servizi non inseriti del perimetro definito da ARERA?</td>
    <td>{{dati_comune.serv_exra_arera}}</td>
  </tr>
  <tr>
    <td>L'impresa ha in essere 'lavori in corso' per come definiti da ARERA?
</td>
    <td>{{dati_comune.lav_in_corso}}</td>
  </tr>
  <tr>
    <td>Sono previste varizioni nelle attività gestionali?
</td>
    <td>{{dati_comune.var_gest}}</td>
  </tr>
  <tr>
    <td>Sono previsti miglioramenti nei livelli di qualità?
</td>
    <td>{{dati_comune.miglior_qual}}</td>
  </tr>
  <tr>
    <td>Sono previsti maggiori costi per la implementazione del TQRIF?
</td>
    <td>{{dati_comune.costi_tqrif}}</td>
  </tr>


  <tr>
    <td></td>
  </tr>


  <tr>
    <td><h6>Costi Smaltimento / Trattamento</h6></td>
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
<b-form-file type="file" v-model="file" >Wezii</b-form-file>

    </main>
  </template>


  <script>

  import axios from '@nuxtjs/axios'
  import xls from 'xlsx'

  export default {


      async asyncData({ $axios, params })
        {
          try {
            let dati_comuni = await $axios.$get(`/dati_comuni/`);
            return { dati_comuni };
          } catch (e) {
              return { dati_comuni: [] };
        }
      },



    data() {
      return {

        file:null

      }
    },

    methods:
    {
        async inviaReport()
        {

          if(this.dati_comuni.length >= 1)
          {

            var XLSX = require("xlsx");
            var workbook = XLSX.utils.book_new();
            const nome_azienda = this.dati_comuni[1].nome_azienda

            workbook.Props =
            {
              Title:nome_azienda
            }

            var i = 0
            while(i < this.dati_comuni.length)
            {
                let costi_smaltimento = await this.$axios.$get(`/costi_smaltimento/?daticomune=` + this.dati_comuni[i].id);
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
                    alert(contenuto)

                }
              document.getElementById('tab'+i).insertAdjacentHTML("beforeend", contenuto)

              var tabella = document.getElementById('tab'+i)

              var worksheet = XLSX.utils.table_to_sheet(tabella)
              XLSX.utils.book_append_sheet(workbook, worksheet, this.dati_comuni[i].nome_comune)
              i++
            }
            //workbook.Sheets.Carceri.A1.v="ciao"
            var file = XLSX.write(workbook,{booktype:"xlsx",type:"binary"});

            file = new File([file], nome_azienda + ".xlsx")


            this.$axios.post('/export_aziende',{

              export_file:file

            })

            .then((response) => {
              if(response.status >= 200 && response.status < 300)
              {

                  alert("tutto bene")

              }
            })
            .catch((error) => {

             if (error.response) {
               // The request was made and the server responded with a status code
               // that falls out of the range of 2xx
               alert(error.response.data)

             }

           });
          }
      }

    }
  }
  </script>
