const router = require("express").Router();
const fs = require("fs");
const path = require("path");

const dbPath = path.join(__dirname, "..", "db.json");

router.get("/", (req, res) => {
  const data = fs.readFileSync(dbPath, "utf8");
  const parseData = JSON.parse(data);
  res.json(parseData);
});

router.post("/", (req, res) => {
  const data = fs.readFileSync(dbPath, "utf8");
  const parseData = JSON.parse(data);

  const { name, email } = req.body;
  if (!name || !email) {
    return res.status(400).json({ message: "name and email are required" });
  }
  const latestData = parseData.users.at(-1);

  const user = {
    id: latestData ? latestData.id + 1 : 1,
    name,
    email,
  };

  parseData.users.push(user);
  fs.writeFileSync(dbPath, JSON.stringify(parseData, null, 2));

  res.status(201).json(user);
});

router.put("/:id", (req, res) => {
  const data = fs.readFileSync(dbPath, "utf8");
  const parseData = JSON.parse(data);

  const { id } = req.params;
  const { name, email } = req.body;

  const index = parseData.users.findIndex((u) => u.id == id);
  if (index === -1) {
    return res.status(404).json({ message: "User not found" });
  }

  if (!name || !email) {
    return res.status(400).json({ message: "name and email required" });
  }

  const updated = {
    id: Number(id),
    name,
    email,
  };

  parseData.users[index] = updated;
  fs.writeFileSync(dbPath, JSON.stringify(parseData, null, 2));

  res.json(updated);
});

router.patch("/:id", (req, res) => {
  const data = fs.readFileSync(dbPath, "utf8");
  const parseData = JSON.parse(data);

  const { id } = req.params;
  const user = parseData.users.find((u) => u.id == id);

  if (!user) {
    return res.status(404).json({ message: "User not found" });
  }

  const { name, email } = req.body;

  if (name !== undefined) user.name = name;
  if (email !== undefined) user.email = email;

  fs.writeFileSync(dbPath, JSON.stringify(parseData, null, 2));

  res.json(user);
});

router.delete("/:id", (req, res) => {
  const data = fs.readFileSync(dbPath, "utf8");
  const parseData = JSON.parse(data);

  const { id } = req.params;
  const index = parseData.users.findIndex((u) => u.id == id);

  if (index === -1) {
    return res.status(404).json({ message: "User not found" });
  }

  const removed = parseData.users.splice(index, 1)[0];

  fs.writeFileSync(dbPath, JSON.stringify(parseData, null, 2));

  res.json(removed);
});

module.exports = router;
