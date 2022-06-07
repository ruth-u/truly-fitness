<template>
  <section class="login-page">
    <h1>Truly <br />Fitness</h1>
    <div class="form">
      <form class="login-form">
        <label for="user_name"></label>
        <input
          type="text"
          id="user_name"
          name="user_name"
          placeholder="nombre de usuario"
          v-model="user.user_name"
          required
        />
        <label for="password"></label>
        <input
          type="password"
          id="password"
          name="password"
          placeholder="contraseña"
          v-model="user.password"
          required
        />

        <p class="message">
          ¿Aun no te has registrado?
          <a href="/sing-up">Registrate</a>
        </p>
        <button @click.prevent="onLoginClicked">Login</button>
      </form>
    </div>
  </section>
</template>

<script>
import { loginUser } from "@/services/auth.js";

export default {
  data() {
    return {
      user: {
        user_name: "",
        password: "",
      },
    };
  },

  methods: {
    isValidateLoginForm() {
      if (this.user_name === "" || this.password === "") {
        return false;
      } else {
        return true;
      }
    },

    async onLoginClicked() {
      if (!this.isValidateLoginForm()) {
        alert("datos incompletos");
        return;
      }
      const response = await loginUser(this.user.user_name, this.user.password);
      const loginStatus = response.status;
      console.log("response", response);

      if (loginStatus === 200) {
        this.$router.push("/training_plan");
      } else {
        alert("unauthorized");
      }
    },
  },
};
</script>

//
<style scoped>
* {
  margin: 0;
  padding: 0;
  border: 0;
}
section {
  width: 100vw;
}
h1 {
  text-align: center;
  font-family: "Roboto", sans-serif #081106;
  font-weight: bold;
  font-size: 30 px;
  color: #393942;
}

.login-page {
  border: 0;
  height: 70vh;
  padding: 8% 0 0;
}
.form {
  position: relative;
  z-index: 1;
  background: #ffffff;
  max-width: 360px;
  margin: 0 auto 100px;
  padding: 45px;
  text-align: center;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
}
.form input {
  font-family: "Roboto", sans-serif;
  outline: 0;
  background: #f2f2f2;
  width: 100%;
  border: 0;
  margin: 0 0 15px;
  padding: 15px;
  box-sizing: border-box;
  font-size: 14px;
}
.form button {
  font-family: "Roboto", sans-serif;
  text-transform: uppercase;
  outline: 0;
  background: #4caf50;
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
  background: #43a047;
}
.form .message {
  margin: 15px 0 0;
  color: #666666;
  font-size: 12px;
}
.form .message a {
  color: #4caf50;
  text-decoration: none;
}

body {
  background: linear-gradient(
    90deg,
    rgba(141, 194, 111, 1) 0%,
    rgba(118, 184, 82, 1) 50%
  );
  font-family: "Roboto", sans-serif;
}
</style>
