<template>
      <div class="row">
      <div class="col-12">
        <chart-card title="Topic Progression"
                    sub-title="Weekly Trend"
                    :chart-data="data"
                    :chart-options="options">
          <span slot="footer">
            <i class="ti-reload"></i> Updated just now
          </span>
          <div slot="legend">
            <i class="fa fa-circle text-info"></i> {{term}}

          </div>
        </chart-card>
      </div>
  </div>
</template>

<script>
import { stringify } from 'querystring'

export default {
  name: 'Sentiment',
  props: ['articles', 'term'],
  data (){
    return{
      data:{
        labels: [],
        series: []
      },
      options: {
          low: 0,
          high: 1000,
          showArea: true,
          height: "245px",
          axisX: {
            showGrid: false
          },
          lineSmooth: Chartist.Interpolation.simple({
            divisor: 3
          }),
          showLine: true,
          showPoint: false
        }
    }
  },
  mounted(){
      this.setLabels()
      this.setSeries()
  },
  methods: {
      setLabels(){
          var date = new Date()
          date.setDate(date.getDate() - 7)
          
          for(i = 0; i < 7; i++){
              this.labels.append(String(date.getMonth) + "/" + String(date.getDate))
              date.setDate(date.getDate()+1)
          }
      },
      setSeries(){
          var start = new Date()
          var end = new Date()
          start.setDate(start.getDate() - 7)
        
          this.series.append([])
          for (article in this.articles){
              var artDate = new Date(article.published)
              if(artDate.getDate() > start && artDate.getDate() < end){
                  series[0].append(article.sentiment)
              }
          }
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #e0fff1;
}
div{
  margin-top: 20px;
}
</style>
