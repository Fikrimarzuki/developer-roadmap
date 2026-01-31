const mode = process.env.ASYNC_MODE || "async";
// cb | promise | async | fsp | sync

const UserModelCallback = require("./user.model.cb");
const UserModelPromise = require("./user.model.promise");
const UserModelAsync = require("./user.model.async");
const UserModelFspChain = require("./user.model.fsp");
const UserModelSync = require("./user.model.sync");

class UserModel {
  static impl() {
    if (mode === "cb") return UserModelCallback;
    if (mode === "promise") return UserModelPromise;
    if (mode === "fsp") return UserModelFspChain;
    if (mode === "sync") return UserModelSync;
    return UserModelAsync;
  }

  static getAll() {
    const Impl = this.impl();

    if (mode === "cb") {
      return new Promise((resolve, reject) => {
        Impl.getAll((err, users) => (err ? reject(err) : resolve(users)));
      });
    }

    if (mode === "sync") return Promise.resolve(Impl.getAll());
    return Impl.getAll();
  }

  static getById(id) {
    const Impl = this.impl();

    if (mode === "cb") {
      return new Promise((resolve, reject) => {
        Impl.getById(id, (err, user) => (err ? reject(err) : resolve(user)));
      });
    }

    if (mode === "sync") return Promise.resolve(Impl.getById(id));
    return Impl.getById(id);
  }

  static create(data) {
    const Impl = this.impl();

    if (mode === "cb") {
      return new Promise((resolve, reject) => {
        Impl.create(data, (err, user) => (err ? reject(err) : resolve(user)));
      });
    }

    if (mode === "sync") return Promise.resolve(Impl.create(data));
    return Impl.create(data);
  }

  static remove(id) {
    const Impl = this.impl();

    if (mode === "cb") {
      return new Promise((resolve, reject) => {
        Impl.remove(id, (err, deleted) => (err ? reject(err) : resolve(deleted)));
      });
    }

    if (mode === "sync") return Promise.resolve(Impl.remove(id));
    return Impl.remove(id);
  }

  static update(id, data) {
    const Impl = this.impl();

    if (mode === "cb") {
      return new Promise((resolve, reject) => {
        Impl.update(id, data, (err, updated) =>
          err ? reject(err) : resolve(updated)
        );
      });
    }

    if (mode === "sync") return Promise.resolve(Impl.update(id, data));
    return Impl.update(id, data);
  }
}

module.exports = UserModel;
