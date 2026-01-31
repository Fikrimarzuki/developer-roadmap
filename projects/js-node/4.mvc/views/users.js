const listView = (users) => {
  return {
    count: users.length,
    users,
  };
};

const detailView = (user) => {
  return {
    user,
  };
};

module.exports = {
  listView,
  detailView,
};
