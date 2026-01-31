const UserModelCallback = require("./user.model.cb");

class UserModelPromise {
  static getAll() {
    return new Promise((resolve, reject) => {
      UserModelCallback.getAll((err, users) => (err ? reject(err) : resolve(users)));
    });
  }

  static getById(id) {
    return new Promise((resolve, reject) => {
      UserModelCallback.getById(id, (err, user) => (err ? reject(err) : resolve(user)));
    });
  }

  static create(data) {
    return new Promise((resolve, reject) => {
      UserModelCallback.create(data, (err, user) => (err ? reject(err) : resolve(user)));
    });
  }

  static remove(id) {
    return new Promise((resolve, reject) => {
      UserModelCallback.remove(id, (err, deleted) => (err ? reject(err) : resolve(deleted)));
    });
  }

  static update(id, data) {
    return new Promise((resolve, reject) => {
      UserModelCallback.update(id, data, (err, updated) =>
        err ? reject(err) : resolve(updated)
      );
    });
  }
}

module.exports = UserModelPromise;
