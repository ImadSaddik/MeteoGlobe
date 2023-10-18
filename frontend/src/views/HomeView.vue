<template>
  <GeoJsonGlobeVue
    v-if="!loading"
    :globeImageUrl="'//unpkg.com/three-globe/example/img/earth-dark.jpg'"
    :polygonsData="countries"
    :pointsData="pointsData"
    :polygonCapColor="() => '#fff'"
    :polygonSideColor="() => '#000'"
    :polygonStrokeColor="() => '#111'"
    :pointAltitude="0.01"
    :pointRadius="0.1"
    :pointColor="() => '#000'"
    :cameraZPosition="500"
    :cameraMinDistance="120"
  />
</template>

<script>
import axios from 'axios';
import GeoJsonGlobeVue from '@/components/GeoJsonGlobe.vue';
import countries from '../assets/datasets/countries.geojson';

export default {
  name: 'HomeView',
  components: {
    GeoJsonGlobeVue,
  },
  computed: {
    pointsData() {
      return this.pointsDataFull.map((point) => {
        return {
          lat: point.latitude,
          lng: point.longitude,
          name: point.name
        }
      })
    }
  },
  data () {
    return {
      countries: countries,
      pointsDataFull: [],
      loading: true,
    }
  },
  mounted () {
    this.getData()
  },
  methods: {
    async getData() {
      await axios
      .get('/api/v1/get_data/')
      .then(response => {
        console.log(response.data)
        // this.pointsDataFull = response.data
        this.loading = false
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}
</script>
