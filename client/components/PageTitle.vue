

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
      <b-container class="p-0 m-0">
        <b-row>
          <b-col>
            <h2>{{name}}</h2>
            <p>{{description}}</p>
          </b-col>
        </b-row>
      </b-container>
    </div>
  </template>
