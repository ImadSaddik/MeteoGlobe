<template>
  <div id="globeContainer"></div>
</template>

<script>
import ThreeGlobe from "three-globe";
import * as THREE from "three";
import { TrackballControls } from "three/examples/jsm/controls/TrackballControls.js";

export default {
  name: "GeoJsonGlobe",
  props: [
    "polygonsData",
    "pointsData",
    "polygonCapColor",
    "polygonSideColor",
    "polygonStrokeColor",
    "pointAltitude",
    "pointRadius",
    "pointColor",
    "globeImageUrl",
    "cameraZPosition",
    "cameraMinDistance",
    "cameraMaxDistance",
  ],
  data() {
    return {
    };
  },
  mounted() {
    this.showGlobe();
  },
  methods: {
    showGlobe() {
      const globe = new ThreeGlobe()
        .globeImageUrl(this.globeImageUrl)
        .polygonsData(
          this.polygonsData.features.filter((d) => d.properties.ISO_A2 !== "AQ")
        )
        .polygonAltitude(0.01)
        .polygonCapColor(this.polygonCapColor)
        .polygonSideColor(this.polygonSideColor)
        .polygonStrokeColor(this.polygonStrokeColor)
        .pointsData(this.pointsData)
        .pointAltitude(this.pointAltitude)
        .pointRadius(this.pointRadius)
        .pointColor(this.pointColor)

      const renderer = new THREE.WebGLRenderer();
      renderer.setSize(window.innerWidth, window.innerHeight);
      document
        .getElementById("globeContainer")
        .appendChild(renderer.domElement);

      const scene = new THREE.Scene();
      scene.add(globe);
      scene.add(new THREE.AmbientLight(0xcccccc, Math.PI));
      scene.add(new THREE.DirectionalLight(0xffffff, 0.6 * Math.PI));

      const camera = new THREE.PerspectiveCamera();
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      camera.position.z = this.cameraZPosition;

      const tbControls = new TrackballControls(camera, renderer.domElement);
      tbControls.minDistance = this.cameraMinDistance;
      tbControls.maxDistance = this.cameraMaxDistance;
      tbControls.zoomSpeed = 0.5;

      const this_ = this;

      (function animate() {
        tbControls.rotateSpeed = this_.calculateRotateSpeed(camera.position);
        tbControls.update();
        renderer.render(scene, camera);
        requestAnimationFrame(animate);
      })();
    },
    calculateRotateSpeed(position) {
      const maxRotateSpeed = 3;
      const minRotateSpeed = 0.2;

      const magnitude = Math.sqrt(
        position.x * position.x +
          position.y * position.y +
          position.z * position.z
      );

      const normalizedValue =
        (magnitude - this.cameraMinDistance) /
        (this.cameraMaxDistance - this.cameraMinDistance);

      return (
        minRotateSpeed + normalizedValue * (maxRotateSpeed - minRotateSpeed)
      );
    },
  },
};
</script>
