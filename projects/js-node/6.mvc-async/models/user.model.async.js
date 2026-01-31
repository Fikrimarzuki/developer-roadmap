const fs = require("fs/promises");
const path = require("path");

const dbPath = path.join(__dirname, "..", "data", "users.json");

class UserModelAsync {
  static async ensureFile() {
    try {
      await fs.access(dbPath);
    } catch {
      await fs.mkdir(path.dirname(dbPath), { recursive: true });
      await fs.writeFile(dbPath, "[]", "utf-8");
    }
  }

  static async readUsers() {
    await this.ensureFile();
    const raw = await fs.readFile(dbPath, "utf-8");
    return JSON.parse(raw);
  }

  static async writeUsers(users) {
    await fs.writeFile(dbPath, JSON.stringify(users, null, 2), "utf-8");
  }

  static async getAll() {
    return await this.readUsers();
  }

  static async getById(id) {
    const users = await this.readUsers();
    return users.find((u) => String(u.id) === String(id)) || null;
  }

  static async create(data) {
    const users = await this.readUsers();
    const nextId =
      users.length === 0 ? 1 : Math.max(...users.map((u) => Number(u.id))) + 1;

    const newUser = {
      id: nextId,
      name: data.name || "No name",
      email: data.email || null,
    };

    users.push(newUser);
    await this.writeUsers(users);
    return newUser;
  }

  static async remove(id) {
    const users = await this.readUsers();
    const idx = users.findIndex((u) => String(u.id) === String(id));
    if (idx === -1) return null;

    const deleted = users[idx];
    users.splice(idx, 1);
    await this.writeUsers(users);
    return deleted;
  }

  static async update(id, data) {
    const users = await this.readUsers();
    const idx = users.findIndex((u) => String(u.id) === String(id));

    if (idx === -1) return null;

    users[idx] = {
      ...users[idx],
      name: data.name,
      email: data.email,
    };

    await this.writeUsers(users);
    return users[idx];
  }
}

module.exports = UserModelAsync;
