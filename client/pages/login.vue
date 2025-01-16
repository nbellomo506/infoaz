<template>
  <main>
    <Header/>
    <b-container mt="5" v-if="loaded === true">
        <b-row class="mr-1 ml-1 mt-5">
          <b-col xl="6" v-if="is_logged !== true" offset-xl="3" class="justify-content-center shadow p-3 mt-5  bg-white rounded">

            <b-form class="ml-1 mr-1" >
              <b-form-group  id="email-group" label="Email:" label-for="input-1">
                <b-form-input id="email" name="email" v-model="email" type="email"></b-form-input>
                <b-alert class="mt-2" v-if="msg.email" show variant="danger">{{msg.email}}</b-alert>
              </b-form-group>

              <b-form-group  id="password-group" label="Password:" label-for="input-2">
                <b-form-input id="password" name="password" v-model="password" type="password"></b-form-input>
                <b-alert class="mt-2" v-if="msg.password" show variant="danger">{{msg.password}}</b-alert>
              </b-form-group>

              <b-alert class="mt-2" v-if="msg.login" show variant="danger">{{msg.login}}</b-alert>

              <b-container>
                <b-row class="p-0">
                  <b-col xl="3" offset-xl="9" md="4" offset-md="8" >
                      <b-btn @click="login()" variant="infowaste" block>
                        Accedi
                      </b-btn>
                  </b-col>
                </b-row>
                <hr>
                <b-row>
                  <b-col xl="6" md="4">
                      <b-button to='password_reset' block variant="link">
                        Password Dimenticata?
                      </b-button>
                  </b-col>
                  <b-col xl="3" offset-xl="3" >
                      <b-button to='registrazione' block variant="infowaste-2">
                        Registrati
                      </b-button>
                  </b-col>
                </b-row>
              </b-container>

            </b-form>
          </b-col>
        </b-row>
    </b-container>
    <Footer/>

  </main>
</template>


<script>
export default {

  /*async asyncData({ $axios, params})
    {
      try {

        $axios.defaults.withCredentials = true;
        let is_logged = await $axios.$get(`/is_logged`);


        return { is_logged };

      } catch (e) {

          console.log(e)
          return { is_logged: false };
    }


  },*/



   name: 'Login',
   data() {
      return {
         is_logged:undefined,
         email: '',
         password: '',
         msg:
         {
           email:'',
           password:'',
           login:''
         },
         loaded:false,

      }
   },
   mounted () {

     this.$axios.defaults.withCredentials = true;

     this.$axios.$get(`/is_logged`)
     .then((response) => {
       this.is_logged = response
       if (this.is_logged === true)
       {
         if (typeof window !== 'undefined')
         {
           // 👉️ can use window here
           window.location.replace("./home")
         }
       }
     })
     .catch((error) => {

       this.msg.login = "Errore di rete. Riprovare più tardi"

     })
     this.loaded = true



   },
   methods: {

    async login() {
      // Reset error messages before validating new input
      this.msg = {
        email: '',
        password: '',
        login: ''
      }

      // Client-side validation
      if (!this.email) { 
        this.msg.email = "Inserire la propria email"
      }

      if (!this.password) { 
        this.msg.password = "Inserire la propria password"
      }

      // If the input is not valid, exit early
      if (!this.email || !this.password) {
        return
      }

      // Send login request to server
      try {
        const response = await this.$axios.post('/login', {
          email: this.email,
          password: this.password
        })

        // Check the response status and message from the server
        if (response.status === 200) {
          if (response.data.message === "OK") {
            // If the message is "OK", redirect the user to the home page
            window.location.replace("./home")
          } else {
            // If there's a different server message, display it
            this.msg.login = response.data.message
          }
        } else {
          // If response status is not 200, handle the error
          this.msg.login = response.data.message || "Si è verificato un errore."
        }

      } catch (error) {
        // Handle server errors
        if (error.response) {
          const status = error.response.status
          const message = error.response.data.message

          // Handle different server errors based on the status
          if (status === 400) {
            this.msg.login = message || "Email e password sono obbligatori."
          } else if (status === 401) {
            this.msg.login = message || "Email o password non validi."
          } else if (status === 403) {
            this.msg.login = message || "Il tuo account non è stato verificato."
          } else if (status === 500) {
            this.msg.login = "Si è verificato un errore imprevisto, riprova più tardi."
          } else {
            this.msg.login = "Si è verificato un errore imprevisto, riprova più tardi."
          }
        } else {
          // Network error (no server response)
          this.msg.login = "Errore di connessione, riprova più tardi."
        }
      }
    }
   }
};
</script>
