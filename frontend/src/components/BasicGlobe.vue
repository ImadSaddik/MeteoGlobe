<template>
  <div id="globeViz"></div>
</template>

<script>
import ThreeGlobe from 'three-globe';
import * as THREE from 'three';
import { TrackballControls } from 'three/examples/jsm/controls/TrackballControls.js';

export default {
  name: 'BasicGlobe',
  props: [],
  data () {
    return {
    }
  },
  mounted () {
    this.showGlobe();
  },
  methods: {
    showGlobe () {
      const N = 300;
      const gData = [...Array(N).keys()].map(() => ({
        lat: (Math.random() - 0.5) * 180,
        lng: (Math.random() - 0.5) * 360,
        size: Math.random() / 3,
        color: ['red', 'white', 'blue', 'green'][Math.round(Math.random() * 3)]
      }));

      const Globe = new ThreeGlobe()
        .globeImageUrl('//unpkg.com/three-globe/example/img/earth-dark.jpg')
        .bumpImageUrl('//unpkg.com/three-globe/example/img/earth-topology.png')
        .pointsData(gData)
        .pointAltitude('size')
        .pointColor('color');

      setTimeout(() => {
        gData.forEach(d => d.size = Math.random());
        Globe.pointsData(gData);
      }, 4000);

      // Setup renderer
      const renderer = new THREE.WebGLRenderer();
      renderer.setSize(window.innerWidth, window.innerHeight);
      document.getElementById('globeViz').appendChild(renderer.domElement);

      // Setup scene
      const scene = new THREE.Scene();
      scene.add(Globe);
      scene.add(new THREE.AmbientLight(0xcccccc, Math.PI));
      scene.add(new THREE.DirectionalLight(0xffffff, 0.6 * Math.PI));

      // Setup camera
      const camera = new THREE.PerspectiveCamera();
      camera.aspect = window.innerWidth/window.innerHeight;
      camera.updateProjectionMatrix();
      camera.position.z = 500;

      // Add camera controls
      const tbControls = new TrackballControls(camera, renderer.domElement);
      tbControls.minDistance = 101;
      tbControls.rotateSpeed = 5;
      tbControls.zoomSpeed = 0.8;

      (function animate() {
        tbControls.update();
        renderer.render(scene, camera);
        requestAnimationFrame(animate);
        })();
    }
  }
}
</script>