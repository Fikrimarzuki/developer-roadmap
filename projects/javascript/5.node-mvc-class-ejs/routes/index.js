const router = require("express").Router();
const userRoutes = require("./users");

router.get("/", (req, res) => {
  res.json("Connected");
});

router.use("/users", userRoutes);

module.exports = router;
