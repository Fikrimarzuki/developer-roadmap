const router = require("express").Router();
const userRoutes = require("./users");

router.get("/", (req, res) => res.redirect("/users"));
router.use("/users", userRoutes);

module.exports = router;
