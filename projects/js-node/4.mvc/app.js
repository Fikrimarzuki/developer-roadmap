require("dotenv").config();

const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;

const routers = require("./routes");

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use(routers);

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});


