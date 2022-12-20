

<script>
  export default {
  props: ['name','description'],
  data() {
    return {

    }
  },


}
</script>


  <template>
    <div>
      <b-container>
        <b-row>
          <b-col>
            <h1>{{name}}</h1>
            <p>{{description}}</p>
          </b-col>
        </b-row>
      </b-container>
    </div>
  </template>
