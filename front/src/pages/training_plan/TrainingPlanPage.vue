<template>
  <h1>My plan</h1>
  <section class="my-plans">
    <div class="my-plan" v-for="exercise in exercises" :key="exercise.id">
      <p>{{ exercise.name }}</p>
      <p>{{ exercise.description }}</p>
      <p>{{ exercise.img }}</p>
    </div>
  </section>
</template>

<script>
import config from "@/config.js";
export default {
  data() {
    return {
      exercises: [],
      user: localStorage,
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

      console.log("*******", response);
    },

    exercisesImages(){
      exercises = this.getAllExercises()

      if (exercises.name === "sentadillas"){
          return
      }

    }
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
  font-size: 50px;
}
.my-plans {
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
}
</style>
