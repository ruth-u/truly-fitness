<template>
  <select
    name="user"
    id="user"
    v-model="selectedUser"
    :options="options"
  ></select>
</template>

//
<script>
export default {
  data() {
    return {
      options: [],
    };
  },
  methods: {
    selectedUser(v) {
      console.table(v);
    },
  },
};
</script>

//
<style scoped></style>
