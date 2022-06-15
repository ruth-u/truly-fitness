<template>
  <section class="form">
    <div class="sing_up">
      <input
        type="text"
        id="first_name"
        name="first_name"
        v-model="user.first_name"
        placeholder="introduce tu nombre"
      />
      <label for="first_name"></label>
      <input
        type="text"
        id="last_name"
        name="last_name"
        v-model="user.last_name"
        placeholder="introduce tu primer apellido"
      />
      <label for="last_name"></label>
      <input
        type="text"
        id="user_name"
        name="user_name"
        v-model="user.user_name"
        placeholder="elige nombre de usuario"
      />
      <label for="user_name"></label>
      <input
        type="password"
        id="password"
        name="password"
        v-model="user.password"
        placeholder="elige una contraseña"
      />
      <label for="password"></label>
    </div>
    <p>¿Cual es tu objetivo?</p>
    <div>
      <input
        type="radio"
        id="loose_weight"
        name="loose_weight"
        value="loose_weight"
        v-model="user.goal"
      />
      <label for="loose_weight">Perder peso</label>
    </div>
    <div>
      <input
        type="radio"
        id="gain_weight"
        name="gain_weight"
        value="gain_weight"
        v-model="user.goal"
      />
      <label for="gain_weight">Ganar peso</label>
    </div>
    <label for="weight">Peso:</label>
    <input
      type="text"
      id="weight"
      name="weight"
      v-model="user.weight"
      required
    />
    <label for="height">Altura:</label>
    <input
      type="text"
      id="height"
      name="height"
      v-model="user.height"
      required
    />
    <p>¿Tienes experiencia previa entrenando?</p>
    <div>
      <input
        type="radio"
        id="experiencie_yes"
        name="experiencie_yes"
        value="1"
        v-model="user.experiencie"
      />
      <label for="experiencie_yes">Si</label>
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

      <br />

      <label for="height">Fecha de registro:</label>
      <input
        type="date"
        id="user_register"
        name="user_register"
        v-model="user.register_date"
        required
      />
    </div>
    <div>
      <button @click.prevent="createNewUser(user)">Guardar</button>
    </div>
  </section>
  {{ user }}
</template>

<script>
import { v4 as uuidv4 } from "uuid";
import config from "@/config.js";

export default {
  name: "Home",
  data() {
    return {
      user: {
        id: "",
        user_name: "",
        password: "",
        first_name: "",
        last_name: "",
        goal: "",
        weight: "",
        height: "",
        experiencie: false,
        register_date: "",
      },
    };
  },
  methods: {
    isValidEventForm() {
      if (
        this.user.first_name === "" ||
        this.user.last_name === "" ||
        this.user.user_name === "" ||
        this.user.password === "" ||
        this.user.goal === "" ||
        this.user.weight === "" ||
        this.user.height === "" ||
        this.user.experiencie === "" ||
        this.user.register_date === ""
      ) {
        return false;
      } else {
        return true;
      }
    },

    async createNewUser(user) {
      user.id = uuidv4();
      const settings = {
        method: "POST",
        body: JSON.stringify(user),
        headers: {
          "Content-Type": "application/json",
          Authorization: user.id,
        },
      };

      console.log("*******", settings);

      let response = await fetch(`${config.API_PATH}/users`, settings);
      this.$router.push("/training_plan");

      return response;
    },
    async newUser() {
      if (!this.isValidEventForm()) {
        alert("Se deben rellaner todos los campos");
        return;
      }
      await this.createNewUser(this.user);
      alert("Usuario creado correctamente");
    },
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.goalContent {
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

.goalContent .looseWeight {
  display: grid;
  grid-row: inherit;
  cursor: pointer;
  background-color: greenyellow;
}

.goalContent .gainWeight {
  height: fit-content;
  display: grid;
  grid-row: inherit;
  cursor: pointer;
  background-color: greenyellow;
}
</style>
