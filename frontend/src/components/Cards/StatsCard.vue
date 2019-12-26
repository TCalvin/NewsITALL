<template>
  <card>
    <div>
      <div v-if="view == 'tile'">
        <div class="col-md-12" v-if="$slots.header">
          <slot name="header"></slot>
        </div>
        <div class="col-md-12" v-if="$slots.content">
          <slot name="content"></slot>
        </div>
      </div>
      <div v-if="view == 'list'" class="row">
        <div class="col-5" v-if="$slots.header">
          <slot name="header"></slot>
        </div>
        <div class="col-7" v-if="$slots.content">
          <slot name="content"></slot>
        </div>
      </div>
      <div v-if="$slots.footer">
        <hr/>
        <slot name="footer"></slot>
      </div>
    </div>

  </card>
</template>
<script>
import Card from "./Card.vue";

export default {
  name: "stats-card",
  props: ['view'],
  components: {
    Card
  }
};
</script>
<style>
</style>
