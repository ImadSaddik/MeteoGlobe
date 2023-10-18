<template>
  <div id="globeContainer"></div>
</template>

<script>
import ThreeGlobe from 'three-globe';
import * as THREE from 'three';
import { TrackballControls } from 'three/examples/jsm/controls/TrackballControls.js';

export default {
  name: 'GeoJsonGlobe',
  props: [
    'polygonsData', 'pointsData', 'polygonCapColor', 'polygonSideColor', 'polygonStrokeColor',
    'pointAltitude', 'pointRadius', 'pointColor', 'globeImageUrl', 'cameraZPosition', 'cameraMinDistance'
  ],
  data () {
    return {
    }
  },
  mounted () {
    this.showGlobe();
  },
  methods: {
    showGlobe () {
      const Globe = new ThreeGlobe()
        .globeImageUrl(this.globeImageUrl)
        .polygonsData(this.polygonsData.features.filter(d => d.properties.ISO_A2 !== 'AQ'))
        .polygonCapColor(this.polygonCapColor)
        .polygonSideColor(this.polygonSideColor)
        .polygonStrokeColor(this.polygonStrokeColor)
        .pointsData(this.pointsData)
        .pointAltitude(this.pointAltitude)
        .pointRadius(this.pointRadius)
        .pointColor(this.pointColor);

      const renderer = new THREE.WebGLRenderer();
      renderer.setSize(window.innerWidth, window.innerHeight);
      document.getElementById('globeContainer').appendChild(renderer.domElement);

      const scene = new THREE.Scene();
      scene.add(Globe);
      scene.add(new THREE.AmbientLight(0xcccccc, Math.PI));
      scene.add(new THREE.DirectionalLight(0xffffff, 0.6 * Math.PI));

      const camera = new THREE.PerspectiveCamera();
      camera.aspect = window.innerWidth/ window.innerHeight;
      camera.updateProjectionMatrix();
      camera.position.z = this.cameraZPosition;

      const tbControls = new TrackballControls(camera, renderer.domElement);
      tbControls.minDistance = this.cameraMinDistance;
      tbControls.rotateSpeed = 1;
      tbControls.zoomSpeed = 0.5;

      (function animate() {
        tbControls.update();
        renderer.render(scene, camera);
        requestAnimationFrame(animate);
      })();
    }
  }
}
</script>