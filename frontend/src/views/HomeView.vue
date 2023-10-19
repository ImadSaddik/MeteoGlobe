<template>
  <FilterPanelVue @send-form-data-to-parent="(data) => getData(data)" />
  <GeoJsonGlobeVue
    v-if="!loading"
    :globeImageUrl="'//unpkg.com/three-globe/example/img/earth-dark.jpg'"
    :polygonsData="countries"
    :pointsData="pointsData"
    :polygonCapColor="() => '#424242'"
    :polygonSideColor="() => '#000'"
    :polygonStrokeColor="() => '#111'"
    :pointAltitude="0.01"
    :pointRadius="0.05"
    :pointColor="() => '#EBB800'"
    :cameraZPosition="500"
    :cameraMinDistance="120"
  />
</template>

<script>
import axios from "axios";
import countries from "../assets/datasets/countries.geojson";

import GeoJsonGlobeVue from "@/components/GeoJsonGlobe.vue";
import FilterPanelVue from "@/components/FilterPanel.vue";

export default {
  name: "HomeView",
  components: {
    GeoJsonGlobeVue,
    FilterPanelVue,
  },
  computed: {
    pointsData() {
      return this.pointsDataFull.map((point) => {
        return {
          lat: point.latitude,
          lng: point.longitude,
          name: point.name,
        };
      });
    },
  },
  data() {
    return {
      countries: countries,
      pointsDataFull: [],
      loading: false,
    };
  },
  methods: {
    async getData(panelData) {
      this.loading = true;
      await axios
        .get("/api/v1/get_points_data/", {
          params: {
            min_mass: panelData.minMass,
            max_mass: panelData.maxMass,
            country: panelData.country,
            discovery_year: panelData.discoveryYear,
            discovery_type: panelData.discoveryType,
            chemical_composition: panelData.chemicalComposition,
          },
        })
        .then((response) => {
          console.log(response.data);
          this.pointsDataFull = response.data;
          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
