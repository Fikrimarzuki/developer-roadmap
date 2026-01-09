const fs = require("fs");
const path = require("path");

const dbPath = path.join(__dirname, "../data/users.json");

class UserModelCallback {
  static ensureFile(cb) {
    fs.access(dbPath, (err) => {
      if (!err) return cb(null);

      fs.mkdir(path.dirname(dbPath), { recursive: true }, (mkErr) => {
        if (mkErr) return cb(mkErr);
        fs.writeFile(dbPath, "[]", "utf-8", cb);
      });
    });
  }

  static readUsers(cb) {
    this.ensureFile((err) => {
      if (err) return cb(err);

      fs.readFile(dbPath, "utf-8", (readErr, raw) => {
        if (readErr) return cb(readErr);
        try {
          cb(null, JSON.parse(raw));
        } catch (e) {
          cb(e);
        }
      });
    });
  }

  static writeUsers(users, cb) {
    fs.writeFile(dbPath, JSON.stringify(users, null, 2), "utf-8", cb);
  }

  static getAll(cb) {
    this.readUsers(cb);
  }

  static getById(id, cb) {
    this.readUsers((err, users) => {
      if (err) return cb(err);
      const user = users.find((u) => String(u.id) === String(id)) || null;
      cb(null, user);
    });
  }

  static create(data, cb) {
    this.readUsers((err, users) => {
      if (err) return cb(err);

      const nextId =
        users.length === 0 ? 1 : Math.max(...users.map((u) => Number(u.id))) + 1;

      const newUser = {
        id: nextId,
        name: data.name || "No name",
        email: data.email || null,
      };

      users.push(newUser);
      this.writeUsers(users, (wErr) => {
        if (wErr) return cb(wErr);
        cb(null, newUser);
      });
    });
  }

  static remove(id, cb) {
    this.readUsers((err, users) => {
      if (err) return cb(err);

      const idx = users.findIndex((u) => String(u.id) === String(id));
      if (idx === -1) return cb(null, null);

      const deleted = users[idx];
      users.splice(idx, 1);

      this.writeUsers(users, (wErr) => {
        if (wErr) return cb(wErr);
        cb(null, deleted);
      });
    });
  }

  static update(id, data, cb) {
    this.readUsers((err, users) => {
      if (err) return cb(err);

      const idx = users.findIndex((u) => String(u.id) === String(id));
      if (idx === -1) return cb(null, null);

      users[idx] = {
        ...users[idx],
        name: data.name,
        email: data.email,
      };

      this.writeUsers(users, (wErr) => {
        if (wErr) return cb(wErr);
        cb(null, users[idx]);
      });
    });
  }
}

module.exports = UserModelCallback;
