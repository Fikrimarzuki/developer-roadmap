const fs = require("fs");
const path = require("path");

const dbPath = path.join(__dirname, "../data/db.json");

function readUsers() {
  const raw = fs.readFileSync(dbPath, "utf-8");
  return JSON.parse(raw);
}

function writeUsers(users) {
  fs.writeFileSync(dbPath, JSON.stringify(users, null, 2), "utf-8");
}

function getAll() {
  return readUsers();
}

function getById(id) {
  const users = readUsers();
  return users.find((u) => String(u.id) === String(id)) || null;
}

function create(data) {
  const users = readUsers();

  const nextId =
    users.length === 0 ? 1 : Math.max(...users.map((u) => Number(u.id))) + 1;

  const newUser = {
    id: nextId,
    name: data.name || "No name",
    email: data.email || null,
  };

  users.push(newUser);
  writeUsers(users);
  return newUser;
}

function update(id, data) {
  const users = readUsers();
  const index = users.findIndex((u) => String(u.id) === String(id));

  if (index === -1) return null;

  users[index] = {
    id: users[index].id,
    name: data.name,
    email: data.email,
  };

  writeUsers(users);
  return users[index];
}

function patch(id, data) {
  const users = readUsers();
  const index = users.findIndex((u) => String(u.id) === String(id));

  if (index === -1) return null;

  users[index] = {
    ...users[index],
    ...data,
  };

  writeUsers(users);
  return users[index];
}

function remove(id) {
  const users = readUsers();
  const index = users.findIndex((u) => String(u.id) === String(id));

  if (index === -1) return null;

  const deleted = users[index];
  users.splice(index, 1);
  writeUsers(users);
  return deleted;
}

module.exports = {
  getAll,
  getById,
  create,
  update,
  patch,
  remove,
};
