<template>
  <div>
    <nav>
      <!-- <router-link to="/info">ℹ️</router-link> -->
    </nav>
  </div>
  <div v-if="isLoading" class="loading">
    <p>Loading&#8230;</p>
  </div>
  <div v-if="isLoading == false">
    <h1>Bienvenido a tu plan semanal ! {{ this.user.user_name }}</h1>

    <button @click="filterByLegs">Tren inferior</button>

    <button @click="filterByAbs">Abdomen</button>

    <button @click="filterByArms">Tren superior</button>

    <button @click="filterByHit">Hit</button>

    <button @click="showAllExercisesAgain">Todos</button>
  </div>

  <section class="my-plan">
    <section class="exerciseContent">
      <div v-for="exercise in filteredList" :key="exercise.id">
        <article>
          <h2>{{ exercise.name }}</h2>
        </article>
        <article>
          {{ exercises.img }}
          <img :key="exercise.id" :src="images[exercise.id - 1]" />
        </article>

        <article class="detailBtn">
          <router-link :to="`/exercises/${exercise.id}`">
            ver detalle
          </router-link>
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
      isLoading: false,
      user: {},
      exercises: [],
      filteredList: null,
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
    this.getAllExercises();
  },

  methods: {
    filterByLegs() {
      this.filteredList = this.exercises.filter(
        (exercise) => exercise.category == "pierna"
      );
    },
    filterByAbs() {
      this.filteredList = this.exercises.filter(
        (exercise) => exercise.category == "abdomen"
      );
    },
    filterByArms() {
      this.filteredList = this.exercises.filter(
        (exercise) => exercise.category == "brazos"
      );
    },
    filterByHit() {
      this.filteredList = this.exercises.filter(
        (exercise) => exercise.category == "hit"
      );
    },
    async showAllExercisesAgain() {
      let user = JSON.parse(localStorage.getItem("user"));
      const endpoint = `${config.API_PATH}/plan/${user.user_name}`;
      let response = await fetch(endpoint);
      this.exercises = await response.json();
      this.filteredList = this.exercises;
    },

    async getAllExercises() {
      this.isLoading = true;
      let user = JSON.parse(localStorage.getItem("user"));
      await new Promise((resolve) => setTimeout(resolve, 2700));
      const endpoint = `${config.API_PATH}/plan/${user.user_name}`;
      let response = await fetch(endpoint);
      this.exercises = await response.json();
      this.filteredList = this.exercises;
      this.isLoading = false;
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
  font-size: 40px;
}

.my-plan {
  padding-bottom: 1em;
  background-color: rgba(143, 136, 133, 0.548);
}
.exerciseContent {
  width: 100%;
  overflow-y: scroll;
  max-height: 80vh;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
}

.exerciseContent img {
  max-width: 100%;
  max-height: 62%;
}

.exerciseContent article {
  padding: 0.5em;
  display: grid;
  grid-template-rows: 1fr auto auto;
}
nav {
  text-align: right;
}

/* Absolute Center Spinner */
.loading {
  position: fixed;
  z-index: 999;
  height: 2em;
  width: 2em;
  overflow: visible;
  margin: auto;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

/* Transparent Overlay */
.loading:before {
  content: "";
  display: block;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.521);
}

/* :not(:required) hides these rules from IE9 and below */
.loading:not(:required) {
  /* hide "loading..." text */
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}

.loading:not(:required):after {
  content: "";
  display: block;
  font-size: 10px;
  width: 1em;
  height: 1em;
  margin-top: -0.5em;
  -webkit-animation: spinner 1700ms infinite linear;
  -moz-animation: spinner 1700ms infinite linear;
  -ms-animation: spinner 1700ms infinite linear;
  -o-animation: spinner 1700ms infinite linear;
  animation: spinner 1700ms infinite linear;
  border-radius: 0.5em;
  -webkit-box-shadow: rgba(0, 0, 0, 0.75) 1.5em 0 0 0,
    rgba(0, 0, 0, 0.75) 1.1em 1.1em 0 0, rgba(0, 0, 0, 0.75) 0 1.5em 0 0,
    rgba(0, 0, 0, 0.75) -1.1em 1.1em 0 0, rgba(0, 0, 0, 0.5) -1.5em 0 0 0,
    rgba(0, 0, 0, 0.5) -1.1em -1.1em 0 0, rgba(0, 0, 0, 0.75) 0 -1.5em 0 0,
    rgba(0, 0, 0, 0.75) 1.1em -1.1em 0 0;
  box-shadow: rgba(0, 0, 0, 0.75) 1.5em 0 0 0,
    rgba(0, 0, 0, 0.75) 1.1em 1.1em 0 0, rgba(0, 0, 0, 0.75) 0 1.5em 0 0,
    rgba(0, 0, 0, 0.75) -1.1em 1.1em 0 0, rgba(0, 0, 0, 0.75) -1.5em 0 0 0,
    rgba(0, 0, 0, 0.75) -1.1em -1.1em 0 0, rgba(0, 0, 0, 0.75) 0 -1.5em 0 0,
    rgba(0, 0, 0, 0.75) 1.1em -1.1em 0 0;
}

/* Animation */

@-webkit-keyframes spinner {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@-moz-keyframes spinner {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@-o-keyframes spinner {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@keyframes spinner {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
</style>
