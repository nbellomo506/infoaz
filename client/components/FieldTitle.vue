

<script>
  export default {
  props: ['name','num','letter','description',"req"],
  data() {
    return {

    }
  }

}
</script>


  <template>
    <div>
      <div v-bind:class = "(req === 'yes')?'text-danger':'text-secondary'" class="pr-4">
        <p :name="name"> </p>
        <b>{{num}}{{letter}}  </b>{{description}}
      </div>
    </div>
  </template>
