<template>
  <section class="register-page">
    <div class="form">
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
      <p>¿Cual es tu objetivo?</p>
      <label for="loose_weight">Perder peso</label>
      <input
        type="radio"
        id="loose_weight"
        name="loose_weight"
        value="loose_weight"
        v-model="user.goal"
      />

      <label for="gain_weight">Ganar peso</label>
      <input
        type="radio"
        id="gain_weight"
        name="gain_weight"
        value="gain_weight"
        v-model="user.goal"
      />

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
      <div><p>¿Tienes experiencia previa entrenando?</p></div>
      <label class="labelForYes" for="experiencie_yes">Si</label>
      <input
        type="radio"
        id="experiencie_yes"
        name="experiencie_yes"
        value="1"
        v-model="user.experiencie"
      />
      <label class="labelForNo" for="experiencie_no">No</label>

      <input
        type="radio"
        id="experiencie_no"
        name="experiencie_no"
        value="0"
        v-model="user.experiencie"
      />

      <div>
        <button @click.prevent="createNewUser(user)">Guardar</button>
      </div>
    </div>
  </section>
</template>

<script>
import { v4 as uuidv4 } from "uuid";
import config from "@/config.js";

export default {
  name: "Form",
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
      localStorage.setItem("user", JSON.stringify(user));
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

.register-page {
  border: 0;
  height: 50vh;
  padding-bottom: 1%;
}
.form {
  position: relative;
  z-index: 1;
  background: #ffffff;
  max-width: 380px;
  margin: 0 auto 100px;
  padding: 45px;
  text-align: center;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
}
.form input {
  outline: 0;
  background: #ffffff;
  width: 100%;
  border: 0;
  margin: 0 0 15px;
  padding: 15px;
  box-sizing: border-box;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);

  font-size: 14px;
}

.form button {
  /* font-family: "Roboto", sans-serif; */
  text-transform: uppercase;
  outline: 0;
  background: rgba(57, 116, 226, 0.438);
  width: 100%;
  border: 0;
  padding: 15px;
  color: #ffffff;
  font: bold;
  font-size: 14px;
  -webkit-transition: all 0.3 ease;
  transition: all 0.3 ease;
  cursor: pointer;
}
.form button:hover,
.form button:active,
.form button:focus {
  background: rgba(8, 86, 122, 0.767);
}
</style>
