import config from "@/config.js";
// import { v4 as uuidv4 } from "uuid";

export async function loginUser(user_name, password) {
  const settings = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      user_name: user_name,
      password: password,
    }),
  };

  const response = fetch(`${config.AUTH_PATH}/login`, settings);
  return response;
}
