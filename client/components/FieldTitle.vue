

<script>
  export default {
  props: ['name','letter','description',"req"],
  data() {
    return {

    }
  }

}
</script>


  <template>
    <div>
      <div v-bind:class = "(req === 'yes')?'text-danger':'text-secondary'" class="pr-4">

        <div v-if="letter === undefined">
          <li class="field_index" >
            <p :name="name"> </p>
            <b>{{letter}}  </b>{{description}}
          </li>
        </div>

        <div v-if="letter !== undefined">
          <p :name="name"> </p>
          <b>{{letter}}.  </b>{{description}}
        </div>

      </div>
    </div>
  </template>
