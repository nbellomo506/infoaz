
import Header from '../components/Header'
import Footer from '../components/Footer'


<template>
  <main>
    <Header/>
      <b-container mt="5" >
        <b-row class="mr-1 ml-1 mt-5">
          <b-col xl="8" offset-xl="2" class="justify-content-center shadow p-3 mt-5 bg-white rounded">
            <h2>Guida</h2>
            <hr>
            <h5>Costi Smaltimento/Trattamento</h5>
            <div class="video-container">
              <iframe
                controls
                autoplay
                loop
                muted
                class="responsive-video"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                src="https://www.youtube.com/embed/h3bZXXZqZww"
                allowfullscreen
              >

                <!-- <source src="../assets/video/" type="video/mp4" />-->
            </iframe>
            </div>
          </b-col>
        </b-row>
        <b-row class="mr-1 ml-1 mt-3 mb-5">
          <b-col xl="8" offset-xl="2" class="justify-content-center shadow p-3 mt-5 bg-white rounded">
            <h2>Assistenza</h2>     
            <hr>
            <b-modal hidden id="help-tab" cancel-variant="danger" title="Messaggio" ok-variant="infowaste" @ok="askHelp" cancel-title="Annulla" ok-title="Invia">
              Verrà inviata un'email ad assistenza@bintobit.com
              <b-form-input v-model="help_message"></b-form-input>
            </b-modal>

          </b-col>
        </b-row>
      </b-container>
    <Footer/>
  </main>
</template>
<style scoped>
.video-container {
  width: 100%;
  max-width: 800px;
  height: 450px;
  max-height: 800px;
  margin: auto;
}

.responsive-video {
  width: 100%;
  height: 100%;
  border: 2px solid #ccc;
  border-radius: 8px;
}
</style>


<script>
export default {
   name: 'Login',
   data() {
      return {
         email: '',
         msg:{
           email:'',
         }
      }
   },
   methods: {

   }
};
</script>
