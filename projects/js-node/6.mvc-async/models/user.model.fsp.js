const fs = require("fs/promises");
const path = require("path");

const dbPath = path.join(__dirname, "..", "data", "users.json");

class UserModelFspChain {
  static ensureFile() {
    return fs.access(dbPath).catch(() =>
      fs
        .mkdir(path.dirname(dbPath), { recursive: true })
        .then(() => fs.writeFile(dbPath, "[]", "utf-8"))
    );
  }

  static readUsers() {
    return this.ensureFile()
      .then(() => fs.readFile(dbPath, "utf-8"))
      .then((raw) => JSON.parse(raw));
  }

  static writeUsers(users) {
    return fs.writeFile(dbPath, JSON.stringify(users, null, 2), "utf-8");
  }

  static getAll() {
    return this.readUsers();
  }

  static getById(id) {
    return this.readUsers().then(
      (users) => users.find((u) => String(u.id) === String(id)) || null
    );
  }

  static create(data) {
    return this.readUsers().then((users) => {
      const nextId =
        users.length === 0 ? 1 : Math.max(...users.map((u) => Number(u.id))) + 1;

      const newUser = {
        id: nextId,
        name: data.name || "No name",
        email: data.email || null,
      };

      users.push(newUser);
      return this.writeUsers(users).then(() => newUser);
    });
  }

  static remove(id) {
    return this.readUsers().then((users) => {
      const idx = users.findIndex((u) => String(u.id) === String(id));
      if (idx === -1) return null;

      const deleted = users[idx];
      users.splice(idx, 1);
      return this.writeUsers(users).then(() => deleted);
    });
  }

  static update(id, data) {
    return this.readUsers().then((users) => {
      const idx = users.findIndex((u) => String(u.id) === String(id));
      if (idx === -1) return null;

      users[idx] = {
        ...users[idx],
        name: data.name,
        email: data.email,
      };

      return this.writeUsers(users).then(() => users[idx]);
    });
  }
}

module.exports = UserModelFspChain;
