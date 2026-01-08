require("dotenv").config();

const express = require("express");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 3000;

const routers = require("./routes");

app.use(express.urlencoded({ extended: true })); // for form submit
app.use(express.json());

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

app.use(routers);

app.listen(PORT, () => {
  console.log(`Listening on port: ${PORT}`);
});
