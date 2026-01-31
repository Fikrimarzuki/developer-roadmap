const express = require("express");
const app = express();
const PORT = 3000;
const routers = require("./routers");

app.use(express.json());

app.use(routers);

app.listen(PORT, () => {
  console.log(`Listen on port: ${PORT}`);
})
