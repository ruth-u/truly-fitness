<template>
  <h1>My plan</h1>
  <section class="my-plans">
    <section class="exerciseSection">
      <div v-for="exercise in exercises" :key="exercise.id">
        <article>{{ exercise.name }}</article>
        <article>{{ exercise.description }}</article>
        <article>
          {{ exercises.img }}
          <img :key="exercise.id" :src="images2[exercise.id - 1]" />
        </article>
      </div>
    </section>
  </section>
</template>

<script>
import config from "@/config.js";

export default {
  data() {
    return {
      exercises: [],
      user: localStorage,
      images2: [
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
    this.getAllExercises();
  },

  methods: {
    async getAllExercises() {
      const endpoint = `${config.API_PATH}/exercises`;
      let response = await fetch(endpoint);
      this.exercises = await response.json();
      console.log(response.img);
    },
  },

  // computed: {
  //   exercisesImages(exercises) {
  //     exercises = this.getAllExercises();
  //     // imgList = [];
  //     for (let i of exercises) {
  //       console.log(i);
  //     }
  //   },
  // },
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
  font-size: 50px;
}
/* .my-plans {
  margin-top: 2em;
  display: grid;
  place-content: center;
}
.my-plan {
  border: 1px solid black;
  padding: 1em 15em 1em 15em;
  margin-top: 1em;
  border-radius: 2%;
  background-color: rgba(170, 120, 158, 0.438);
} */

.exerciseSection {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  grid-gap: 0.5em;
}

.exerciseSection img {
  max-width: 100%;
  max-height: 62%;
}

.exerciseSection article {
  padding: 0.5em;
  display: grid;
  grid-template-rows: auto auto auto;
}
</style>
