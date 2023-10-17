<template>
  <GeoJsonGlobeVue
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
  />
</template>

<script>
import GeoJsonGlobeVue from '@/components/GeoJsonGlobe.vue';
import countries from '../assets/datasets/countries.geojson';

export default {
  name: 'HomeView',
  components: {
    GeoJsonGlobeVue,
  },
  data () {
    return {
      countries: countries,
      pointsData: [
        { lat: 33.896933, lng: -5.530857 },
        { lat: 33.895212, lng: -6.123823 }
      ]
    }
  },
  mounted () {
  },
  methods: {
  }
}
</script>
