<template>
  <div>
    <nav>
      <router-link to="/info">ℹ️</router-link>
    </nav>
  </div>
  <h1>Bienvenido</h1>
  <section class="my-plan">
    <section class="exerciseContent">
      <button @click="filterByLegs">Tren inferior</button>

      <button @click="filterByAbs">Abdomen</button>

      <button @click="filterByArms">Tren superior</button>

      <button @click="filterByHit">Hit</button>

      <button @click="getAllExercises">Todos</button>
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
    async getAllExercises() {
      let user = JSON.parse(localStorage.getItem("user"));
      console.log(user, "****");
      const endpoint = `${config.API_PATH}/plan/${user.user_name}`;
      let response = await fetch(endpoint);
      this.exercises = await response.json();
      this.filteredList = this.exercises;
      // let user = localStorage.getItem("user");
      // console.log(JSON.parse(user));
    },
  },

  // async getUsers() {
  //   const endpoint = `${config.API_PATH}/users`;
  //   let response = await fetch(endpoint);
  //   this.users = await response.json();
  //   console.log(">>>>>", this.users);
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
  font-size: 40px;
}

/* .my-plan {
  margin-top: 2em;
  display: grid;
  place-content: center;
}
.excerciseSection {
  border: 1px solid black;
  padding: 1em 15em 1em 15em;
  margin-top: 1em;
  border-radius: 2%;
  background-color: rgba(170, 120, 158, 0.438);
} */
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
</style>
