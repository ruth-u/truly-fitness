<template>
  <nav><router-link to="/training_plan">MI PLAN</router-link></nav>
  <h1>Detalle del ejercicio</h1>
  <section class="exerciseContainer">
    <div class="exerciseSection">
      <article>
        <h2>{{ exercise.name }}</h2>
      </article>
      <article>
        {{ exercise.description }}
      </article>
      <article>
        {{ exercise.img }}
        <img :key="exercise.id" :src="images[exercise.id - 1]" />
      </article>
    </div>
  </section>
</template>

<script>
import config from "@/config.js";

export default {
  name: "Detail",
  data() {
    return {
      exercise: {},
      images: [
        require("@/images/legs/sentadillas.jpg"),
        require("@/images/legs/hip-thrust.jpeg"),
        require("@/images/legs/patadas_de_burro.jpg"),
        require("@/images/legs/peso-muerto.jpg"),
        require("@/images/legs/hip-thrust.jpeg"),
        require("@/images/abs/plancha.jpg"),
        require("@/images/abs/abdominales.jpg"),
        require("@/images/abs/dead-bug.jpg"),
        require("@/images/abs/Bicycle-crunches.jpg"),
        require("@/images/abs/russian-twist.jpg"),
        require("@/images/arms/curl-biceps.jpg"),
        require("@/images/arms/flexiones.jpg"),
        require("@/images/arms/levantamiento-lateral-hombros.jpg"),
        require("@/images/arms/rotacion-ext.jpg"),
        require("@/images/arms/remo-con-mancuernas.jpg"),
        require("@/images/hit/correr.jpg"),
        require("@/images/hit/zancadas.jpg"),
        require("@/images/hit/jumping-jacks.jpg"),
        require("@/images/hit/burpees.jpg"),
        require("@/images/hit/mountain-climbers.jpg"),
        require("@/images/legs/sentadillas.jpg"),
        require("@/images/legs/hip-thrust.jpeg"),
        require("@/images/legs/patadas_de_burro.jpg"),
        require("@/images/legs/peso-muerto.jpg"),
        require("@/images/legs/hip-thrust.jpeg"),
        require("@/images/abs/plancha.jpg"),
        require("@/images/abs/abdominales.jpg"),
        require("@/images/abs/dead-bug.jpg"),
        require("@/images/abs/Bicycle-crunches.jpg"),
        require("@/images/abs/russian-twist.jpg"),
        require("@/images/arms/curl-biceps.jpg"),
        require("@/images/arms/flexiones.jpg"),
        require("@/images/arms/levantamiento-lateral-hombros.jpg"),
        require("@/images/arms/rotacion-ext.jpg"),
        require("@/images/arms/remo-con-mancuernas.jpg"),
        require("@/images/hit/correr.jpg"),
        require("@/images/hit/zancadas.jpg"),
        require("@/images/hit/jumping-jacks.jpg"),
        require("@/images/hit/burpees.jpg"),
        require("@/images/hit/mountain-climbers.jpg"),
      ],
    };
  },

  mounted() {
    this.getExercisesById();
  },

  methods: {
    async getExercisesById() {
      let exerciseId = this.$route.params.id;
      let endpoint = `${config.API_PATH}/exercises/${exerciseId}`;
      let response = await fetch(endpoint);
      this.exercise = await response.json();
    },
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-size: 20px;
}
h1 {
  text-align: center;
  margin-top: 1em;
  font-size: 30px;
}

nav {
  text-align: center;
}

.exerciseContainer {
  /* margin-top: 2em; */
  display: grid;
  place-content: center;
  text-align: center;
}

.exerciseSection {
  width: 100%;
  max-height: 70vh;
  display: grid;
  grid-template-rows: 1fr 1fr 1fr;
  grid-gap: 0.5em;
}

.exerciseSection img {
  max-width: 100%;
  max-height: 85%;
}
</style>
