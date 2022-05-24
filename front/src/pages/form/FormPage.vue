<template>
  <main class="main">
    <div class="goalsContent" v-if="showGoalsContent">
      <p class="looseWeight">
        {{ goals.looseWeigth }}
      </p>
      <p class="gainWeight">
        {{ goals.gainMuscle }}
      </p>

      <button @click="onAcceptedClicked">Aceptar</button>
    </div>
    <div class="form" v-if="showForm">
      <label for="height">Altura:</label>
      <input
        type="text"
        id="height"
        name="height"
        v-model="user.height"
        required
      />

      <label for="weight">Peso:</label>
      <input
        type="text"
        id="weight"
        name="weight"
        v-model="user.weight"
        required
      />
      <p>¿Tienes experiencia previa?</p>
      <div>
        <input
          type="radio"
          id="experiencie_yes"
          name="experiencie_yes"
          value="1"
          v-model="user.experiencie"
        />
        <label for="experiencie_yes">si</label>
      </div>
      <div>
        <input
          type="radio"
          id="experiencie_no"
          name="experiencie_no"
          value="0"
          v-model="user.experiencie"
        />
        <label for="experiencie_no">No</label>
      </div>

      <div>
        <button @click="onAcceptedClicked">Atras</button>
        <button @click.prevent="updateDataFromUser">Siguiente</button>
      </div>
    </div>
  </main>
  {{ user }}
</template>

<script>
// import { v4 as uuidv4 } from "uuid";
import config from "@/config.js";

export default {
  name: "Home",
  data() {
    return {
      goals: {
        looseWeigth: "Perder peso",
        gainMuscle: "Ganar peso",
      },

      showForm: false,
      showGoalsContent: true,
      returnToGoalsContant: false,
      user: {
        id: "",
        height: "",
        weight: "",
        experiencie: false,
      },
    };
  },
  methods: {
    onAcceptedClicked() {
      this.showForm = !this.showForm;
      this.showGoalsContent = !this.showGoalsContent;
      this.returnToGoalsContant = !this.returnToGoalsContant;
    },

    isValidEventForm() {
      if (
        this.user.weight === "" ||
        this.user.height === "" ||
        this.user.experiencie === ""
      ) {
        return false;
      } else {
        return true;
      }
    },

    async updateDataFromUser(user) {
      user.id = localStorage.userId;
      const settings = {
        method: "POST",
        body: JSON.stringify(user),
        headers: {
          Authorization: localStorage.userId,
          "Content-Type": "application/json",
        },
      };

      console.log("*******", settings);
      let response = await fetch(
        `${config.API_PATH}/users/${user.id}`,
        settings
      );
      this.$router.push("/training-plan");

      return response;
    },
    async newUserForm() {
      if (!this.isValidEventForm()) {
        alert("Se deben rellaner todos los campos");
        return;
      }
      await this.updateDataFromUser(this.user);
      alert("Evento guardado correctamente");
    },
  },
};
</script>

<style scoped>
.main {
  margin: 0;
}
.goalsContent {
  width: fit-content;
  border: 1px solid black;
  padding: 2em;
  margin-left: auto;
  margin-right: auto;
  /* margin-bottom: 5em; */
}

.form {
  width: fit-content;
  border: 1px solid black;
  padding: 2em;
  margin-left: auto;
  margin-right: auto;
}
/* label,
#experiencie {
  padding-block: 1em;
} */
/* 
.form,
#weight {
  display: grid;
  grid-row: inherit;
} */

p:hover {
  background-color: gray;
}

.goalsContent .looseWeight {
  display: grid;
  grid-row: inherit;
  cursor: pointer;
  background-color: greenyellow;
}

.goalsContent .gainWeight {
  height: fit-content;
  display: grid;
  grid-row: inherit;
  cursor: pointer;
  background-color: greenyellow;
}
</style>
