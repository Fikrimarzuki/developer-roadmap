const router = require("express").Router();
const UsersController = require("../controllers/users.controller");

router.get("/", UsersController.index);
router.get("/new", UsersController.newForm);
router.post("/", UsersController.create);
router.get("/:id", UsersController.show);
router.get("/:id/edit", UsersController.editForm);
router.post("/:id", UsersController.update);
router.post("/:id/delete", UsersController.delete);

module.exports = router;
