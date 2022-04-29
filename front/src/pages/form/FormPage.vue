<template>
  <main class="main">
    <div class="goalsContent" v-if="showGoalsContent">
      <checkbox class="looseWeight">
        {{ goals.looseWeigth }}
      </checkbox>
      <checkbox class="gainWeight">
        {{ goals.gainMuscle }}
      </checkbox>

      <button @click="onClickedButtom">Aceptar</button>
    </div>
    <div class="form" v-if="showForm">
      <label for="height">Altura:</label>
      <input type="text" id="height" name="user_height" />

      <label for="weight">Peso:</label>
      <input type="text" id="weight" name="user_weight" />
      <p>¿Tienes experiencia previa?</p>
      <div>
        <input
          type="radio"
          id="experiencie_yes"
          name="user_experiencie"
          value="experiencie_yes"
        />
        <label for="experiencie_yes">si</label>
      </div>
      <div>
        <input
          type="radio"
          id="experiencie_no"
          name="user_experiencie"
          value="experiencie_no"
        />
        <label for="experiencie_no">No</label>
      </div>

      <div>
        <button @click="onClickedButtom" v-if="returnToGoalsContant">
          Atras
        </button>
        <button>Siguiente</button>
      </div>
    </div>
  </main>
</template>

<script>
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
    };
  },
  methods: {
    onClickedButtom() {
      this.showForm = !this.showForm;
      this.showGoalsContent = !this.showGoalsContent;
      this.returnToGoalsContant = !this.returnToGoalsContant;
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
}

.goalsContent .gainWeight {
  height: fit-content;
  display: grid;
  grid-row: inherit;
  cursor: pointer;
}
</style>
