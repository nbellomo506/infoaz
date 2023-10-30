
import Header from '../components/Header'
import Footer from '../components/Footer'

<template>
  <main>
    <Header/>
    <b-container mt="5" >

      <b-row>
        <b-col disabled="true" xl="6" offset-xl="3" class="justify-content-center p-3 pb-0 mt-5">
          <b-button variant="infowaste" to="./login"><b-icon icon="arrow-90deg-left"></b-icon> Indietro</b-button>
        </b-col>
      </b-row>

      <b-row>
        <b-col disabled="true" xl="6" offset-xl="3" class="justify-content-center p-3 pb-0">
          <h1>Registrazione</h1>
          <hr>
        </b-col>
      </b-row>

        <b-row class="mr-1 ml-1 mt-4">
          <b-col disabled="true" xl="6" offset-xl="3" class="justify-content-center shadow p-3 mt-2 bg-white rounded">
              <b-container  class="p-0 m-0 b-0">
                  <b-row>
                    <b-col xl="6">
                      <b-form-group label="Nome">
                        <b-form-input ref="nome" id="nome" @change="controlloNome()" v-model="form.nome" type="text"></b-form-input>
                      </b-form-group>
                      <b-alert v-if="msg.nome.length > 0" show variant="danger">{{msg.nome}}</b-alert>
                    </b-col>
                    <b-col xl="6">
                      <b-form-group label="Cognome">
                        <b-form-input ref="cognome" id="cognome" @change="controlloCognome()" v-model="form.cognome" type="text"></b-form-input>
                      </b-form-group>
                      <b-alert v-if="msg.cognome.length > 0" show variant="danger">{{msg.cognome}}</b-alert>
                    </b-col>
                  </b-row>
                  <hr>

                    <b-row>
                      <b-col>
                        <b-form-group label="Titolo">
                          <b-form-select ref="titolo" v-model="form.titolo" @change="controlloTitolo()" :options="titoli"></b-form-select>
                        </b-form-group>
                        <b-alert v-if="msg.titolo.length > 0" show variant="danger">{{msg.titolo}}</b-alert>
                      </b-col>
                    </b-row>
                    <hr>
                    <b-row>
                      <b-col>
                        <b-form-group label="Azienda">
                          <b-form-input ref="ragione_sociale" class="mb-2" id="ragione_sociale" v-model="form.ragione_sociale" type="text" placeholder="Ragione Sociale" ></b-form-input>
                          <b-form-input class="mt-2" id="p_iva" v-model="form.p_iva" maxlength="11" type="text" placeholder="Partita Iva" ></b-form-input>
                        </b-form-group>
                        <b-alert v-if="msg.azienda.length > 0" show variant="danger">{{msg.azienda}}</b-alert>
                      </b-col>
                    </b-row>
                    <hr>
                    <b-row>
                      <b-col>
                        <b-form-group label="Telefono">
                          <b-form-input ref="telefono" class="mt-2" id="telefono" v-model="form.telefono" maxlength="10" type="text" ></b-form-input>
                        </b-form-group>
                        <b-alert v-if="msg.telefono.length > 0" show variant="danger">{{msg.telefono}}</b-alert>
                      </b-col>
                    </b-row>
                    <hr>
                    <b-row>
                      <b-col>
                        <b-form-group label="Email">
                          <b-form-input ref="emIL" id="email" v-model="form.email" type="email" ></b-form-input>
                        </b-form-group>
                        <b-alert v-if="msg.email.length > 0" show variant="danger">{{msg.email}}</b-alert>

                        <b-form-group label="Email Secondaria">
                          <b-form-input id="email2" v-model="form.email2" type="email" ></b-form-input>
                        </b-form-group>
                        <b-alert v-if="msg.email2.length > 0" show variant="danger">{{msg.email2}}</b-alert>
                      </b-col>
                    </b-row>
                    <hr>

                    <b-row>
                      <b-col>
                        <b-form-group label="Password">
                          <b-form-input ref="password" id="password" @change=controlloPassword() v-model="form.password" type="password" ></b-form-input>
                        </b-form-group>

                        <b-form-group label="Conferma Password">
                          <b-form-input id="conferma_password" @change=controlloPassword() v-model="form.conferma_password" type="password" ></b-form-input>
                        </b-form-group>
                        <b-alert v-if="msg.password.length > 0" show variant="danger">{{msg.password}}</b-alert>
                      </b-col>
                    </b-row>

                    <b-row class="pb-2 pt-2">
                      <b-col>
                        <b-form-checkbox
                          :disabled="!form.check.serv.attivo"
                          v-model="form.check.serv.value"
                          value="1"
                          unchecked-value="0">
                          Accetto <a target="_blank" @click="form.check.serv.attivo = true" href="./files/Rev01_CONDIZIONI_USO_DEL%20SERVIZIO.pdf">Informativa Uso del Servizio</a>
                        </b-form-checkbox>
                        <b-alert v-if="msg.check.serv.length > 0" show variant="danger">{{msg.check.serv}}</b-alert>

                      </b-col>

                    </b-row>

                    <b-row class="pb-2 pt-2">
                      <b-col>
                        <b-form-checkbox
                          :disabled="!form.check.priv.attivo"
                          v-model="form.check.priv.value"
                          value="1"
                          unchecked-value="0">
                          Accetto <a target="_blank" href="./files/BINTOBIT_informativa_privacy.pdf" @click="form.check.priv.attivo = true" >Informativa sulla Privacy</a>
                        </b-form-checkbox>
                        <b-alert v-if="msg.check.priv.length > 0" show variant="danger">{{msg.check.priv}}</b-alert>

                      </b-col>

                    </b-row>

                    <b-row>
                      <b-col>
                      </b-col>
                    </b-row>

                    <b-row>
                      <b-col xl="3" offset-xl="9" md="4" offset-md="8" >
                        <b-button @click="registrazione()" block  variant="infowaste">
                          Registrati
                        </b-button>
                      </b-col>
                    </b-row>
                </b-container>
              </b-col>
            </b-row>
          </b-container>

          <Footer/>

          <b-modal id="registrazione-ok" hide-footer>
            <div class="d-block text-center">
              <h5>Richiesta di Registrazione avvenuta con successo!</h5>
              <p>Sarà inviata mail di abilitazione al servizio</p>
            </div>
            <b-button class="mt-3" variant="success" block to="./login">Ok</b-button>
          </b-modal>

          <!--
          <b-card class="mt-3" header="Form Data Result">
            <pre class="m-0">{{ form }}</pre>
          </b-card>
          -->

  </main>
</template>




<script>
  export default {
    data() {
      return {
        form: {
          nome:'',
          cognome:'',
          titolo:'',
          ragione_sociale: '',
          p_iva: '',
          telefono: '',
          email: '',
          email2: '',
          password: '',
          conferma_password:'',
          load:true,
          check:{
            serv:{
              attivo:false,
              value:0,

            },
            priv:{
              attivo:false,
              value:0
            }

          }

        },
        titoli:
        [
          {text:'Ambiente',value:'ambiente'},
          {text:'Consulente',value:'consulente'},
          {text:'Amministrazione',value:'amministrazione'},
          {text:'Logistica',value:'logistica'}

        ],
        msg: {
          nome:'',
          cognome:'',
          titolo:'',
          password: '',
          email:'',
          telefono:'',
          email2:'',
          azienda:'',

          check:{
            serv:'',
            priv:''
          }
        },
      }
    },


          methods: {

            registrazione()
            {

                var ris = 0
                ris=this.controlloNome()
                ris=this.controlloCognome()+ris
                ris=this.controlloTitolo()+ris
                ris=this.controlloEmail(this.form.email,1)+ris
                ris=this.controlloEmail(this.form.email2,2)+ris
                ris=this.controlloTelefono()+ris
                ris=this.controlloPassword()+ris
                ris=this.controlloAzienda()+ris
                ris=this.controlloFlag(this.form.check.priv.value,2)+ris
                ris=this.controlloFlag(this.form.check.serv.value,1)+ris


                if( ris == 0)
                {
                  const ris = this.$axios.post('/new_user', {
                    nome: this.form.nome,
                    cognome: this.form.cognome,
                    titolo:this.form.titolo,
                    ragione_sociale: this.form.ragione_sociale,
                    p_iva: this.form.p_iva,
                    telefono: this.form.telefono,
                    email: this.form.email,
                    email2: this.form.email2,
                    password: this.form.password

                  })
                  .then((response) => {

                      if(response.status >= 200 && response.status < 300)
                      {
                          console.log(response.data)
                          if(response.data === "Un utente con questa email è gia registrato")
                          {
                            this.msg.email = response.data

                          }else {
                            this.$bvModal.show('registrazione-ok')
                          }
                      }
                  })

                  .catch((error) => {

                        if (error.response) {
                          // The request was made and the server responded with a status code
                          // that falls out of the range of 2xx
                          console.log(error.response.data);
                          console.log(error);
                          if((error.response.data.email) && error.response.data.email == "user with this email already exists.")
                          {
                            this.msg.email="Un utente con l'email inserita è già registrato"
                          }
                          console.log(error.response.status);
                          console.log(error.response.headers);
                        } else if (error.request) {
                          // The request was made but no response was received
                          // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                          // http.ClientRequest in node.js
                          console.log(error.request);
                        } else {
                          // Something happened in setting up the request that triggered an Error
                          console.log('Error', error.message);
                        }
                        console.log(error.config);
                      });
                }

            },

            controlloNome()
            {

              var flag=0

              if(this.form.nome.length === 0)
                {
                  this.$refs.nome.$el.focus()
                  this.msg.nome="Fornire un nome"
                  flag=1

                }else
                  {
                    this.msg.nome=""
                    flag=0
                  }

                return flag

            },

            controlloCognome()
            {
              var flag=0

              if(this.form.cognome.length === 0)
                {
                  this.$refs.cognome.$el.focus()
                  this.msg.cognome="Fornire un cognome"
                  flag=1

                }else
                {
                  this.msg.cognome=""

                }
                return flag


            },

            controlloTitolo()
            {
              var flag=0

                if(this.form.titolo.length === 0)
                {
                  this.$refs.titolo.$el.focus()
                  this.msg.titolo="Selezionare un titolo"
                  flag=1

                }else {

                  this.msg.titolo=""

                }
                return flag
            },

            controlloTelefono()
            {
              var flag=0

                if(this.form.telefono.length === 0)
                {
                  this.$refs.telefono.$el.focus()
                  this.msg.telefono="Il numero di telefono è obbligatorio"
                  flag=1

                }else {

                  this.msg.telefono=""

                }
                return flag
            },
            controlloPassword()
            {
              var flag=0
              this.msg.password=""

              if(this.form.password.length === 0 || this.form.conferma_password.length === 0)
                {

                  this.msg.password="Fornire una password"
                  flag=1

                }else {


                        //controllo numeri
                        if(!(/[0-9]/.test(this.form.password)))
                        {
                          this.msg.password="Le password deve contenere almeno un numero."
                          flag=1

                        }else
                        //controllo minuscole
                        if(!(/[a-z]/.test(this.form.password)))
                        {
                          this.msg.password="Le password deve contenere almeno una minuscola."
                          flag=1

                        }
                        //controllo maiuscole
                        if(!(/[A-Z]/.test(this.form.password)))
                        {
                          this.msg.password="Le password deve contenere almeno una maiuscola."
                          flag=1

                        }

                        //controllo simboli
                        if(!(/[$-/:-?{-~!"^_`\[\]]/.test(this.form.password)))
                        {
                          this.msg.password="Le password deve contenere almeno un simbolo."
                          flag=1

                        }
                        // controllo lunghezza (minore o uguale a 8 caratteri)
                        if(this.form.password.length < 8)
                        {
                          this.msg.password="Le password deve contenere almeno 8 caratteri."
                          flag=1
                        }

                        if( !(this.form.password === this.form.conferma_password) )
                        {
                            this.msg.password="Le password non coincidono."
                            flag=1

                        }


                }
                if(flag==1)
                {
                  this.$refs.password.$el.focus()
                }
                return flag

            },

            controlloAzienda()
            {
              var flag=0

              if(this.form.ragione_sociale.length === 0 || this.form.p_iva.length === 0)
                {

                  this.msg.azienda="I dati dell'azienda sono obbligatori"
                  flag=1

                }else {
                        if (!/^[0-9]{11}$/.test(this.form.p_iva))
                        {
                          this.msg.azienda="Dati azienda non validi [Partita IVA]"
                          flag=1

                        }else {
                          this.msg.azienda=""

                        }
                }
                if(flag == 1)
                {
                  this.$refs.ragione_sociale.$el.focus()
                }
                return flag

            },

            controlloEmail(email,tipo)
            {
              var msg=""
              var flag=0

              if(email == '')
                {
                  if(tipo == 1)
                  {
                   msg="Email mancante"
                   flag=1
                  }

                  if(tipo == 2)
                  {
                    msg=""
                  }

                }else {

                            if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email))
                            {
                              msg=""
                            }else {

                              msg="Email non valida"
                              flag=1

                            }

                        }

              if(tipo == 1)
              {
                this.msg.email = msg
              }
              if(tipo == 2)
              {
                this.msg.email2 = msg
              }

              return flag

            },

            controlloFlag(state,num)
            {
                var flag=0

                  if(num == 1 && state == 0)
                  {
                    this.msg.check.serv = "Deve leggere e accettare le condizioni di servizio per potersi registrare"
                    flag=1

                  }else if(state == 1){
                    this.msg.check.serv = ""
                  }

                  if(num == 2 && state == 0)
                  {
                    this.msg.check.priv = "Deve leggere e accettare l'informativa sulla privacy per potersi registrare"
                    flag=1

                  }else if(state == 1){
                    this.msg.check.priv = ""

                  }


                return flag
            }





          }
      }
      </script>
