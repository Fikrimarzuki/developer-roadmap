const router = require("express").Router();
const UsersController = require("../controllers/users.controller");

router.get("/", UsersController.renderUsersList);
router.get("/new", UsersController.renderNewUserForm);
router.get("/:id", UsersController.renderUserDetail);
router.get("/:id/edit", UsersController.renderEditUserForm);

router.post("/", UsersController.createUserFromForm);
router.post("/:id/edit", UsersController.updateUserFromForm);
router.post("/:id/delete", UsersController.deleteUserFromForm);

module.exports = router;
