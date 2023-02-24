
import Header from '../components/Header'
import Footer from '../components/Footer'


<template>
  <main>
    <Header/>
      <b-container mt="5" >
        <b-row class="mr-1 ml-1 mt-5">
          <b-col xl="6" offset-xl="3" class="justify-content-center shadow p-3 mt-5  bg-white rounded">

            <b-form class="ml-1 mr-1" >
              <b-form-group  id="email-group" label="Email:" label-for="input-1">
                <b-form-input id="email" name="email" v-model="email" type="email"></b-form-input>
                <b-alert class="mt-2" v-if="msg.email.length > 0" show variant="danger">{{msg.email}}</b-alert>
              </b-form-group>

              <b-container>
                <b-row>
                  <b-col xl="3" offset-xl="9" md="4" offset-md="8" >
                      <b-button @click="inviaRichiesta()" block variant="infowaste">
                        Richiedi
                      </b-button>
                  </b-col>
                </b-row>
              </b-container>

            </b-form>
          </b-col>
        </b-row>
      </b-container>
      <Footer/>

      <b-modal id="invio-email-ok" hide-footer>
        <div class="d-block text-center">
          <h5>Messaggio</h5>
          <p>E' stata inviata un'email a {{email}} con le indicazioni per il ripristino della password</p>
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
   name: 'Login',
   data() {
      return {
         email: 'nbellomo506@gmail.com',
         msg:{
           email:'',
         }
      }
   },
   methods: {
      inviaRichiesta()
      {
          if(this.email != "")
          {
            this.msg.email=""

              if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.email))
              {

                this.$axios.post('/password_reset/', {

                  email:this.email

                 })
                 .then((response) => {
                   // successful response flow
                   this.$bvModal.show('invio-email-ok')
                 })
                 .catch((error) => {
                   // error response flow
                 })


             }
                else {

                  this.msg.email="Email non valida"

                }
          }
            else {
              this.msg.email="Inserire la propria email"

            }
      }
   }
};
</script>
