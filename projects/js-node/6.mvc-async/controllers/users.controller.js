const UserModel = require("../models/user.model");

class UsersController {
  static async renderUsersList(req, res) {
    const users = await UserModel.getAll();
    return res.render("users/index", { title: "Users", users });
  }

  static renderNewUserForm(req, res) {
    return res.render("users/new", { title: "Create User" });
  }

  static async renderUserDetail(req, res) {
    const user = await UserModel.getById(req.params.id);

    if (!user) {
      return res.status(404).render("users/not-found", {
        title: "User Not Found",
        id: req.params.id,
      });
    }

    return res.render("users/detail", { title: `User #${user.id}`, user });
  }

  static async createUserFromForm(req, res) {
    const { name, email } = req.body;

    if (!name || name.trim() === "") {
      return res.status(400).send("Name is required");
    }

    await UserModel.create({
      name: name.trim(),
      email: email?.trim() || null,
    });

    return res.redirect("/users");
  }

  static async deleteUserFromForm(req, res) {
    const deleted = await UserModel.remove(req.params.id);

    if (!deleted) {
      return res.status(404).render("users/not-found", {
        title: "User Not Found",
        id: req.params.id,
      });
    }

    return res.redirect("/users");
  }

  static async renderEditUserForm(req, res) {
    const user = await UserModel.getById(req.params.id);

    if (!user) {
      return res.status(404).render("users/not-found", {
        title: "User Not Found",
        id: req.params.id,
      });
    }

    return res.render("users/edit", {
      title: `Edit User #${user.id}`,
      user,
    });
  }

  static async updateUserFromForm(req, res) {
    const { name, email } = req.body;

    if (!name || name.trim() === "") {
      return res.status(400).send("Name is required");
    }

    const updated = await UserModel.update(req.params.id, {
      name: name.trim(),
      email: email?.trim() || null,
    });

    if (!updated) {
      return res.status(404).render("users/not-found", {
        title: "User Not Found",
        id: req.params.id,
      });
    }

    return res.redirect(`/users/${req.params.id}`);
  }
}

module.exports = UsersController;
