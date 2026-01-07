const router = require("express").Router();
const controllers = require("../controllers/users.controller");

router.get("/", controllers.getAllUser);
router.get("/:id", controllers.getUser);
router.post("/", controllers.createUser);
router.put("/:id", controllers.updateUser);
router.patch("/:id", controllers.updatePartialUser);
router.delete("/:id", controllers.deleteUser);

module.exports = router;
