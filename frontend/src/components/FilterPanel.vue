<template>
  <div class="container-fluid ms-3 mt-3 position-absolute w-25">
    <div class="row">
      <div class="col bg-white p-3 rounded-3">
        <div class="row d-flex flex-row">
          <div class="col">
            <h5 class="card-title">Meteors filter panel</h5>
          </div>
          <div class="col-auto">
            <i
              v-if="expandedPanel"
              type="button"
              class="fa-solid fa-angle-up fa-xl"
              @click="expandedPanel = false"
            ></i>
            <i
              v-else
              type="button"
              class="fa-solid fa-angle-down fa-xl"
              @click="expandedPanel = true"
            ></i>
          </div>
        </div>
        <div v-show="expandedPanel" class="row mt-4 mb-3 gx-3">
          <div class="col">
            <div>
              <label for="minMassLabel" class="form-label">Mass min (Kg)</label>
              <input
                type="number"
                class="form-control"
                id="minMassLabel"
                placeholder="0.52"
                v-model="minMass"
              />
            </div>
          </div>
          <div class="col">
            <div>
              <label for="maxMassLabel" class="form-label">Mass max (Kg)</label>
              <input
                type="number"
                class="form-control"
                id="maxMassLabel"
                placeholder="120"
                v-model="maxMass"
              />
            </div>
          </div>
        </div>
        <div v-show="expandedPanel" class="row mb-3">
          <label for="countryDropDownLabel" class="form-label"
            >Select a country</label
          >
          <div class="dropdown">
            <button
              id="countryDropDownLabel"
              class="btn btn-secondary dropdown-toggle w-100"
              type="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              {{ country ? country : "Nothing selected" }}
            </button>
            <ul
              class="dropdown-menu"
              style="max-height: 200px; overflow-y: auto"
            >
              <li v-for="item in countryList" :key="item">
                <a class="dropdown-item" @click="country = item">{{ item }}</a>
              </li>
            </ul>
          </div>
        </div>
        <div v-show="expandedPanel" class="row mb-3 gx-3">
          <div class="col">
            <div>
              <label for="discoveryYearLabel" class="form-label">Year</label>
              <input
                type="number"
                class="form-control"
                id="discoveryYearLabel"
                placeholder="2023"
                v-model="discoveryYear"
              />
            </div>
          </div>
          <div class="col">
            <div>
              <label for="discoveryTypeLabel" class="form-label"
                >Discovery type</label
              >
              <div class="dropdown">
                <button
                  id="discoveryTypeLabel"
                  class="btn btn-secondary dropdown-toggle w-100"
                  type="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  {{ discoveryType ? discoveryType : "Nothing selected" }}
                </button>
                <ul class="dropdown-menu">
                  <li v-for="item in discoveryTypeList" :key="item">
                    <a class="dropdown-item" @click="discoveryType = item">{{
                      item
                    }}</a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div v-show="expandedPanel" class="row mb-4">
          <label for="chemicalCompositionDropDownLabel" class="form-label"
            >Select a chemical composition</label
          >
          <div class="dropdown">
            <button
              id="chemicalCompositionDropDownLabel"
              class="btn btn-secondary dropdown-toggle w-100"
              type="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              {{
                chemicalComposition ? chemicalComposition : "Nothing selected"
              }}
            </button>
            <ul
              class="dropdown-menu"
              style="max-height: 200px; overflow-y: auto"
            >
              <li v-for="item in chemicalCompositionList" :key="item">
                <a class="dropdown-item" @click="chemicalComposition = item">{{
                  item
                }}</a>
              </li>
            </ul>
          </div>
        </div>
        <div v-show="expandedPanel" class="row">
          <div class="col d-flex flex-row-reverse">
            <button class="btn btn-danger" @click="resetFilters">Reset</button>
            <button class="btn btn-success me-3" @click="sendFormDataToParent">Submit</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "FilterPanel",
  data() {
    return {
      expandedPanel: true,

      minMass: null,
      maxMass: null,

      country: null,
      countryList: [],

      discoveryYear: null,
      discoveryType: null,
      discoveryTypeList: [],

      chemicalComposition: null,
      chemicalCompositionList: [],
    };
  },
  mounted() {
    this.getCountryList();
    this.getDiscoveryTypeList();
    this.getChemicalCompositionList();
  },
  methods: {
    async getCountryList() {
      await axios
        .get("/api/v1/get_country_list/")
        .then((response) => {
          this.countryList = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async getDiscoveryTypeList() {
      await axios
        .get("/api/v1/get_discovery_type_list/")
        .then((response) => {
          this.discoveryTypeList = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async getChemicalCompositionList() {
      await axios
        .get("/api/v1/get_chemical_composition_list/")
        .then((response) => {
          this.chemicalCompositionList = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    sendFormDataToParent() {
      console.log("sendFormDataToParent");
      this.$emit("sendFormDataToParent", {
        minMass: this.minMass,
        maxMass: this.maxMass,
        country: this.country,
        discoveryYear: this.discoveryYear,
        discoveryType: this.discoveryType,
        chemicalComposition: this.chemicalComposition,
      });
    },
    resetFilters() {
      this.minMass = null;
      this.maxMass = null;
      this.country = null;
      this.discoveryYear = null;
      this.discoveryType = null;
      this.chemicalComposition = null;
    },
  },
};
</script>

<style scoped>
.btn.dropdown-toggle {
  text-align: left;
  padding-right: 2rem;
  position: relative;
}

.btn.dropdown-toggle::after {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  right: 10px;
}
</style>
