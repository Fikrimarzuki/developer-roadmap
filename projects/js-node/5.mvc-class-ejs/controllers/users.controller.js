const UserModel = require("../models/user.model");

class UsersController {
  static index(req, res) {
    const users = UserModel.findAll();
    return res.render("users/index", { users });
  }

  static newForm(req, res) {
    return res.render("users/new");
  }

  static create(req, res) {
    const { name, email } = req.body;

    if (!name || !email) {
      return res.status(400).send("Name and email are required");
    }

    const user = UserModel.create({ name, email });
    return res.redirect(`/users/${user.id}`);
  }

  static show(req, res) {
    const user = UserModel.findById(req.params.id);
    if (!user) return res.status(404).send("User not found");

    return res.render("users/show", { user });
  }

  static editForm(req, res) {
    const user = UserModel.findById(req.params.id);
    if (!user) return res.status(404).send("User not found");

    return res.render("users/edit", { user });
  }

  static update(req, res) {
    const { name, email } = req.body;

    const user = UserModel.update(req.params.id, { name, email });
    if (!user) return res.status(404).send("User not found");

    return res.redirect(`/users/${user.id}`);
  }

  static delete(req, res) {
    const ok = UserModel.delete(req.params.id);
    if (!ok) return res.status(404).send("User not found");

    return res.redirect("/users");
  }
}

module.exports = UsersController;
