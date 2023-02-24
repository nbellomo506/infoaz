
  <template>
    <main>
      <b-container fluid class="bg-light pt-4 pb-4 b-0 mb-0 mt-max">
        <b-row class="ml-5">
          <b-col class="text-center" offset-xl="5" cols="1">
            <a href="#" @click="gotoCredits()">Credits</a>
          </b-col>
        </b-row>
      </b-container>
    </main>
  </template>

<style scoped>
  .mt-max{
    margin-top:150px;
}
</style>

  <script>
  import axios from '@nuxtjs/axios'

  export default {
    mounted () {


    },


    data() {
      return {

      }
    },

    methods:
    {

      gotoCredits()
      {
        if(this.$route.name === 'compila_dati_comune-id')
        {
          window.location.replace("../../credits")
        }else {
            window.location.replace("./credits")

        }
      }

    }

  }
</script>
