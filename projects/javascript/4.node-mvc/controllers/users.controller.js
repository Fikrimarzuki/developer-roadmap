const userModel = require("../models/user.model");
const userView = require("../views/users");

const getAllUser = (req, res) => {
  const users = userModel.getAll();
  res.json(userView.listView(users));
};

const getUser = (req, res) => {
  const { id } = req.params;
  const user = userModel.getById(id);

  if (!user) {
    return res.status(404).json({ message: "User not found" });
  }

  res.json(user);
};

const createUser = (req, res) => {
  const { name, email } = req.body;

  if (!name) {
    return res.status(400).json({ message: "Name is required" });
  }

  const newUser = userModel.create({ name, email });
  res.status(201).json(newUser);
};

const updateUser = (req, res) => {
  const { id } = req.params;
  const { name, email } = req.body;

  if (!name || !email) {
    return res
      .status(400)
      .json({ message: "Name and email are required for full update" });
  }

  const updated = userModel.update(id, { name, email });

  if (!updated) {
    return res.status(404).json({ message: "User not found" });
  }

  res.json(updated);
};

const updatePartialUser = (req, res) => {
  const { id } = req.params;
  const data = req.body;

  const updated = userModel.patch(id, data);

  if (!updated) {
    return res.status(404).json({ message: "User not found" });
  }

  res.json(updated);
};

const deleteUser = (req, res) => {
  const { id } = req.params;

  const deleted = userModel.remove(id);

  if (!deleted) {
    return res.status(404).json({ message: "User not found" });
  }

  res.json({ message: "User deleted", user: deleted });
};

module.exports = {
  getAllUser,
  getUser,
  createUser,
  updateUser,
  updatePartialUser,
  deleteUser,
};
