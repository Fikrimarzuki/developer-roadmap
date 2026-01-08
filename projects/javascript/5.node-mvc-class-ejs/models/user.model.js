const fs = require("fs");
const path = require("path");

class UserModel {
  static dbPath() {
    return path.join(__dirname, "../data/users.json");
  }

  static _read() {
    const raw = fs.readFileSync(this.dbPath(), "utf-8");
    return JSON.parse(raw || "[]");
  }

  static _write(data) {
    fs.writeFileSync(this.dbPath(), JSON.stringify(data, null, 2), "utf-8");
  }

  static findAll() {
    return this._read();
  }

  static findById(id) {
    const users = this._read();
    return users.find((u) => u.id === Number(id)) || null;
  }

  static create(payload) {
    const users = this._read();
    const nextId = users.length ? Math.max(...users.map((u) => u.id)) + 1 : 1;

    const newUser = {
      id: nextId,
      name: payload.name?.trim() || "",
      email: payload.email?.trim() || ""
    };

    users.push(newUser);
    this._write(users);
    return newUser;
  }

  static update(id, payload) {
    const users = this._read();
    const idx = users.findIndex((u) => u.id === Number(id));
    if (idx === -1) return null;

    const updated = {
      ...users[idx],
      name: payload.name?.trim() ?? users[idx].name,
      email: payload.email?.trim() ?? users[idx].email
    };

    users[idx] = updated;
    this._write(users);
    return updated;
  }

  static delete(id) {
    const users = this._read();
    const before = users.length;
    const filtered = users.filter((u) => u.id !== Number(id));
    if (filtered.length === before) return false;

    this._write(filtered);
    return true;
  }
}

module.exports = UserModel;
