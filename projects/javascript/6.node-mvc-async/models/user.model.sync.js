const fs = require("fs");
const path = require("path");

const dbPath = path.join(__dirname, "..", "data", "users.json");

class UserModelSync {
  static ensureFile() {
    if (!fs.existsSync(dbPath)) {
      fs.mkdirSync(path.dirname(dbPath), { recursive: true });
      fs.writeFileSync(dbPath, "[]", "utf-8");
    }
  }

  static readUsers() {
    this.ensureFile();
    const raw = fs.readFileSync(dbPath, "utf-8");
    return JSON.parse(raw);
  }

  static writeUsers(users) {
    fs.writeFileSync(dbPath, JSON.stringify(users, null, 2), "utf-8");
  }

  static getAll() {
    return this.readUsers();
  }

  static getById(id) {
    const users = this.readUsers();
    return users.find((u) => String(u.id) === String(id)) || null;
  }

  static create(data) {
    const users = this.readUsers();
    const nextId =
      users.length === 0 ? 1 : Math.max(...users.map((u) => Number(u.id))) + 1;

    const newUser = {
      id: nextId,
      name: data.name || "No name",
      email: data.email || null,
    };

    users.push(newUser);
    this.writeUsers(users);
    return newUser;
  }

  static remove(id) {
    const users = this.readUsers();
    const idx = users.findIndex((u) => String(u.id) === String(id));
    if (idx === -1) return null;

    const deleted = users[idx];
    users.splice(idx, 1);
    this.writeUsers(users);
    return deleted;
  }

  static update(id, data) {
    const users = this.readUsers();
    const idx = users.findIndex((u) => String(u.id) === String(id));
    if (idx === -1) return null;

    users[idx] = {
      ...users[idx],
      name: data.name,
      email: data.email,
    };

    this.writeUsers(users);
    return users[idx];
  }

}

module.exports = UserModelSync;
