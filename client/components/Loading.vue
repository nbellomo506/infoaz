


<template>
    <main>
      <b-row>
        <b-col offset-xl="1" xl="10">
          <b-container class="mb-3 mt-5">
            <b-row>
              <b-col xl="12">
                <div class="d-flex justify-content-center mb-3">
                  <h1>Attendere...</h1>
                </div>
                <div class="d-flex justify-content-center mb-3">
                  <b-spinner label="Loading..."></b-spinner>
                </div>
              </b-col>
            </b-row>
          </b-container>
        </b-col>
      </b-row>
    </main>
</template>


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


    }

  }
</script>
