<template>
  <h1>My Plan</h1>
  <section class="my-plans">
    <section class="exerciseSection">
      <div v-for="exercise in exercises" :key="exercise.id">
        <article>
          <h2>{{ exercise.name }}</h2>
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
    };
  },

  mounted() {
    this.getAllExercises();
    // this.getUsers();
  },

  methods: {
    async getAllExercises() {
      const endpoint = `${config.API_PATH}/plan`;
      let response = await fetch(endpoint);
      this.exercises = await response.json();
      console.log("LACLSITOOO", this.user);
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
