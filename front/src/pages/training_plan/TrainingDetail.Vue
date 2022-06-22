<template>
  <section class="my-plans">
    <section class="exerciseSection">
      <div>
        <article>
          <h2>{{ exercise.name }}</h2>
        </article>
        <article>
          {{ exercises.img }}
          <img :key="exercise.id" :src="images[exercise.id - 1]" />
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

    this.getExercisesById()
  },

    async getExercisesById() {
      let exerciseId = this.$route.params.id;
      const settings = {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      };

      const endpoint = `${config.API_PATH}/exercises/${exercise_id}`;
      let response = await fetch(endpoint);
      this.exercises = await response.json();
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
  font-size: 50px;
}

.exerciseSection {
  width: 100%;
  overflow-y: scroll;
  max-height: 70vh;
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
