
import Header from '../components/Header'


<template>
  <main>
    <Header/>
    <b-container mt="5" >
        <b-row class="mr-1 ml-1 mt-5">
          <b-col xl="6" v-if="is_logged === false" offset-xl="3" class="justify-content-center shadow p-3 mt-5  bg-white rounded">

            <b-form class="ml-1 mr-1" >
              <b-form-group  id="email-group" label="Email:" label-for="input-1">
                <b-form-input id="email" name="email" v-model="email" type="email"></b-form-input>
                <b-alert class="mt-2" v-if="msg.email.length > 0" show variant="danger">{{msg.email}}</b-alert>
              </b-form-group>

              <b-form-group  id="password-group" label="Password:" label-for="input-2">
                <b-form-input id="password" name="password" v-model="password" type="password"></b-form-input>
                <b-alert class="mt-2" v-if="msg.password.length > 0" show variant="danger">{{msg.password}}</b-alert>
              </b-form-group>

              <b-alert class="mt-2" v-if="msg.login.length > 0" show variant="danger">{{msg.login}}</b-alert>

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

  </main>
</template>


<script>

export default {

  async asyncData({ $axios, params })
    {
      try {
        $axios.defaults.withCredentials = true;
        let is_logged = await $axios.$get(`/is_logged`);
        return { is_logged };

      } catch (e) {

          console.log(e)
          return { is_logged: false };
    }


  },



   name: 'Login',
   data() {
      return {
         is_logged:false,
         email: '',
         password: '',
         msg:
         {
           email:'',
           password:'',
           login:''
         }
      }
   },
   mounted () {

      this.$axios.defaults.withCredentials = true;

      if(this.is_logged == true)
      {
        this.goTo("./home")
      }
   },
   methods: {



     async goTo(location)
     {
        window.location.replace(location)
     },

     async login() {

       if(this.email.length == 0)
       {
         this.msg.email="Inserire la propria email"
       }

       if(this.password.length == 0)
       {
         this.msg.password="Inserire la propria password"

       }

       if(this.email.length > 0 && this.password.length > 0)
       {
         this.$axios.defaults.withCredentials = true;

             this.$axios.post('/login', {

                   email: this.email,
                   password: this.password

               })
              .then((response) => {

               if(response.status >= 200 && response.status <= 208)
               {
                  if (response.data == "SI")
                  {
                    window.location.replace("./home")
                  }
                  else if(response.data == "NO")
                  {
                    this.msg.login="Email o password errati"
                  }
                }
              })
              .catch((error) => {

               if (error.response) {
                 // The request was made and the server responded with a status code
                 // that falls out of the range of 2xx
                 if(error.response.data)
                 {
                   this.msg.login="Qualcosa è andato storto"
                 }

               } else if (error.request) {

                 if(error.response.data)
                 {
                   this.msg.login="Qualcosa è andato storto"
                 }
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

         /*const data = { 'email': this.email, 'password': this.password }
         console.log(data);
         try{
            const response = await this.$auth.loginWith('local', { data: data})
            console.log(response)
            this.$auth.$storage.setUniversal('email', response.data.email)
            await this.$auth.setUserToken(response.data.access_token, response.data.refresh_token)
         } catch(e) {
            console.log(e.message)
         }*/



      }
   }
};
</script>
