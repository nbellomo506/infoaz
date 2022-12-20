
import Header from '../components/Header'


<template>
  <main>
    <Header/>
    <b-container mt="5" >
        <b-row class="mr-1 ml-1 mt-5">
          <b-col xl="6" offset-xl="3" class="justify-content-center shadow p-3 mt-5  bg-white rounded">

            <b-form class="ml-1 mr-1" >
              <b-form-group  id="password-group" label="Nuova Password" label-for="password">
                <b-form-input id="password" name="password" v-model="password" type="password"></b-form-input>
              </b-form-group>

              <b-form-group  id="password-group" label="Conferma Password" label-for="password2">
                <b-form-input id="password2" name="password2" v-model="password2" type="password"></b-form-input>
                <b-alert class="mt-2" v-if="msg.password.length > 0" show variant="danger">{{msg.password}}</b-alert>

              </b-form-group>

              <b-container>
                <b-row>
                  <b-col xl="5" offset-xl="7" md="4" offset-md="8" >
                      <b-button @click="submit()" block variant="infowaste">
                        Cambia Password
                      </b-button>
                  </b-col>
                </b-row>
              </b-container>
              {{password}}

            </b-form>
          </b-col>
        </b-row>
      </b-container>

      <b-modal id="pass-reset-ok" hide-footer>
        <div class="d-block text-center">
          <h5>Messaggio</h5>
          <p>Password modificata con successo</p>
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

   data(token) {
      return {
          msg:{
            password:'',
          },
         password: '',
         password2:'',
         token: this.$route.query.token,

      }
   },
   methods: {
      submit()
      {
        if(this.password.length === 0 || this.password2.length === 0)
          {

            this.msg.password="Fornire una password"

          }else {

                  //controllo numeri
                  if(!(/[0-9]/.test(this.password)))
                  {
                    this.msg.password="Le password deve contenere almeno un numero."

                  }else
                  //controllo minuscole
                  if(!(/[a-z]/.test(this.password)))
                  {
                    this.msg.password="Le password deve contenere almeno una minuscola."
                  }else
                  //controllo maiuscole
                  if(!(/[A-Z]/.test(this.password)))
                  {
                    this.msg.password="Le password deve contenere almeno una maiuscola."
                  }else

                  //controllo simboli
                  if(!(/[$-/:-?{-~!"^_`\[\]]/.test(this.password)))
                  {
                    this.msg.password="Le password deve contenere almeno un simbolo."
                  }else
                  // controllo lunghezza (minore o uguale a 8 caratteri)
                  if(this.password.length < 8)
                  {
                    this.msg.password="Le password deve contenere almeno 8 caratteri."
                  }else

                  if( !(this.password === this.password2) )
                  {
                      this.msg.password="Le password non coincidono."

                  }else {

                    this.msg.password=""
                    this.$axios.post('/password_reset/confirm/', {

                      token:this.token,
                      password:this.password
                    })
                      .then((response) => {
                      this.$bvModal.show('password-reset-ok')
                       alert("Password modificata con successo")
                       window.location.replace("../login")

                     })
                     .catch((error) => {
                       console.log(error)

                     })
                  }

          }



      }


   }
};
</script>
