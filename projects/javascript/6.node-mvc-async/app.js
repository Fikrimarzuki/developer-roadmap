require("dotenv").config();

const path = require("path");
const express = require("express");
const app = express();

const routes = require("./routes");

const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

app.use(routes);

app.listen(PORT, () => console.log(`Listening on port ${PORT}`));
