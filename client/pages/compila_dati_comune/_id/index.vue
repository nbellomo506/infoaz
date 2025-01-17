
import Header from '../components/Header'
import PageTitle from '../components/PageTitle'
import FieldTitle from '../components/FieldTitle'
import Loading from '../components/Loading'
import Footer from '../components/Footer'


  <template>
    <main>
      <Header/>
      <b-nav v-if="dati_comune !== false && is_company_set === true && is_logged === true" class="mt-3" tabs align="center">
        <b-nav-item :hidden="dati_comune.ricavi_conai != 'IMPRESA' && section.num == 5 " class="text-danger" @click="goToSection(section.num)" style="cursor:pointer" v-for="section in sections" :key="section.num" :active="section.num === current_section">
          <p :class="section.class">
            {{section.text}}
          </p>
        </b-nav-item>
      </b-nav>

      <div class="container-fluid p-0 pb-0 mb-0 m-0 b-0" v-if="dati_comune !== false && is_company_set === true && is_logged === true && loaded === true">
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
            <b-col class="borders-rounded pt-5 pb-0 mb-0" offset-xl="1" xl="9">
              <ol class="p-0 m-0 b-0">
                <div v-bind:class="{'disabled-container' : azienda.report_is_sent || azienda.report_attempts <= 0 }" class="p-0 b-0 m-0" v-if="current_section === 1" @change="sections[0].edits = true">
                  <h3>Comune di {{dati_comune.nome_comune}}</h3>
                  <h3>{{sections[current_section-1].text}}</h3>
                  <p>
                    I campi in rosso sono obbligatori e, ove non diversamente specificato, sono riferiti all’annualità {{ new Date().getFullYear() - 2 }}.<br>
                    Compilare la pagina in ogni sua parte e premere il pulsante <b>SALVA</b> prima di passare alla pagina successiva.<br>
                    <!--Il pulsante <b>HELP</b> è in basso.-->
                  </p>
                  <div class="rounded shadow bg-light border p-3">
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
                  <b-container class="p-0 m-0 b-0" name="calc_o_mis" v-show="azienda.pef_mis_o_ric === 'CALCOLATO'">
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
                      <b-input-group append="€">
                        <b-form-input class="form-control" v-model="dati_comune.valore_can" type="text" :formatter="formatCurrency">
                        </b-form-input>
                      </b-input-group>
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
                      <FieldTitle  name="" description="Sono inclusi nel contratto e a carico dell'impresa anche i servizi di spazzamento e igiene ambientale?" />
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

                    <b-col :class="container_specs">
                      <FieldTitle name="idArera" description="ID Arera" />
                      <input class="form-control" v-model="dati_comune.idArera" type="text">
                    </b-col>

                    </b-row>
                  </div>
                </div>

                <div v-bind:class="{'disabled-container' : azienda.report_is_sent || azienda.report_attempts <= 0 }" class="p-0 b-0 m-0" v-if="current_section === 5 && dati_comune.ricavi_conai == 'IMPRESA'" @change="sections[1].edits = true">
                  <h3>Comune di {{dati_comune.nome_comune}}</h3>
                  <h4>MACRO-INDICATORE R1</h4>
                  Il MTR-2 aggiornato alle annualità 2024 – 2025 richiede la valorizzazione nel PEF del Macro – Indicatore R1,
                  un indicatore che tiene conto del risultato aggregato dell’efficienza e della qualità della raccolta
                  differenziata.<br>
                  Per individuare i valori che saranno oggetto di calcolo, è necessario <b> analizzare i dati esposti nelle
                  prefatture emesse da sistemi di compliance </b> (consorzi di filiera CONAI e altri)<b> di competenza</b> dell’anno a-2.<br>
                  I sistemi di compliance, infatti, emettono con cadenza mensile un documento che riassume i dati delle
                  quantità raccolte, delle quantità valorizzate e del risultato economico ottenuto.<br>
                  <b>Nel caso in cui i rifiuti di imballaggio</b> raccolti in modo differenziato <b> vengano sottoposti ad un trattamento
                  intermedio</b> di cernita, prima di essere avviati all’impianto di selezione, sarà <b> necessario specificare anche le
                  quantità complessive raccolte nell’anno a-2 e avviate a trattamento intermedio</b>.<br>
                  Le prefatture riferite a ciascun consorzio di filiera/rifiuto con il quale nell’anno a-2 era in essere un rapporto
                  contrattuale dovranno essere caricate in un file zip.
                  <table class="table table-striped table-bordered">
                    <thead class="thead-dark">
                      <tr>
                        <th v-for="field in efficienzaQualDifFFields">{{field.label}}</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(item,index) in efficienzaQualDiffItems">
                        <td v-for="field in efficienzaQualDifFFields">
                          <b-form-radio-group
                              :key="item.consorzio"
                              v-if="field.type == 'radio'"
                              v-model="item[field.key]"
                              @change=""
                              :name="item.consorzio">
                            <b-form-radio v-for="choice in field.choices" :key="choice" :value="choice.value">
                              {{choice.text}}
                            </b-form-radio>
                          </b-form-radio-group>
                          <b-input :name="item.consorzio" v-if="field.type == 'number' && item.pretrattamento" type="number" min="0" :placeholder="field.placeholder" v-model="item[field.key]"></b-input>
                          <b-form-file
                            v-if="field.type == 'file'"
                            v-model="item[field.key]"
                            placeholder=".zip"
                            :name="item.consorzio"
                            drop-placeholder="Rilascia file qui..."
                          ></b-form-file>
                          <div v-if="field.type == 'text' || (field.type == 'file' && item[field.key] != '[object File]')">
                            {{item[field.key]}}
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <div v-bind:class="{'disabled-container' : azienda.report_is_sent || azienda.report_attempts <= 0 }" class="p-0 b-0 m-0" v-if="current_section === 2" @change="sections[2].edits = true">
                  <b-container class="m-0 p-0 b-0">
                    <h3>Comune di {{dati_comune.nome_comune}}</h3>
                    <h3>Dati tecnici dell'appalto</h3>
                    <p>
                      I campi in rosso sono obbligatori e, ove non diversamente specificato, sono riferiti all’annualità {{new Date().getFullYear() - 2}}.<br>
                      Compilare la pagina in ogni sua parte e premere il pulsante <b>SALVA</b> prima di passare alla pagina successiva.<br>
                      <!--Il pulsante <b>HELP</b> è in basso.-->
                    </p>
                    <div class="rounded shadow bg-light border p-3">
                    <b-row>
                      <b-col xl="12">
                        <FieldTitle req="yes" name="tons" description="Quantitativi totali rifiuti raccolti [ton]" />
                      </b-col>
                    </b-row>
                    <b-row class="mb-4">
                      <b-col xl="4">
                        <FieldTitle letter="a" req="yes" name="" description="2022" />
                        <input class="form-control" v-model="dati_comune.ton_anno_1" type="number">
                      </b-col>
                      <b-col xl="4">
                        <FieldTitle letter="b" req="yes" name="" description="2023" />
                        <input class="form-control" v-model="dati_comune.ton_anno_2" type="number">
                      </b-col>
                      <b-col xl="4">
                        <FieldTitle letter="c" req="yes" name="" description="2024" />
                        <input class="form-control" v-model="dati_comune.ton_anno_3" type="number">
                      </b-col>
                    </b-row>
                    <hr>
                    <b-row>
                      <b-col xl="12">
                        <FieldTitle name="tons" req="yes" description="Percentuali raccolta differenziata" />
                      </b-col>
                    </b-row>
                    <b-row>
                      <b-col xl="4" >
                        <FieldTitle letter="a" req="yes" name="" description="2022" />
                        <input class="form-control" v-model="dati_comune.xcent_raccolta_anno_1" type="number">
                      </b-col>
                      <b-col xl="4">
                        <FieldTitle letter="b" req="yes" name="" description="2023" />
                        <input class="form-control" v-model="dati_comune.xcent_raccolta_anno_2" type="number">
                      </b-col>
                      <b-col xl="4">
                        <FieldTitle letter="c" req="yes" name="" description="2024" />
                        <input class="form-control" v-model="dati_comune.xcent_raccolta_anno_3" type="number">
                      </b-col>
                    </b-row>
                    </div>
                  </b-container>
                </div>

                <div v-bind:class="{'disabled-container' : azienda.report_is_sent || azienda.report_attempts <= 0 }" class="p-0 b-0 m-0" v-if="current_section === 3" @change="sections[3].edits = true">
                  <b-container class="m-0 p-0 b-0">
                    <h3>Comune di {{dati_comune.nome_comune}}</h3>
                    <h3>Documenti riferiti all'appalto</h3>
                    <p>
                      I campi in rosso sono obbligatori e, ove non diversamente specificato, sono riferiti all’annualità {{ new Date().getFullYear() - 2 }}.<br>
                      Compilare la pagina in ogni sua parte e premere il pulsante <b>SALVA</b> prima di passare alla pagina successiva.<br>
                      <!--Il pulsante <b>HELP</b> è in basso.-->
                    </p>
                    <div class="rounded shadow bg-light border p-3">

                    <b-row class="justify-content-start">
                      <b-col cols="12" md="6" :class="container_specs">
                        <FieldTitle req="yes" description="Contabilità di commessa anno 2023 (in excel)" />
                        <b-row>
                          <b-col cols="10">
                            <b-form-group>
                              <b-form-file
                                v-model="files.cont_commessa_anno_2"
                                placeholder="File Excel"
                                drop-placeholder="Rilascia qui...">
                              </b-form-file>
                              <font v-if="dati_comune.cont_commessa_anno_2 != '[object File]'">
                                {{dati_comune.cont_commessa_anno_2}}
                              </font>
                            </b-form-group>
                          </b-col>
                          <b-col cols="2" class="text-right">
                            <b-icon v-if="dati_comune.cont_commessa_anno_2 !== '' || files.cont_commessa_anno_2.length !== 0" 
                                    class="h4 p-0 b-0 m-0 mt-1" 
                                    variant="success" 
                                    icon="check-circle-fill">
                            </b-icon>
                            <b-icon v-if="dati_comune.cont_commessa_anno_2 === '' && files.cont_commessa_anno_2.length === 0" 
                                    class="h4 p-0 b-0 m-0 mt-1" 
                                    variant="danger" 
                                    icon="x-circle-fill">
                            </b-icon>
                          </b-col>
                        </b-row>
                      </b-col>
                      <b-col cols="12" md="6" :class="container_specs">
                        <FieldTitle req="yes" description="Contratto d'appalto vigente (in pdf)" />
                        <b-row>
                          <b-col cols="10">
                            <b-form-group>
                              <b-form-file
                                v-model="files.contratto_appalto"
                                placeholder="File PDF"
                                drop-placeholder="Rilascia qui...">
                              </b-form-file>
                              <font v-if="dati_comune.contratto_appalto != '[object File]'">
                                {{dati_comune.contratto_appalto}}
                              </font>
                            </b-form-group>
                          </b-col>
                          <b-col cols="2" class="text-right">
                            <b-icon v-if="dati_comune.contratto_appalto !== '' || files.contratto_appalto.length !== 0" 
                                    class="h4 p-0 b-0 m-0 mt-1" 
                                    variant="success" 
                                    icon="check-circle-fill">
                            </b-icon>
                            <b-icon v-if="dati_comune.contratto_appalto === '' && files.contratto_appalto.length === 0" 
                                    class="h4 p-0 b-0 m-0 mt-1" 
                                    variant="danger" 
                                    icon="x-circle-fill">
                            </b-icon>
                          </b-col>
                        </b-row>
                      </b-col>
                    </b-row>
                    <b-row class="justify-content-start">
                      <b-col xl="12" md="6">
                        <FieldTitle req="yes" description="PEF 2022 Validato dall'ETC (Delibera + Relazione + tool excel ARERA definitivo in unico file .zip)" />
                        <b-row>
                          <b-col cols="11">
                            <b-form-group>
                              <b-form-file
                                v-model="files.pef_valid_ETC_a_2"
                                placeholder="File Zip"
                                drop-placeholder="Rilascia qui...">
                              </b-form-file>
                              <font v-if="dati_comune.pef_valid_ETC_a_2 != '[object File]'">
                                {{dati_comune.pef_valid_ETC_a_2}}
                              </font>
                            </b-form-group>
                          </b-col>
                          <b-col cols="1" class="text-right">
                            <b-icon v-if="dati_comune.pef_valid_ETC_a_2 !== '' || files.pef_valid_ETC_a_2.length !== 0" 
                                    class="h4 p-0 b-0 m-0 mt-1" 
                                    variant="success" 
                                    icon="check-circle-fill">
                            </b-icon>
                            <b-icon v-if="dati_comune.pef_valid_ETC_a_2 === '' && files.pef_valid_ETC_a_2.length === 0" 
                                    class="h4 p-0 b-0 m-0 mt-1" 
                                    variant="danger" 
                                    icon="x-circle-fill">
                            </b-icon>
                          </b-col>
                        </b-row>
                      </b-col>
                    </b-row>
                    <b-row class="justify-content-start">
                      <b-col cols="12" md="6" :class="container_specs">
                        <FieldTitle req="no" description="CARICARE MUD anno a - 1" />
                        <b-row>
                          <b-col cols="10">
                            <b-form-group>
                              <b-form-file
                                v-model="files.mud_a_1"
                                placeholder="File Zip"
                                drop-placeholder="Rilascia qui...">
                              </b-form-file>
                              <font v-if="dati_comune.mud_a_1 != '[object File]'">
                                {{dati_comune.mud_a_1}}
                              </font>
                            </b-form-group>
                          </b-col>
                          <b-col cols="2" class="text-right">
                            <b-icon v-if="dati_comune.mud_a_1 !== '' || files.mud_a_1.length !== 0" 
                                    class="h4 p-0 b-0 m-0 mt-1" 
                                    variant="success" 
                                    icon="check-circle-fill">
                            </b-icon>
                            <b-icon v-if="dati_comune.mud_a_1 === '' && files.mud_a_1.length === 0" 
                                    class="h4 p-0 b-0 m-0 mt-1" 
                                    variant="danger" 
                                    icon="x-circle-fill">
                            </b-icon>
                          </b-col>
                        </b-row>
                      </b-col>
                      <b-col cols="12" md="6" :class="container_specs">
                        <FieldTitle req="no" description="CARICARE MUD anno a - 2" />
                        <b-row>
                          <b-col cols="10">
                            <b-form-group>
                              <b-form-file
                                v-model="files.mud_a_2"
                                placeholder="File Zip"
                                drop-placeholder="Rilascia qui...">
                              </b-form-file>
                              <font v-if="dati_comune.mud_a_2 != '[object File]'">
                                {{dati_comune.mud_a_2}}
                              </font>
                            </b-form-group>
                          </b-col>
                          <b-col cols="2" class="text-right">
                            <b-icon v-if="dati_comune.mud_a_2 !== '' || files.mud_a_2.length !== 0" 
                                    class="h4 p-0 b-0 m-0 mt-1" 
                                    variant="success" 
                                    icon="check-circle-fill">
                            </b-icon>
                            <b-icon v-if="dati_comune.mud_a_2 === '' && files.mud_a_2.length === 0" 
                                    class="h4 p-0 b-0 m-0 mt-1" 
                                    variant="danger" 
                                    icon="x-circle-fill">
                            </b-icon>
                          </b-col>
                        </b-row>
                
                      </b-col>
                    </b-row>
                  </div>

                  </b-container>
                </div>
              
              </ol>
            </b-col>
          </b-row>
        </b-container>

        <b-row v-bind:class="{'disabled-container' : azienda.report_is_sent || azienda.report_attempts <= 0 }" v-if="current_section === 4" class="ml-0 mr-3 mb-5 mt-0 pb-0 p-0 pb-5">
          <b-col>
            <h3>Comune di {{dati_comune.nome_comune}}</h3>
            <h3>Costi Smaltimento / Trattamento</h3>
            <p>
              Per inserire una nuova riga alla tabella premere il tasto <b>AGGIUNGI RIGA</b>. Il <b>SALVATAGGIO</b> è <b>AUTOMATICO</b>.
            </p>
            <table
              bordered
              fluid
              class="ml-0 mb-5 mt-5 pl-0 pb-5 b-0 custom-bordered-table"
              v-if="!loading"
            >
              <!-- Table Header -->
              <tr class="sticky-top bg-infowaste" style="height:30px; padding: 0;">
                <td
                  class="p-1 pl-0 pt-1 pb-1 border-theme"
                  :style="field.style"
                  v-for="field in costiFields"
                >
                  <b-button
                    size="sm"
                    class="h-100 w-100 p-1 pt-0 pb-0 border-dark"
                    @click="orderBy(field, costiFields, costi_smaltimento)"
                    variant="white"
                  >
                    {{ field.label }}
                    <b-icon
                      variant="primary"
                      v-if="field.order == -1"
                      icon="arrow-down"
                    ></b-icon>
                    <b-icon
                      variant="primary"
                      v-if="field.order == 0"
                      icon="arrow-down-up"
                    ></b-icon>
                    <b-icon
                      variant="primary"
                      v-if="field.order == 1"
                      icon="arrow-up"
                    ></b-icon>
                  </b-button>
                </td>
                <td
                  style="width:150px; justify-content: center; align-items: center;"
                  class="border-dark"
                >
                  <p class="pt-2 text-white text-center">AZIONI</p>
                </td>
              </tr>
              <tr class="bg-light rounded p-2" v-for="(item, index) in costi_smaltimento">
                <td v-for="field in costiFields" class="p-2 pl-3 border-dark">
                  <p v-if="field.type === 'euro'">
                    {{ item[field.key] }}€
                  </p>
                  <p v-else>
                    {{ item[field.key] }}
                  </p>
                </td>
                <td class="pt-1 pb-1 border-dark">
                  <b-container class="container">
                    <b-row class="row p-0 m-0">
                      <b-col class="xl-4 p-1 m-0">
                        <b-button
                          class="w-100 h-100 p-0"
                          v-b-modal.confermaEliminazione
                          @click="setRowtoDelete(item)"
                          variant="danger"
                        >
                          <b-icon icon="trash"></b-icon>
                        </b-button>
                      </b-col>
                      <b-col class="xl-4 p-1 m-0">
                        <b-button
                          class="w-100 h-100 p-0"
                          v-b-modal.editRow
                          @click="editingRow(item)"
                          variant="infowaste"
                        >
                          <b-icon icon="pencil"></b-icon>
                        </b-button>
                      </b-col>
                    </b-row>
                  </b-container>
                </td>
              </tr>
              <tr v-if="costi_smaltimento.length == 0">
                <td colspan="100%">
                La tabella è vuota
                </td>
              </tr>
            </table>
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
          <b-row class="row" v-if="current_section == 4">
            <b-col class="xl-1 offset-xl-10">
              <b-button v-b-modal.addRow block variant="success">
                  AGGIUNGI RIGA
              </b-button>
            </b-col>
          </b-row>
          <b-row class="row" v-else>
            <b-col class="xl-1 offset-xl-10">
              <b-button block @click="saveDatiComune(dati_comune,files)" variant="infowaste">
                  Salva
              </b-button>
            </b-col>
          </b-row>
        </b-container>
      </div>

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

      <!--ROW EDITING-->
      <b-modal
        v-if="item !== undefined"
        id="editRow"
        title="Modifica"
        ok-title="Salva"
        ok-variant="infowaste"
        cancel-title="Annulla"
        cancel-variant="danger"
        size="lg"
        class="custom-modal"
        @ok.prevent="editRow"
        >
        <b-container class="container p-3 m-0" @change="sections[4].edits = true">
          <!-- Group fields in pairs -->
          <b-row class="row p-2 m-0" v-for="rowIndex in Math.ceil(costiFields.length / 2)" :key="rowIndex">
            <!-- Two fields per row -->
            <b-col
              class="offset-xl-0 xl-6 offset-sm-0 sm-12 p-3 m-0 ml-1 mr-1 bg-light rounded border text-sm"
              v-for="colField in costiFields.slice((rowIndex - 1) * 2, rowIndex * 2)"
              :key="colField.key"
            >
              <label class="form-label text-sm">{{ colField.label }}</label>
              <template v-if="colField.type === 'text'">
                <b-input
                  class="mb-3 text-sm"
                  :disabled="colField.disabled"
                  :type="colField.type"
                  v-model="item[colField.key]"
                ></b-input>
              </template>
              <template v-else-if="colField.type === 'select'">
                <b-select
                  class="mb-3 text-sm"
                  :disabled="colField.disabled"
                  :options="colField.choices"
                  v-model="item[colField.key]"
                ></b-select>
              </template>
              <template v-else-if="colField.type === 'number'">
                <b-input
                  class="mb-3 text-sm"
                  :disabled="colField.disabled"
                  @input="calcoloImportoItem(item,colField.key)"
                  min="0"
                  :type="colField.type"
                  :value="colField.default"
                  v-model="item[colField.key]"
                ></b-input>
              </template>
              <template v-else-if="colField.type === 'euro'">
                <b-input-group append="€" class="text-sm">
                    <b-form-input
                      :ref="colField.key"
                      :placeholder="colField.placeholder" 
                      v-model="item[colField.key]"
                      type="text"
                      @input="calcoloImportoItem(item,colField.key)"
                      :formatter="formatCurrency">
                    </b-form-input>
                  </b-input-group>
              </template>
              <template v-else-if="colField.type === 'textarea'">
                <b-form-textarea
                  class="mb-3 text-sm"
                  :disabled="colField.disabled"
                  v-model="item[colField.key]"
                  rows="4"
                  max-rows="8"
                ></b-form-textarea>
              </template>
              <b-alert
                variant="danger"
                fade
                show
                v-if="editingItemMessages[colField.key]"
                class="mt-2"
              >
                {{ editingItemMessages[colField.key] }}
              </b-alert>
            </b-col>
          </b-row>
        </b-container>
      </b-modal>

      <!--ROW ADDING-->
      <b-modal
        @change="sections[4].edits = true"
        id="addRow"
        title="Modifica"
        ok-title="Aggiungi"
        ok-variant="success"
        cancel-title="Annulla"
        cancel-variant="danger"
        size="lg"
        class="custom-modal"
        @ok.prevent="addRow"
        >
        <b-container class="container p-3 m-0">
          <!-- Group fields in pairs -->
          <b-row class="row p-2 m-0" v-for="rowIndex in Math.ceil(costiFields.length / 2)" :key="rowIndex">
            <!-- Two fields per row -->
            <b-col
              class="offset-xl-0 xl-6 offset-sm-0 sm-12 p-3 m-0 ml-1 mr-1 bg-light rounded border text-sm"
              v-for="colField in costiFields.slice((rowIndex - 1) * 2, rowIndex * 2)"
              :key="colField.key"
            >
              <label class="form-label text-sm">{{ colField.label }}</label>
              <template v-if="colField.type === 'text'">
                <b-input
                  class="mb-3 text-sm"
                  :disabled="colField.disabled"
                  :type="colField.type"
                  v-model="newItem[colField.key]"
                ></b-input>
              </template>
              <template v-else-if="colField.type === 'select'">
                <b-select
                  class="mb-3 text-sm"
                  :disabled="colField.disabled"
                  :options="colField.choices"
                  v-model="newItem[colField.key]"
                ></b-select>
              </template>
              <template v-else-if="colField.type === 'number'">
                <b-input
                  class="mb-3 text-sm"
                  :disabled="colField.disabled"
                  min="0"
                  @input="calcoloImportoItem(newItem,colField.key)"
                  :type="colField.type"
                  :value="colField.default"
                  v-model="newItem[colField.key]"
                ></b-input>
              </template>
              <template v-else-if="colField.type === 'euro'">
                <b-input-group append="€" class="text-sm">
                    <b-form-input
                      :ref="colField.key"
                      :placeholder="colField.placeholder" 
                      v-model="newItem[colField.key]"
                      @input="calcoloImportoItem(newItem,colField.key)"
                      type="text"
                      :formatter="formatCurrency">
                    </b-form-input>
                  </b-input-group>
              </template>
              <template v-else-if="colField.type === 'textarea'">
                <b-form-textarea
                  class="mb-3 text-sm"
                  :disabled="colField.disabled"
                  v-model="newItem[colField.key]"
                  rows="4"
                  max-rows="8"
                ></b-form-textarea>
              </template>
              <b-alert
                variant="danger"
                fade
                show
                v-if="newItemMessages[colField.key]"
                class="mt-2">
                {{ newItemMessages[colField.key] }}
              </b-alert>
            </b-col>
          </b-row>
        </b-container>
      </b-modal>

      <b-modal id="confermaEliminazione" @ok="deleteRow(),edits=true" ok-variant="danger" cancel-variant="infowaste" ok-title="Si" cancel-title="Annulla" title="Conferma" v-if="rowtoDelete">
        <p class="my-2">
           Sei sicuro di voler eliminare la riga selezionata ?
        </p>
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


        this.$axios.$get(`/is_company_set`)
        .then((response) => {
          this.is_company_set = response
          this.$axios.$get(`/is_logged`)
          .then((response) => {
            this.is_logged = response
            this.$axios.$get(`/role`)
            .then((response) => {
              this.role = response
              this.$axios.$get(`/getEfficienzaQualitaDifferenziata`)
              .then((response) => {
                this.efficienzaQualDiffItems = response
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


                  if (this.dati_comune.ton_anno_1 === 0  || this.dati_comune.ton_anno_2 === 0 || this.dati_comune.ton_anno_3 === 0 ||
                  this.dati_comune.xcent_raccolta_anno_1 === 0 || this.dati_comune.xcent_raccolta_anno_2 === 0 || this.dati_comune.xcent_raccolta_anno_3 === 0)
                  {
                    this.sections[2].completed = 0
                  }else {
                    this.sections[2].completed = 1

                  }



                  if(this.dati_comune.cont_commessa_anno1 == '' || this.dati_comune.cont_commessa_anno2 == '' || this.dati_comune.contratto_appalto == '')
                  {
                    this.sections[3].completed = 0
                  }

                  this.current_section = this.dati_comune['current_section']
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
                    for (const section of this.sections){

                      if (section.num >= 1 && section.num  <= 3)
                      {
                          if (section.completed)
                            section.class = 'text-success'
                          else
                            section.class = 'text-danger'
                      }
                      else
                      {
                        section.class = 'text-primary'
                      }
                    }
                      //Converto il valore testuale in euro
                      // Ensure the value is a number, then convert it to fixed 2 decimal places and replace the dot with a comma
                      this.dati_comune.valore_can = parseFloat(this.dati_comune.valore_can).toFixed(2).replace(".", ",");

                      // Check if the length of the string is sufficient to apply formatting
                      if (this.dati_comune.valore_can.length >= 4) {

                        // Split the value into integer and decimal parts
                        let [integerPart, decimalPart] = this.dati_comune.valore_can.split(',');

                        // Format the integer part by adding periods every 3 digits
                        let formattedInteger = '';
                        let digitsCount = 0;

                        // Loop over the integer part from right to left
                        for (let i = integerPart.length - 1; i >= 0; i--) {
                          let char = integerPart[i];

                          // If it's a digit and we need to add a separator every 3 digits
                          if (digitsCount > 0 && digitsCount % 3 === 0) {
                            formattedInteger = "." + formattedInteger;  // Add the separator (dot)
                          }

                          formattedInteger = char + formattedInteger;
                          digitsCount++;
                        }

                        // Combine the integer part with the decimal part (if it exists)
                        if (decimalPart) {
                          this.dati_comune.valore_can = formattedInteger + "," + decimalPart; // Add the decimal part with comma
                        } else {
                          this.dati_comune.valore_can = formattedInteger;  // No decimal part
                        }
                      }


                    this.$axios.$post(`/get_costi_smaltimento` ,{id: this.id})
                    .then((response) => {
                      this.costi_smaltimento = response

                      //Preparo il nuovo item per l'aggiunta
                      this.newItem = {}
                      if (this.costiFields && Array.isArray(this.costiFields)) {
                        for (const field of this.costiFields) {
                          this.newItemMessages[field.key] = "";
                        }
                      }

                      this.items = response
                      for(const item of this.items)
                      {
                        item.importo = item.importo.toFixed(2).replace(".", ",");
                        item.prezzo_unitario = item.prezzo_unitario.toFixed(2).replace(".", ",");

                        item.importo = this.addDots(item.importo)
                        item.prezzo_unitario = this.addDots(item.prezzo_unitario)

                        item.editing=false
                        item.error=""
                      }
                      this.items = this.items.sort((t1,t2) => t1["id"] > t2["id"] ? -1 : 1)

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

    methods:
    {
        formatCurrency(value) {
          this.formatting = true
          // Remove decimals, keeping only two digits after the comma
          value = this.rimuoviDecimali(value,2);
          // Clean the value and remove invalid characters
          value = this.eliminaCaratteri(value);

          this.formatting=false
          return value;
        },
        
        eliminaCaratteri(str) {
            let result = '';
            let commaFound = false;
            for (let i = 0; i < str.length; i++) {
              if (str[i] >= "0" && str[i] <= "9") {
                result += str[i];
              }
              if (str[i] === '.') {
                result += str[i];
              }
              if (str[i] === ',' && !commaFound) {
                result += str[i];
                commaFound = true;
              }
            }
            return result;
        },

        rimuoviDecimali(str, maxDec) {
          let commaIndex = str.indexOf(",");
          if (commaIndex === -1) return str; // No decimals

          let integerPart = str.slice(0, commaIndex);
          let decimalPart = str.slice(commaIndex + 1, commaIndex + 1 + maxDec);

          return integerPart + ',' + decimalPart;
        },

        setRowtoDelete(item)
        {
          this.rowtoDelete = item
        },

        deleteRow()
        {
          this.loading = true
          this.$axios.post('/del_costi_smaltimento', {
                daticomune: this.dati_comune.id,
                id: this.rowtoDelete['id'],
              })
              .then((response) => {
                  this.loading = false
                  window.location.reload()
              })
        },

        async goToSection(num)
        {
           if (num >= 1 &&  num <= this.sections.length  && num !== this.current_section)
           {
                for(var i=0; i < this.sections.length; i++){
                  if(this.sections[i].num == this.current_section){
                    if(this.sections[i].edits == true){
                      this.$bvModal
                      .msgBoxConfirm('Sei sicuro di voler cambiare pagina? Le modifiche non salvate andranno perse', {
                        title: 'Conferma Azione',
                        okTitle: 'Conferma',
                        cancelTitle: 'Annulla',
                        okVariant: 'infowaste',
                        cancelVariant: 'danger',
                        centered: true, // Optional: centers the modal
                      })
                      .then(value => {
                        if(value == true){
                          this.current_section = num
                          this.updateSection();
                          window.location.reload();
                        }
                      })
                      .catch(err => {
                        // An error occurred
                      })
                    }else{
                      this.current_section = num
                    }
                  }
                }
            }
        },

        async uploadFiles(dati_comune)
        {

            var formData = new FormData();
            var upload = false


            if(dati_comune.cont_commessa_anno_2 == '[object File]')
            {
              upload = true
              dati_comune.cont_commessa_anno_2 = new File([dati_comune.cont_commessa_anno_2],dati_comune.cont_commessa_anno_2.name)
              formData.append("cont_commessa_anno_2", dati_comune.cont_commessa_anno_2,dati_comune.cont_commessa_anno_2.name);
            }

            if(dati_comune.contratto_appalto == '[object File]')
            {
              upload = true
              dati_comune.contratto_appalto = new File([dati_comune.contratto_appalto],dati_comune.contratto_appalto.name)
              formData.append("contratto_appalto", dati_comune.contratto_appalto,dati_comune.contratto_appalto.name);
            }

            if(dati_comune.pef_valid_ETC_a_2 == '[object File]')
            {
              upload = true
              dati_comune.pef_valid_ETC_a_2 = new File([dati_comune.pef_valid_ETC_a_2],dati_comune.pef_valid_ETC_a_2.name)
              formData.append("pef_valid_ETC_a_2", dati_comune.pef_valid_ETC_a_2,dati_comune.pef_valid_ETC_a_2.name);
            }

            if(dati_comune.mud_a_1 == '[object File]')
            {
              upload = true
              dati_comune.mud_a_1 = new File([dati_comune.mud_a_1],dati_comune.mud_a_1.name)
              formData.append("mud_a_1", dati_comune.mud_a_1,dati_comune.mud_a_1.name);
            }

            if(dati_comune.mud_a_2 == '[object File]')
            {
              upload = true
              dati_comune.mud_a_2 = new File([dati_comune.mud_a_2],dati_comune.mud_a_2.name)
              formData.append("mud_a_2", dati_comune.mud_a_2,dati_comune.mud_a_2.name);
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
              }).then((response) => {
                  location.reload()
              })
            }else {
              location.reload()

            }

        },

        editingRow(row) {
          if (!row) return; // Ensure row is valid

          // Reset editing state and set the selected row to editing in one loop
          for (const item of this.costi_smaltimento) {
            this.$set(item, 'editing', item.id === row.id);
          }

          // Update component state
          this.itemID = row.id;
          this.item = JSON.parse(JSON.stringify(row)); // Deep clone to avoid mutations

          // Ensure editingItemMessages exists
          if (!this.editingItemMessages) {
            this.editingItemMessages = {};
          }

          // Reset messages
          if (this.costiFields && Array.isArray(this.costiFields)) {
            for (const field of this.costiFields) {
              this.editingItemMessages[field.key] = "";
            }
          }
        },

        validateEditItem()
        {
          var field = ""
          var valid = true
          for(const field of this.costiFields){
            if(field.key!= 'id'){
              if (this.item[field.key] === "" || this.item[field.key] === null || this.item[field.key] === undefined){
                this.editingItemMessages[field.key] = "Campo obbligatorio"
                valid = false
              }else {
                this.editingItemMessages[field.key] = ""
              }
              if(field.key === 'partitaIvaGestoreImpianto')
              {
                this.editingItemMessages[field.key] = this.controllaPartitaIVA(this.item[field.key]);
                if( this.editingItemMessages[field.key].length > 0)
                valid=false
              }
            }
          }
          this.$forceUpdate()
          return valid
        },

        editRow(){
          if(this.validateEditItem() == true){
            this.loading = true
            this.item.importo = this.item.importo.replace(/\./g, "");
            this.item.importo = parseFloat(this.item.importo.replace(",", "."));

            this.item.prezzo_unitario = this.item.prezzo_unitario.replace(/\./g, "");
            this.item.prezzo_unitario = parseFloat(this.item.prezzo_unitario.replace(",", "."));

            this.$axios.post('/update_costi_smaltimento', {
                  data: this.item,
                })
                .then((response) => {
                    this.loading = false
                    this.updateSection();
                    window.location.reload()
                })
          }
        },

        addDots(value){
          if (value.length >= 4) {

            // Split the value into integer and decimal parts
            let [integerPart, decimalPart] = value.split(',');

            // Format the integer part by adding periods every 3 digits
            let formattedInteger = '';
            let digitsCount = 0;

            // Loop over the integer part from right to left
            for (let i = integerPart.length - 1; i >= 0; i--) {
              let char = integerPart[i];

              // If it's a digit and we need to add a separator every 3 digits
              if (digitsCount > 0 && digitsCount % 3 === 0) {
                formattedInteger = "." + formattedInteger;  // Add the separator (dot)
              }

              formattedInteger = char + formattedInteger;
              digitsCount++;
            }

            // Combine the integer part with the decimal part (if it exists)
            if (decimalPart) {
              value = formattedInteger + "," + decimalPart; // Add the decimal part with comma
            } else {
              value = formattedInteger;  // No decimal part
            }
            return value;
          }
        },

        controllaPartitaIVA(partitaIVA)
        {
            if (partitaIVA.length !== 11)
                return "La Partita IVA deve contenere 11 cifre."
            if (!/^\d+$/.test(partitaIVA))
                return "Partita IVA non valida."
            return ""

        },

        validateNewItem(){
          var valid = true
          for(const field of this.costiFields)
          {
            if(field.key!= 'id')
            {
                if (this.newItem[field.key] === "" || this.newItem[field.key] === null || this.newItem[field.key] === undefined)
                {
                  this.newItemMessages[field.key] = "Campo obbligatorio"
                  valid = false
                }
                else if(field.key === 'partitaIvaGestoreImpianto')
                {
                  this.newItemMessages[field.key] = this.controllaPartitaIVA(this.newItem[field.key]);
                  this.$forceUpdate()
                  if(this.controllaPartitaIVA(this.newItem[field.key]).length > 0)
                  valid=false
                }else {
                  this.newItemMessages[field.key] = ""
                }
            }
          }
          this.$forceUpdate()
          return valid
        },

        addRow() {
            if (this.newItem) {
                if (this.validateNewItem() === true) {
                    this.loading = true;

                    // Convert `importo` and `prezzo_unitario` to proper formats
                    this.newItem.importo = this.newItem.importo.replace(/\./g, "");
                    this.newItem.importo = parseFloat(this.newItem.importo.replace(",", "."));

                    this.newItem.prezzo_unitario = this.newItem.prezzo_unitario.replace(/\./g, "");
                    this.newItem.prezzo_unitario = parseFloat(this.newItem.prezzo_unitario.replace(",", "."));


                    this.newItem.daticomune = this.dati_comune['id']
                    // Send the request with the `data` wrapper
                    this.$axios
                        .post("/add_costi_smaltimento", {
                            data: this.newItem,
                        })
                        .then((response) => {
                            this.loading = false;
                            if (response.data && !response.data.error) {
                                // Successfully added the item
                                this.updateSection();
                                window.location.reload();
                            } else {
                                // Handle error response
                                alert(response.data.error || "Si è verificato un errore");
                            }
                        })
                        .catch((error) => {
                            this.loading = false;
                            console.error("Error:", error);
                            alert("Impossibile aggiungere i dati");
                        });
                }
            }
        },

        async calcoloImportoItem(item,key)
        {
          if(key == "tons" || key == "prezzo_unitario"){
            
            // Ensure prezzo_unitario and tonnellate are properly initialized
            let prezzoUnitario = item.prezzo_unitario || '0';
            let tonnellate = item.tons || '0';

            // Convert prezzo_unitario to a string if it's not already
            if (typeof prezzoUnitario !== 'string') {
              prezzoUnitario = prezzoUnitario.toString();
            }

            // Replace commas with periods for float conversion
            prezzoUnitario = prezzoUnitario.replace(/\./g, "");
            prezzoUnitario = prezzoUnitario.replace(',', '.');
            
            // Parse both values
            const prezzoUnitarioNumber = parseFloat(prezzoUnitario);
            const tonnellateNumber = parseFloat(tonnellate);

            // Only calculate if both values are valid numbers
            if (!isNaN(prezzoUnitarioNumber) && !isNaN(tonnellateNumber)) {
              // Calculate importo and format to 2 decimal places
              item.importo = (tonnellateNumber * prezzoUnitarioNumber).toFixed(2).replace('.', ',');
              
              // Ensure Vue updates the UI
              this.$forceUpdate();
            }
          }
        },

        updateSection()
        {
          this.$axios.post('/update_compiling_section', {
            azienda : this.dati_comune.azienda,
            id: this.dati_comune.id,
            current_section: this.current_section
            })
            .catch(error => {
                console.log(error)
            });
        },

        orderBy(field,fields,items)
        {
          //set fields order to 0
          for (var i = 0; i < fields.length; i++)
          {
            if (field.key != fields[i].key)
            {
              fields[i].order = 0
            }
          }

          if (field.order == 0)
          {
            field.order = 1
          }
          else {
            field.order = field.order * -1
          }

          if (field.order == -1)
          {
            items = items.sort((t1,t2) => t1[field.key] > t2[field.key] ? -1 : 1)

          }
          if (field.order == 1)
          {
            items = items.sort((t1,t2) => t1[field.key] < t2[field.key] ? -1 : 1)

          }
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

          //converto la valuta in numero di macchina
          dati_comune.valore_can = dati_comune.valore_can.replace(/\./g, "");
          dati_comune.valore_can = parseFloat(dati_comune.valore_can.replace(",", "."));
            
          

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


          if(files.cont_commessa_anno_2 != '[object File]' && dati_comune.cont_commessa_anno_2 == '')
          {
            is_completed = 0
          }

          if(files.contratto_appalto != '[object File]' && dati_comune.contratto_appalto == '')
          {
            is_completed = 0
          }

          if(files.pef_valid_ETC_a_2 != '[object File]' && dati_comune.pef_valid_ETC_a_2 == '')
          {
            is_completed = 0
          }

          /* Non sono obbligatori
          if(files.mud_a_1 != '[object File]' && dati_comune.mud_a_1 == '')
          {
              is_completed = 0
          }
            
          if(files.mud_a_2 != '[object File]' && dati_comune.mud_a_2 == '')
          {
              is_completed = 0
          }*/



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
            idArera: dati_comune.idArera,

            current_section: this.current_section,
            completed: is_completed

          })

          .then(response => {

              var formData = new FormData();
              var upload = false
              var file = false
              //this.loading=true

              for (const item of this.efficienzaQualDiffItems)
              {
                if (item.prefatture_a_2 == '[object File]')
                {
                  file = new File([item.prefatture_a_2],item.prefatture_a_2.name)
                  formData.append(item.consorzio, file ,file.name)
                }
                  formData.append(item.consorzio, item.quantita_in_ton)
                  formData.append(item.consorzio, item.pretrattamento)
              }
              formData.append('comune',this.dati_comune.comune)
              this.$axios.post('/saveEfficienzaQualitaDifferenziata', formData,{
                headers: {
                  'Content-Type': "multipart/form-data; charset='utf-8';",

                },
              }).then((response) => {
                //window.location.reload()
                this.uploadFiles(this.files)
                })

          })

          .catch(error => {

              this.save.msg = error
              this.save.color = "Errore nel salvataggio dati, se il problema persiste , contattare l'assistenza"
              this.$bvModal.show('bv-modal-save-msg')

          });


        }
    },


    data()
    {
      const booleanChoices = [{"value":true,"text":"SI"},{"value":false,"text":"NO"}]
      const tipologieImpiantoChoices = [{value:'Compostaggio',text:'Compostaggio'},
                  {value:'Digestione Anaerobica',text:'Digestione Anaerobica'},
                  {value:'Integrato Aerobico/Anaerobico',text:'Integrato Aerobico/Anaerobico'},
                  {value:'Incenerimento con recupero di energia R1',text:'Incenerimento con recupero di energia R1'},
                  {value:'Incenerimento senza recupero di energia D10',text:'Incenerimento senza recupero di energia D10'},
                  {value:'TMB/TM',text:'TMB/TM'},{value:'Discarica',text:'Discarica'}]


        return {
                  rowEditingError:undefined,
                  rowtoDelete:undefined,
                  itemID:undefined,
                  item:undefined,
                  editingItemMessages:{},
                  newItemMessages:{},
                  newItem:0,

                  is_logged:undefined,
                  is_company_set:undefined,
                  loaded:false,
                  role:'Normal',
                  dati_comune:[],
                  azienda:[],
                  efficienzaQualDifFFields: [
                    { key:'consorzio',label: 'Consorzio di filiera /Rifiuto',type:'text',default:0},
                    { key:'pretrattamento',label: 'Pretrattamento (impianto intermedio)',type:'radio',choices:booleanChoices},
                    { key:'quantita_in_ton',label: 'Quantità in tonnellate raccolte e trasportate a pretrattamento / impianto intermedio [ton.]',type:'number',default:0},
                    { key:'prefatture_a_2',label: 'Upload file .zip prefatture competenza a-2',type:'file',default:0}
                  ],
                  efficienzaQualDiffItems: undefined,
                  sections:[
                    {num:1 , text:"Dati Generali",completed:1,edits:false},
                    {num:5 , text:"Efficienza e qualità differenziata a-2",completed:1,edits:false},
                    {num:2 , text:"Dati tecnici dell'appalto",completed:1,edits:false},
                    {num:3 , text:"Documenti riferiti all'appalto",completed:1,edits:false},
                    {num:4 , text:"Costi Smaltimento / Trattamento",completed:1,edits:false}
                  ],
                  costi_smaltimento:[],
                  current_section:0,
                  id:0,

                  files:{
                    cont_commessa_anno_2:[],
                    contratto_appalto:[],
                    pef_valid_ETC_a_2:[],
                    mud_a_1:[],
                    mud_a_2:[]
                  },

                  width:0,
                  page_id:0,
                  save:{
                    msg:'',
                    color:''

                  },
                  add:{
                      gestore:"",
                      imp_smalt:"",
                      tipo_rifiuto:"",
                      tipo_costo:"CTS",
                      anno:"2022",
                      tons:0,
                      prezzo_unitario:0,
                      importo:0,
                      msg:{

                        imp_smalt:"",
                        tipo_rifiuto:"",
                        partitaIvaGestoreImpianto:""
                      },

                      tipoImpianto:"",
                      gestoreImpianto:"",
                      partitaIvaGestoreImpianto:"",
                      comuneSedeImpianto:"",
                      impiantoDestinazione:"",
                      note:"",
                  },
                  costiFields: [
                    { style: 'height:30px;width:6.5%', order: 0, type: 'select', key: 'gestore', label: 'Gestore che sostiene i costi di tr', choices: ['GESTORE', 'COMUNE'], model: 'add.gestore' },
                    //{ style: 'height:30px;width:6.5%', order: 0, type: 'select', key: 'gestore', label: 'Gestore che sostiene i costi di trattamento/recupero/smaltimento', choices: ['GESTORE', 'COMUNE'], model: 'add.gestore' },
                    { style: 'height:30px;width:6.5%', order: 0, type: 'select', key: 'anno', label: 'Anno', choices: ['2023', '2024'], model: 'add.anno' },
                    { style: 'height:30px;width:10%', order: 0, type: 'textarea', key: 'imp_smalt', label: 'Impianto di smaltimento', model: 'add.imp_smalt', alertMessage: 'add.msg.imp_smalt' },
                    { style: 'height:30px;width:12%', order: 0, type: 'textarea', key: 'tipo_rifiuto', label: 'Codice CER/Tipo di rifiuto', model: 'add.tipo_rifiuto', alertMessage: 'add.msg.tipo_rifiuto' },
                    { style: 'height:30px;width:8%', order: 0, type: 'select', key: 'tipo_costo', label: 'Tipologia costo', choices: ['CTS', 'CTR'], model: 'add.tipo_costo' },
                    { style: 'height:30px;width:10%', order: 0, type: 'number', key: 'tons', label: 'Quantitativi conferiti [ton]', model: 'add.tons', onChange: 'calcoloImporto()' },
                    { style: 'height:30px;width:10%', order: 0, type: 'euro', key: 'prezzo_unitario', label: 'Prezzo unitario con IVA [€/ton]', model: 'add.prezzo_unitario', onChange: 'calcoloImporto()' },
                    { style: 'height:30px;width:10%', order: 0, type: 'euro', key: 'importo', label: 'Importo IVA Inclusa', model: 'add.importo' },
                    { style: 'height:30px;width:12%', order: 0, type: 'select', key: 'tipoImpianto', label: 'Tipologia impianto di destinazione', choices: tipologieImpiantoChoices, model: 'add.tipoImpianto' },
                    { style: 'height:30px;width:9%', order: 0, type: 'text', key: 'gestoreImpianto', label: 'Gestore Impianto', model: 'add.gestoreImpianto' },
                    { style: 'height:30px;width:9%', order: 0, type: 'text', key: 'partitaIvaGestoreImpianto', label: 'Partita IVA Gestore Impianto', model: 'add.partitaIvaGestoreImpianto', alertMessage: 'add.msg.partitaIvaGestoreImpianto' },
                    { style: 'height:30px;width:9%', order: 0, type: 'text', key: 'comuneSedeImpianto', label: 'Comune sede Impianto', model: 'add.comuneSedeImpianto' },
                    //{ style: 'height:30px;width:14%', order: 0, type: 'text', key: 'impiantoDestinazione', label: 'In caso di invio a impianto intermedio, indicare impianto di destinazione finale dei flussi in uscita', model: 'add.impiantoDestinazione' },
                    { style: 'height:30px;width:14%', order: 0, type: 'text', key: 'impiantoDestinazione', label: 'impianto di destinazione finale ', model: 'add.impiantoDestinazione' },
                    { style: 'height:30px;width:6%', order: 0, type: 'textarea', key: 'note', label: 'NOTE', model: 'add.note' }
                  ],



                  container_specs:'col-12 col-xl-6 p-2 pl-3 pr-3 mt-1 mb-1',
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
