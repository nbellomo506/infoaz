
import Header from '../components/Header'
import PageTitle from '../components/PageTitle'
import FieldTitle from '../components/FieldTitle'
import Loading from '../components/Loading'
import Footer from '../components/Footer'



  <template>
    <main>
      <Header/>
        <b-nav v-if="dati_comune !== false && is_company_set === true && is_logged === true" class="mt-3" tabs align="center">
          <b-nav-item class="text-danger" @click="goToSection(section.num)" style="cursor:pointer" v-for="section in sections" :key="section.num" :active="section.num === current_section">
            <font :class="{ 'text-secondary':section.num === 4,'text-success': section.completed === 1 && section.num != 4 , 'text-danger': section.completed === 0 && section.num != 4 }">
              {{section.text}}
            </font>
          </b-nav-item>
        </b-nav>

        <div class="container-fluid p-0 pb-0 mb-5 m-0 b-0" v-if="dati_comune !== false && is_company_set === true && is_logged === true && loaded === true">
          <b-container fluid class=" mt-0 b-0">
          <b-row>
            <b-col class="pt-5 bg-light" xl="2" hidden>
              <div class="pt-2 pb-2">
                <ul>
                  <li style="cursor:pointer" v-for="section in sections">
                    <u>
                      <a @click="goToSection(section.num)">{{section.text}}</a>
                    </u>
                  </li>
                </ul>
              </div>
            </b-col>
            <b-col class="borders-rounded pt-5 pb-5 mb-5" offset-xl="3" xl="6">
              <ol class="p-0 m-0 b-0">
              <PageTitle :name="`Comune di ${dati_comune.nome_comune}`"/>
                <div v-bind:class="{'disabled-container' : azienda.report_is_sent || azienda.report_attempts <= 0 }" class="p-0 b-0 m-0" v-if="current_section === 1">
                  <h3>{{sections[current_section-1].text}}</h3>
                  <p>
                    I campi in rosso sono obbligatori.<br>
                    Compilare la pagina in ogni sua parte e premere il pulsante <b>SALVA</b> prima di passare alla pagina successiva.<br>
                    Il pulsante <b>HELP</b> è in basso.
                  </p>
                  <b-row>
                    <b-col :class="container_specs">
                      <div class="text-secondary pr-4">
                          <div>
                            PEF
                          </div>
                      </div>
                      <b-form-radio-group disabled v-model="azienda.pef_mis_o_ric" :options="opts.tipo2"></b-form-radio-group>
                    </b-col>
                  </b-row>
                  <b-container  class="p-0 m-0 b-0" name="calc_o_mis" v-show="azienda.pef_mis_o_ric === 'CALCOLATO'">
                    <b-row>
                      <b-col :class="container_specs">
                      <FieldTitle letter="a" name="ris_ula_o_ore" req="yes" description="Per ciascuno dei servizi elencati, le risorse umane impiegate sono indicate in:" />
                          <b-form-radio-group v-model="dati_comune.ris_ula_o_ore" :options="opts.tipo3"></b-form-radio-group>
                      </b-col>
                    </b-row>
                    <b-row>
                      <b-col :class="container_specs">
                        <FieldTitle letter="b" req="yes" name="tot_app" description="Totale per la conduzione dell'appalto" />
                        <input class="form-control" v-model="dati_comune.tot_app" type="number" >
                      </b-col>
                      <b-col :class="container_specs">
                        <FieldTitle letter="c" req="yes" name="app_servizi" description="Di cui per impiegati e addetti ai servizi generali" />
                        <input class="form-control" v-model="dati_comune.app_servizi" type="number">
                      </b-col>
                    </b-row>
                    <b-row>
                      <b-col :class="container_specs">
                        <FieldTitle letter="d" req="yes" name="app_rifiuti_diff" description="Di cui per addetti alla raccolta e trasporto dei rifiuti differenziati" />
                        <input class="form-control" v-model="dati_comune.app_rifiuti_diff" type="number">
                      </b-col>
                      <b-col :class="container_specs">
                        <FieldTitle letter="e" req="yes" name="app_rifiuti_indiff" description="Di cui per addetti alla raccolta e trasporto dei rifiuti indifferenziati" />
                        <input class="form-control" v-model="dati_comune.app_rifiuti_indiff" type="number">
                      </b-col>
                    </b-row>
                    <b-row>
                      <b-col :class="container_specs" xl="12">
                        <FieldTitle letter="f" req="yes" name="app_igiene" description="Di cui per addetti ai servizi di spazzamento e igiene urbana" />
                        <input class="form-control" v-model="dati_comune.app_igiene" type="number">
                      </b-col>
                    </b-row>
                  <hr>
                </b-container>

                  <b-row>
                    <b-col :class="container_specs">
                      <FieldTitle name="altri_gestori_flag" req="yes" description="Oltre al Comune e all'impresa operano altri Gestori nel medesimo Comune / Ambito Tariffario?" />
                      <b-form-radio-group v-model="dati_comune.altri_gestori_flag" :options="opts.tipo1"></b-form-radio-group>
                    </b-col>
                    <b-col :class="container_specs" v-show="dati_comune.altri_gestori_flag === true" >
                      <FieldTitle   letter="a" name="altri_gestori"  description="Per quali servizi operano gli altri Gestori" />
                      <input class="form-control" v-model="dati_comune.altri_gestori" type="text">
                    </b-col>
                  </b-row>

                  <b-row>
                    <b-col :class="container_specs">
                      <FieldTitle name="appalto_attuale_data" description="L'appalto con la configurazione attuale è stato avviato il" />
                      <input class="form-control" v-model="dati_comune.appalto_attuale_data" type="date">
                    </b-col>

                    <b-col :class="container_specs">
                      <FieldTitle name="impresa_op_com_data" description="L'impresa opera nel Comune / Ambito Tariffario da" />
                      <input class="form-control" v-model="dati_comune.impresa_op_com_data" type="date">
                    </b-col>
                  </b-row>

                  <b-row>
                    <b-col :class="container_specs">
                      <FieldTitle name="valore_can" description="Valore del canone contrattuale IVA ESCLUSA nell'anno corrente" />
                      <input class="form-control" v-model="dati_comune.valore_can" type="number">

                    </b-col>

                    <b-col :class="container_specs">
                      <FieldTitle name="adeg_contr_flag" description="E' previsto l'adeguamento contrattuale del canone su base annua?" />
                      <b-form-radio-group v-model="dati_comune.adeg_contr_flag" :options="opts.tipo1"></b-form-radio-group>
                    </b-col>
                  </b-row>

                  <b-row>
                    <b-col :class="container_specs" xl="12">
                      <FieldTitle name="ricavi_conai" description="I ricavi dai sistemi di compliance (ricavi CONAI e altri) competono all'impresa o al Comune?" />
                      <b-form-radio-group v-model="dati_comune.ricavi_conai" :options="opts.tipo4"></b-form-radio-group>
                    </b-col>
                  </b-row>

                  <b-row>
                    <b-col :class="container_specs" xl="12">
                      <FieldTitle name="impresa_cts_flag" description="L'impresa sostiene costi CTS relativi al Trattamento e Smaltimento Rifiuti?" />
                      <b-form-radio-group v-model="dati_comune.impresa_cts_flag" :options="opts.tipo1"></b-form-radio-group>
                    </b-col>
                  </b-row>

                  <b-row>
                    <b-col :class="container_specs" xl="12">
                      <FieldTitle name="impresa_ctr_flag" description="L'impresa sostiene costi CTR relativi al Trattamento e Riciclo  Rifiuti?" />
                      <b-form-radio-group v-model="dati_comune.impresa_ctr_flag" :options="opts.tipo1"></b-form-radio-group>
                    </b-col>
                  </b-row>

                  <b-row>
                    <b-col :class="container_specs" xl="12">
                      <FieldTitle    name="" description="Sono inclusi nel contratto e a carico dell'impresa anche i servizi di spazzamento e igiene ambientale?" />
                      <b-form-radio-group v-model="dati_comune.spazz_e_ig_flag" :options="opts.tipo1"></b-form-radio-group>

                    </b-col>
                  </b-row>

                  <b-row>
                    <b-col :class="container_specs">
                      <FieldTitle name="serv_exra_arera_flag" description="Sono presenti nel contratto anche servizi non inseriti del perimetro definito da ARERA?" />
                      <b-form-radio-group v-model="dati_comune.serv_exra_arera_flag" :options="opts.tipo1"></b-form-radio-group>
                    </b-col>
                    <b-col :class="container_specs" v-show="dati_comune.serv_exra_arera_flag == true">
                      <FieldTitle req="yes" letter="a" name="serv_exra_arera" description="Servizi non inseriti nel perimetro" />
                      <input class="form-control" v-model="dati_comune.serv_exra_arera" >
                    </b-col>
                  </b-row>

                  <b-row>
                    <b-col :class="container_specs">
                      <FieldTitle name="" description="L'impresa ha in essere 'lavori in corso' per come definiti da ARERA?" />
                      <b-form-radio-group v-model="dati_comune.lav_in_corso_flag" :options="opts.tipo1"></b-form-radio-group>
                    </b-col>
                    <b-col :class="container_specs" >
                      <div v-show="dati_comune.lav_in_corso_flag == true">
                        <FieldTitle req="yes" letter="a" name="" description="Descrizione dei lavori in corso" />
                        <input class="form-control" v-model="dati_comune.lav_in_corso" >
                      </div>
                    </b-col>
                  </b-row>

                  <b-row>
                    <b-col :class="container_specs">
                      <FieldTitle name="" description="Sono previste variazioni nelle attività gestionali?" />
                      <b-form-radio-group v-model="dati_comune.var_gest_flag" :options="opts.tipo1"></b-form-radio-group>
                    </b-col>
                    <b-col :class="container_specs" >
                      <div v-show="dati_comune.var_gest_flag == true">
                        <FieldTitle req="yes" letter="a" name="" description="Descrizione delle variazioni nella attività gestionali" />
                        <input class="form-control" v-model="dati_comune.var_gest" >
                      </div>
                    </b-col>
                  </b-row>

                  <b-row>
                    <b-col :class="container_specs">
                      <FieldTitle    name="miglior_qual_flag" description="Sono previsti miglioramenti nei livelli di qualità?" />
                      <b-form-radio-group v-model="dati_comune.miglior_qual_flag" :options="opts.tipo1"></b-form-radio-group>
                    </b-col>
                    <b-col :class="container_specs">
                      <div v-show="dati_comune.miglior_qual_flag == true">
                        <FieldTitle req="yes" letter="a" name="miglior_qual" description="Descrizione dei miglioramenti previsti" />
                        <input class="form-control" v-model="dati_comune.miglior_qual" >
                      </div>

                    </b-col>
                  </b-row>

                  <b-row>
                    <b-col :class="container_specs">
                      <FieldTitle name="costi_tqrif_flag" description="Sono previsti maggiori costi per la implementazione del TQRIF?" />
                      <b-form-radio-group v-model="dati_comune.costi_tqrif_flag" :options="opts.tipo1"></b-form-radio-group>
                    </b-col>

                    <b-col :class="container_specs">
                      <div v-show="dati_comune.costi_tqrif_flag == true">
                        <FieldTitle req="yes" letter="a" name="costi_tqrif" description="Importo dei costi previsti per il TQRIF" />
                        <input class="form-control" v-model="dati_comune.costi_tqrif"   type="number">
                      </div>

                    </b-col>
                  </b-row>
                </div>
                <div v-bind:class="{'disabled-container' : azienda.report_is_sent || azienda.report_attempts <= 0 }" class="p-0 b-0 m-0" v-if="current_section === 2">
                  <b-container class="m-0 p-0 b-0">
                    <h3>Dati tecnici dell'appalto</h3>
                    <p>
                      I campi in rosso sono obbligatori.<br>
                      Compilare la pagina in ogni sua parte e premere il pulsante <b>SALVA</b> prima di passare alla pagina successiva.<br>
                      Il pulsante <b>HELP</b> è in basso.
                    </p>
                    <b-row>
                      <b-col :class="container_specs" xl="12">
                        <FieldTitle req="yes" name="tons" description="Quantitativi totali rifiuti raccolti [ton]" />
                      </b-col>
                    </b-row>
                    <b-row>
                      <b-col xl="4" >
                        <FieldTitle letter="a" req="yes" name="" description="2020" />
                        <input class="form-control" v-model="dati_comune.ton_anno_1" type="number">
                      </b-col>
                      <b-col xl="4">
                        <FieldTitle letter="b" req="yes" name="" description="2021" />
                        <input class="form-control" v-model="dati_comune.ton_anno_2" type="number">
                      </b-col>
                      <b-col xl="4">
                        <FieldTitle letter="c" req="yes" name="" description="2022" />
                        <input class="form-control" v-model="dati_comune.ton_anno_3" type="number">
                      </b-col>
                    </b-row>
                  </b-container>
                  <b-container class="m-0 mt-4 p-0 b-0">
                    <b-row>
                      <b-col :class="container_specs" xl="12">
                        <FieldTitle name="tons" req="yes" description="Percentuali raccolta differenziata" />
                      </b-col>
                    </b-row>
                    <b-row>
                      <b-col xl="4" >
                        <FieldTitle letter="a" req="yes" name="" description="2020" />
                        <input class="form-control" v-model="dati_comune.xcent_raccolta_anno_1" type="number">
                      </b-col>
                      <b-col xl="4">
                        <FieldTitle letter="b" req="yes" name="" description="2021" />
                        <input class="form-control" v-model="dati_comune.xcent_raccolta_anno_2" type="number">
                      </b-col>
                      <b-col xl="4">
                        <FieldTitle letter="c" req="yes" name="" description="2022" />
                        <input class="form-control" v-model="dati_comune.xcent_raccolta_anno_3" type="number">
                      </b-col>
                    </b-row>
                  </b-container>
                    <b-row>
                      <b-col :class="container_specs" xl="12">
                        <FieldTitle   name="tons" req="yes" description="Percentuale media delle impurità riscontrate nell'ultima annualità nelle frazioni differenziate" />
                        <input  class="form-control" v-model="dati_comune.xcent_media_imp" type="number">
                      </b-col>
                    </b-row>

                    <b-row>
                    <b-col xl="3" class="mt-5 pl-3 pr-3">
                      <FieldTitle letter="a" req="yes" name="" description="Rifiuti organici" />
                      <input class="form-control" v-model="dati_comune.xcent_media_imp_org" type="number">
                    </b-col>
                    <b-col xl="3" class="mt-5 pl-3 pr-3">
                      <FieldTitle letter="b" req="yes" name="" description="Carta e cartone" />
                      <input class="form-control" v-model="dati_comune.xcent_media_imp_cart" type="number">
                    </b-col>

                    <b-col class="borders bg-grey rounded mt-3" xl="6">
                      <b-container class="m-0 p-0 b-0">
                        <b-row class="m-0 p-0 b-0">
                          <b-col offset-xl="4" xl="4">
                            <b>Imballaggi</b>
                          </b-col>
                        </b-row>

                        <b-row class="m-0 p-0 pb-3 b-0">
                          <b-col xl="4" class="p-0 pr-2">
                            <FieldTitle letter="c" req="yes" name="" description="Plastica" />
                            <input class="form-control" v-model="dati_comune.xcent_media_imp_plastica" type="number">
                          </b-col>
                          <b-col xl="4" class="p-0 pr-2">
                            <FieldTitle letter="d" req="yes" name="" description="Metallo" />
                            <input class="form-control" v-model="dati_comune.xcent_media_imp_metallo" type="percent">
                          </b-col>
                          <b-col xl="4" class="p-0 pr-2">
                            <FieldTitle letter="e" req="yes" name="" description="Vetro" />
                            <input class="form-control" v-model="dati_comune.xcent_media_imp_vetro" type="number">
                          </b-col>
                        </b-row>
                      </b-container>
                    </b-col>
                    </b-row>
                </div>
                <div v-bind:class="{'disabled-container' : azienda.report_is_sent || azienda.report_attempts <= 0 }" class="p-0 b-0 m-0" v-if="current_section === 3">
                  <b-container class="m-0 p-0 b-0">
                    <h3>Documenti riferiti all'appalto</h3>
                    <p>
                      I campi in rosso sono obbligatori.<br>
                      Compilare la pagina in ogni sua parte e premere il pulsante <b>SALVA</b> prima di passare alla pagina successiva.<br>
                      Il pulsante <b>HELP</b> è in basso.
                    </p>
                    <b-row>
                      <b-col cols="12" :class="container_specs">
                        <FieldTitle   req="yes" description="Contabilità di commessa anno 2020 (in excel)" />
                        <b-container>
                          <b-row>
                            <b-col cols="10" xl="10">
                              <b-form-file
                                v-model="files.cont_commessa_anno1"
                                placeholder="File Excel"
                                drop-placeholder="Rilascia qui...">
                              </b-form-file>
                              <font v-if="dati_comune.cont_commessa_anno1 != '[object File]'">
                                {{dati_comune.cont_commessa_anno1}}
                              </font>
                            </b-col>
                            <b-col cols="2" xl="2">
                              <b-icon v-if="dati_comune.cont_commessa_anno1 !== '' || files.cont_commessa_anno1.length !== 0" class="h4 p-0 b-0 m-0 mt-1" variant="success" icon="check-circle-fill"></b-icon>
                              <b-icon v-if="dati_comune.cont_commessa_anno1  === '' && files.cont_commessa_anno1.length === 0"  class="h4 p-0 b-0 m-0 mt-1" variant="danger" icon="x-circle-fill"></b-icon>
                            </b-col>
                          </b-row>
                        </b-container>
                      </b-col>

                      <b-col cols="12" :class="container_specs">
                        <FieldTitle req="yes" description="Contabilità di commessa anno 2021 (in excel)" />
                        <b-container>
                          <b-row>
                            <b-col cols="10" xl="10">
                              <b-form-file
                                v-model="files.cont_commessa_anno2"
                                placeholder="File Excel"
                                drop-placeholder="Rilascia qui...">
                              </b-form-file>
                              <font v-if="dati_comune.cont_commessa_anno2 != '[object File]' ">
                                {{dati_comune.cont_commessa_anno2}}
                              </font>
                            </b-col>
                            <b-col cols="2" xl="2">
                              <b-icon v-if="dati_comune.cont_commessa_anno2  !== '' || files.cont_commessa_anno2.length !== 0" class="h4 p-0 b-0 m-0 mt-1" variant="success" icon="check-circle-fill"></b-icon>
                              <b-icon v-if="dati_comune.cont_commessa_anno2  === '' && files.cont_commessa_anno2.length === 0"  class="h4 p-0 b-0 m-0 mt-1" variant="danger" icon="x-circle-fill"></b-icon>
                            </b-col>
                          </b-row>
                        </b-container>
                      </b-col>
                    </b-row>

                    <b-row>
                      <b-col cols="12" :class="container_specs">
                        <FieldTitle  req="yes" description="Contratto d'appalto vigente" />
                        <b-container>
                          <b-row>
                            <b-col cols="10" xl="10">
                              <b-form-file
                                v-model="files.contratto_appalto"
                                placeholder="File PDF"
                                drop-placeholder="Rilascia qui...">
                              </b-form-file>
                              <font v-if="dati_comune.contratto_appalto != '[object File]' ">
                                {{dati_comune.contratto_appalto}}
                              </font>
                            </b-col>
                            <b-col cols="2" xl="2">
                              <b-icon v-if="dati_comune.contratto_appalto !== '' || files.contratto_appalto.length !== 0" class="h4 p-0 b-0 m-0 mt-1" variant="success" icon="check-circle-fill"></b-icon>
                              <b-icon v-if="dati_comune.contratto_appalto  === '' && files.contratto_appalto.length === 0"  class="h4 p-0 b-0 m-0 mt-1" variant="danger" icon="x-circle-fill"></b-icon>
                            </b-col>
                          </b-row>
                        </b-container>
                      </b-col>
                      <b-col cols="12" :class="container_specs">
                        <FieldTitle req="yes" description="Ultimo PEF validato dall'ETC (Delibera + Relazione con allegati in file .zip)" />
                        <b-container>
                          <b-row>
                            <b-col cols="10" xl="10">
                              <b-form-file
                                v-model="files.ultimo_pef"
                                placeholder="File Zip"
                                drop-placeholder="Rilascia qui...">
                              </b-form-file>
                              <font v-if="dati_comune.ultimo_pef != '[object File]' ">
                                {{dati_comune.ultimo_pef}}
                              </font>
                              {{files.ultimo_pef.name}}
                            </b-col>
                            <b-col cols="2" xl="2">
                              <b-icon v-if="dati_comune.ultimo_pef !== '' || files.ultimo_pef.length != 0" class="h4 p-0 b-0 m-0 mt-1" variant="success" icon="check-circle-fill"></b-icon>
                              <b-icon v-if="dati_comune.ultimo_pef  === '' && files.ultimo_pef.length === 0"  class="h4 p-0 b-0 m-0 mt-1" variant="danger" icon="x-circle-fill"></b-icon>
                            </b-col>
                          </b-row>
                        </b-container>
                      </b-col>
                    </b-row>
                  </b-container>
                </div>
              </ol>
            </b-col>
          </b-row>
        </b-container>


        <b-row v-bind:class="{'disabled-container' : azienda.report_is_sent || azienda.report_attempts <= 0 }" v-if="current_section === 4" class="ml-3 mr-3 mb-5 pb-5">
          <b-col xl="12">
            <h3>Costi Smaltimento / Trattamento</h3>
            <p>
              Per inserire una nuova riga dopo la sua compilazione premere il tasto <b>AGGIUNGI</b> e quindi il tasto <b>SALVA</b>.
            </p>
            <b-row>
              <b-col class="text-center" xl="1">
                Anno
              </b-col>
              <b-col class="text-center" xl="2">
                Impianto di smaltimento
              </b-col>
              <b-col class="text-center" xl="2">
                Codice CER/Tipo di rifiuto
              </b-col>
              <b-col class="text-center" xl="1">
                Tipologia costo
              </b-col>
              <b-col class="text-center" xl="1">
                Quantitativi conferiti [ton]
              </b-col>
              <b-col class="text-center" xl="2">
              Prezzo unitario con IVA [€\ton]
              </b-col>
              <b-col class="text-center" xl="2">
              Importo IVA Inclusa
              </b-col>
            </b-row>
            <b-row class="bg-light rounded p-3">
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
                <b-alert class="mt-2" v-if="add.msg.tipo_rifiuto.length > 0" variant="danger" dismissible show>
                  {{add.msg.tipo_rifiuto}}
                </b-alert>
              </b-col>

              <b-col class="p-0" xl="1">
                <select class="form-control" v-model="add.tipo_costo" >
                  <option value="CTS">CTS</option>
                  <option value="CTR">CTR</option>
                </select>
              </b-col>

              <b-col xl="1">
                <input class="form-control pl-1" min="0" @change=calcoloImporto() v-model="add.tons" type="number">
              </b-col>

              <b-col xl="2">
                <input class="form-control pl-1" min="0" @change=calcoloImporto() v-model="add.prezzo_unitario" type="number">
              </b-col>

              <b-col xl="2">
                <input class="form-control pl-1" min="0" v-model="add.importo" type="number">
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
                <textarea  class="form-control" v-model="extra.tipo_rifiuto">{{extra.tipo_rifiuto}}</textarea>
              </b-col>

              <b-col class="p-0 pr-1" xl="1">
                <select class="form-control" v-model="extra.tipo_costo" >
                  <option value="CTS">CTS</option>
                  <option value="CTR">CTR</option>
                </select>
              </b-col>

              <b-col xl="1">
                <input class="form-control pl-1" min="0" type="number" @change="extra.importo = extra.tons * extra.prezzo_unitario" v-model="extra.tons">
              </b-col>

              <b-col xl="2">
                <b-input class="form-control pl-1" min="0" type="number" @change="extra.importo = extra.tons * extra.prezzo_unitario" v-model="extra.prezzo_unitario"></b-input>
              </b-col>

              <b-col xl="2">
                <input class="form-control pl-1" min="0" type="number" v-model="extra.importo">
              </b-col>

              <b-col xl="1">
                <b-container class="pr-2 mb-5">
                  <b-row>
                    <b-col xl="5 p-0">
                      <button type="button" @click=modificaExtra(extra) block class="btn btn-success" name="button">
                        <b-icon icon="check-square-fill"></b-icon>
                      </button>
                    </b-col>

                    <b-col class="offset-xl-2 p-0" xl="5">
                      <button type="button" @click=eliminaExtra(extra.id) block class="btn btn-danger" name="button">
                        <b-icon icon="trash"></b-icon>
                      </button>
                    </b-col>
                  </b-row>
                </b-container>
              </b-col>
            </b-row>
          </b-col>
        </b-row>
      <Footer :visible="loaded"/>
    </div>

      <b-container v-if="loaded === false">
        <Loading/>
      </b-container>

      <b-container v-if="is_logged === true && is_company_set === false && loaded === true" class="mb-3">
        <b-row>
          <b-col offset-xl="1" xl="10">
            <b-container class="mb-3 mt-5">
              <b-row>
                <b-col xl="12">
                  <h1>Attenzione</h1>
                  <p>
                    Ciao , la tua richiesta di accesso è stata inviata ma i gestori non ti hanno ancora associato l'azienda.<br>
                    Pertanto non hai accesso ai dati inseriti dalla tua azienda
                  </p>
                </b-col>
              </b-row>
            </b-container>
          </b-col>
        </b-row>
      </b-container>


      <b-container v-if="dati_comune === false && is_logged === true && is_company_set === true && loaded === true" class="mb-3">
        <b-row>
          <b-col offset-xl="1" xl="10">
            <b-container class="mb-3 mt-5">
              <b-row>
                <b-col xl="12">
                  <h1>Attenzione</h1>
                  <p>
                    Pagina non trovata
                  </p>
                </b-col>
              </b-row>
            </b-container>
          </b-col>
        </b-row>
      </b-container>

      <div v-if="dati_comune !== false && is_logged === true && is_company_set === true && loaded === true" class="bg-light border fixed-bottom p-2">
        <b-container class="container">
          <b-row class="row">
            <b-col class=" text-center xl-1 offset-xl-5">
              <b-button v-b-modal="'help-tab'" block variant="warning">
                  Help
              </b-button>
            </b-col>
            <b-col class="xl-1 offset-xl-4">
              <b-button block @click="saveDatiComune(dati_comune,files)" variant="infowaste">
                  Salva
              </b-button>
            </b-col>
          </b-row>
        </b-container>
      </div>

        <b-modal id="help-tab" cancel-variant="danger" ok-variant="infowaste" @ok="askHelp" cancel-title="Annulla" ok-title="Invia">
          <font class="h5">Messaggio</font><br>
          (verrà inviata un'email ad assistenza@bintobit.com)
          <b-form-input v-model="help_message"></b-form-input>
        </b-modal>

        <b-modal id="bv-modal-save-msg" hide-footer>
          <div class="text-center">
            <h5>{{save.msg}}</h5>
          </div>
          <hr>
          <b-container class="container">
            <b-row class="row">
              <b-col class="sm-4 offset-sm-6 xl-2 offset-xl-8">
                <b-button class="mt-3" :variant="save.color" block @click="$bvModal.hide('bv-modal-save-msg')">
                  Ok
                </b-button>
              </b-col>
            </b-row>
          </b-container>
        </b-modal>
    </main>
  </template>

  <script>
  import axios from '@nuxtjs/axios'
  import xls from 'xlsx'

  export default {

    async asyncData({ $axios, params })
    {
        let id = params.id;
        return {id}
    },

    mounted ()
    {
      this.$axios.defaults.withCredentials = true

      try {
        this.$axios.$get(`/is_logged`)
        .then((response) => {
          this.is_logged = response
        })

        this.$axios.$get(`/is_company_set`)
        .then((response) => {
          this.is_company_set = response
        })

        this.$axios.$get(`/role`)
        .then((response) => {
          this.role = response
        })

        this.$axios.$post(`/get_dati_comune`,{id: this.id})
        .then((response) => {
          this.dati_comune = response
          if(this.dati_comune.altri_gestori_flag == true)
          {
            if(this.dati_comune.altri_gestori == "")
            {
              this.sections[0].completed = 0
            }
          }else {
            this.dati_comune.altri_gestori=""

          }

          if(this.dati_comune.serv_exra_arera_flag == true)
          {
            if(this.dati_comune.serv_exra_arera == "")
            {
              this.sections[0].completed = 0
            }
          }else {
            this.dati_comune.serv_exra_arera=""

          }

          if(this.dati_comune.lav_in_corso_flag == true)
          {
            if(this.dati_comune.lav_in_corso == "")
            {
              this.sections[0].completed = 0
            }
          }else {
            this.dati_comune.lav_in_corso=""

          }

          if(this.dati_comune.var_gest_flag == true)
          {
            if(this.dati_comune.var_gest == "")
            {
              this.sections[0].completed = 0

            }
          }else {
            this.dati_comune.var_gest=""

          }

          if(this.dati_comune.miglior_qual_flag == true)
          {
            if(this.dati_comune.miglior_qual == "")
            {
              this.sections[0].completed = 0
            }
          }else {
            this.dati_comune.miglior_qual=""

          }

          if(this.dati_comune.costi_tqrif_flag == true)
          {
            if(this.dati_comune.costi_tqrif == 0)
            {
              this.sections[0].completed = 0
            }
          }else {
            this.dati_comune.costi_tqrif=0

          }

          if (this.dati_comune.ton_anno_1 === 0  || this.dati_comune.ton_anno_2 === 0 || this.dati_comune.ton_anno_3 === 0)
          {
            this.sections[1].completed = 0
            console.log("incompleto")

          }

          if (this.dati_comune.xcent_raccolta_anno_1 == 0 || this.dati_comune.xcent_raccolta_anno_2 == 0 || this.dati_comune.xcent_raccolta_anno_3 == 0)
          {

            this.sections[1].completed = 0
          }


          if(this.dati_comune.xcent_media_imp == 0 ||
          this.dati_comune.xcent_media_imp_org == 0 ||
          this.dati_comune.xcent_media_imp_cart == 0 ||
          this.dati_comune.xcent_media_imp_plastica == 0 ||
          this.dati_comune.xcent_media_imp_metallo == 0 ||
          this.dati_comune.xcent_media_imp_vetro == 0 )
          {

            this.sections[1].completed = 0
          }


          if(this.dati_comune.cont_commessa_anno1 == '' || this.dati_comune.cont_commessa_anno2 == '' || this.dati_comune.contratto_appalto == '' || this.dati_comune.ultimo_pef == '')
          {
            this.sections[2].completed = 0
          }

          this.current_section = this.dati_comune['current_section']

        })

        this.$axios.$get(`/get_company_data`)
        .then((response) => {
          this.azienda = response
          if(this.azienda.pef_mis_o_ric === "CALCOLATO")
          {
            if( this.dati_comune.ris_ula_o_ore === "" ||
                this.dati_comune.tot_app <= 0 ||
                this.dati_comune.app_servizi <= 0 ||
                this.dati_comune.app_rifiuti_diff <= 0 ||
                this.dati_comune.app_rifiuti_indiff <= 0 ||
                this.dati_comune.app_igiene <= 0 )
              {
                this.sections[0].completed = 0
              }
          }
        })

        this.$axios.$post(`/get_costi_smaltimento` ,{id: this.id})
        .then((response) => {
          this.costi_smaltimento = response
        })




        this.loaded = true

      } catch (e) {
        console.log(e)
      }



    },

    methods:
    {
        async askHelp()
        {
          var section = this.sections[this.current_section - 1].text
          section = section
          this.$axios.post('/askHelp', {

            message: this.help_message,
            section: section,

          })

        },

        async goToSection(num)
        {
           if (num >= 1 &&  num <= this.sections.length)
           {
                this.current_section = num

          }

        },

        async uploadFiles(dati_comune)
        {

            var formData = new FormData();
            var upload = false

            if(dati_comune.cont_commessa_anno1 == '[object File]')
            {
              upload = true
              dati_comune.cont_commessa_anno1 = new File([dati_comune.cont_commessa_anno1],dati_comune.cont_commessa_anno1.name)
              formData.append("cont_commessa_anno1", dati_comune.cont_commessa_anno1,dati_comune.cont_commessa_anno1.name);
            }

            if(dati_comune.cont_commessa_anno2 == '[object File]')
            {
              upload = true
              dati_comune.cont_commessa_anno2 = new File([dati_comune.cont_commessa_anno2],dati_comune.cont_commessa_anno2.name)
              formData.append("cont_commessa_anno2", dati_comune.cont_commessa_anno2,dati_comune.cont_commessa_anno2.name);
            }

            if(dati_comune.contratto_appalto == '[object File]')
            {
              upload = true
              dati_comune.contratto_appalto = new File([dati_comune.contratto_appalto],dati_comune.contratto_appalto.name)
              formData.append("contratto_appalto", dati_comune.contratto_appalto,dati_comune.contratto_appalto.name);
            }

            if(dati_comune.ultimo_pef == '[object File]')
            {
              upload = true
              dati_comune.ultimo_pef = new File([dati_comune.ultimo_pef],dati_comune.ultimo_pef.name)
              formData.append("ultimo_pef", dati_comune.ultimo_pef,dati_comune.ultimo_pef.name);
            }


            if (upload)
            {
              var id = this.dati_comune.id
              id = new File([id],id)
              formData.append("id", id ,this.dati_comune.id);

              var azienda = this.dati_comune.azienda
              azienda = new File([azienda],azienda)
              formData.append("azienda", azienda ,this.dati_comune.azienda);

              this.$axios.post('/upload_comune_files',formData,{

                   headers: {
                     'Content-Type': "multipart/form-data; charset='utf-8';",

                   },
              })
            }

        },

        async aggiungiExtra()
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
                this.$axios.post('/add_costi_smaltimento', {

                  daticomune:this.dati_comune.id,
                  imp_smalt: this.add.imp_smalt,
                  tipo_rifiuto: this.add.tipo_rifiuto,
                  tipo_costo: this.add.tipo_costo,
                  anno: this.add.anno,
                  tons: this.add.tons,
                  prezzo_unitario: this.add.prezzo_unitario,
                  importo: this.add.importo

                })

                this.saveDatiComune(this.dati_comune,this.files)
                location.reload()
            }


        },

        async modificaExtra(extra)
        {

          this.$axios.post('/update_costi_smaltimento',{

            id:extra.id,
            daticomune:this.dati_comune.id,
            imp_smalt: extra.imp_smalt,
            tipo_rifiuto: extra.tipo_rifiuto,
            tipo_costo: extra.tipo_costo,
            anno: extra.anno,
            tons: extra.tons,
            prezzo_unitario: extra.prezzo_unitario,
            importo: extra.importo,

          })
          this.saveDatiComune(this.dati_comune,this.files)
          location.reload()

        },

        async eliminaExtra(id)
        {
          this.$axios.post('/del_costi_smaltimento',
           {
             daticomune:this.dati_comune.id,
             id: id
           })
          this.saveDatiComune(this.dati_comune,this.files)
          location.reload()

        },

        async calcoloImporto()
        {
            this.add.importo = this.add.tons * this.add.prezzo_unitario
        },

        async saveDatiComune(dati_comune,files)
        {
          var is_completed = 1

          if(this.azienda.pef_mis_o_ric === "CALCOLATO")
          {
            if(
              dati_comune.ris_ula_o_ore === "" ||
              dati_comune.tot_app <= 0 ||
              dati_comune.app_servizi <= 0 ||
              dati_comune.app_rifiuti_diff <= 0 ||
              dati_comune.app_rifiuti_indiff <= 0 ||
              dati_comune.app_igiene <= 0 )
              {
                  is_completed = 0
              }
          }


          else if(this.azienda.pef_mis_o_ric === "MISURATO")
          {
            dati_comune.tot_app = 0
            dati_comune.app_servizi = 0
            dati_comune.app_rifiuti_diff = 0
            dati_comune.app_rifiuti_indif = 0
            dati_comune.app_igiene = 0
          }

          if(dati_comune.altri_gestori_flag == true)
          {
            if(dati_comune.altri_gestori == "")
            {
              is_completed=0
            }
          }else {
            dati_comune.altri_gestori=""

          }

          if(dati_comune.serv_exra_arera_flag == true)
          {
            if(dati_comune.serv_exra_arera == "")
            {
              is_completed=0
            }
          }else {
            dati_comune.serv_exra_arera=""

          }

          if(dati_comune.lav_in_corso_flag == true)
          {
            if(dati_comune.lav_in_corso == "")
            {
              is_completed=0
            }
          }else {
            dati_comune.lav_in_corso=""

          }

          if(dati_comune.var_gest_flag == true)
          {
            if(dati_comune.var_gest == "")
            {
              is_completed=0
            }
          }else {
            dati_comune.var_gest=""

          }

          if(dati_comune.miglior_qual_flag == true)
          {
            if(dati_comune.miglior_qual == "")
            {
              is_completed=0
            }
          }else {
            dati_comune.miglior_qual=""

          }

          if(dati_comune.costi_tqrif_flag == true)
          {
            if(dati_comune.costi_tqrif == 0)
            {
              is_completed=0
            }
          }else {
            dati_comune.costi_tqrif=0

          }


          if (dati_comune.ton_anno_1 == 0  || dati_comune.ton_anno_2 == 0 || dati_comune.ton_anno_3 == 0)
          {
              is_completed = 0
          }

          if (dati_comune.xcent_raccolta_anno_1 == 0 || dati_comune.xcent_raccolta_anno_2 == 0 || dati_comune.xcent_raccolta_anno_3 == 0)
          {
              is_completed = 0
          }


          if(dati_comune.xcent_media_imp == 0 ||
          dati_comune.xcent_media_imp_org == 0 ||
          dati_comune.xcent_media_imp_cart == 0 ||
          dati_comune.xcent_media_imp_plastica == 0 ||
          dati_comune.xcent_media_imp_metallo == 0 ||
          dati_comune.xcent_media_imp_vetro == 0 )
          {
            is_completed = 0
          }

          //controllo invio dei FILES
          if(files.cont_commessa_anno1 != '[object File]' && dati_comune.cont_commessa_anno1 == '')
          {
            is_completed = 0
          }

              if(files.cont_commessa_anno2 != '[object File]' && dati_comune.cont_commessa_anno2 == '')
              {
                is_completed = 0
              }

                  if(files.contratto_appalto != '[object File]' && dati_comune.contratto_appalto == '')
                  {
                    is_completed = 0
                  }

                      if(files.ultimo_pef != '[object File]' && dati_comune.ultimo_pef == '')
                      {
                        is_completed = 0
                      }


          this.$axios.post('/save_dati_comune', {

            id: dati_comune.id,
            azienda: dati_comune.azienda,
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
            ricavi_conai: dati_comune.ricavi_conai,
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
            xcent_media_imp_vetro: dati_comune.xcent_media_imp_vetro,
            current_section: this.current_section,
            completed: is_completed

          })

          .then(response => {

              if(response.status >= 200 && response.status <= 208)
              {
                this.save.msg="Salvataggio avvenuto con successo!"
                this.save.color="success"
                //this.$bvModal.show('bv-modal-save-msg')
              }
          })

          .catch(error => {

              this.save.msg=error
              this.save.color="danger"
              //this.$bvModal.show('bv-modal-save-msg')

          });

          this.uploadFiles(files)
          location.reload()

        }
    },


    data()
    {

        return {
                  is_logged:undefined,
                  is_company_set:undefined,
                  loaded:false,
                  role:'Normal',
                  dati_comune:[],
                  azienda:[],
                  sections:
                  [
                    {num:1 , text:"Dati Generali",completed:1},
                    {num:2 , text:"Dati tecnici dell'appalto",completed:1},
                    {num:3 , text:"Documenti riferiti all'appalto",completed:1},
                    {num:4 , text:"Costi Smaltimento / Trattamento",completed:1}
                  ],
                  costi_smaltimento:[],
                  current_section:0,
                  id:0,


                  files:
                  {
                    cont_commessa_anno1:[],
                    cont_commessa_anno2:[],
                    contratto_appalto:[],
                    ultimo_pef:[]
                  },

                  help_message:"",
                  width:0,
                  page_id:0,
                  save:
                  {
                    msg:'',
                    color:''

                  },

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

                  container_specs:'col-12 col-xl-6 p-2 pl-3 pr-3 mt-3 mb-3',
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

                    tipo4:[
                      { text: 'IMPRESA', value: 'IMPRESA' },
                      { text: 'COMUNE', value: 'COMUNE' }
                    ],

                  },
                  dim:6,
                }

            },



  };
  </script>
