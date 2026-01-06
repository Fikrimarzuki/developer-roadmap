const express = require("express");
const app = express();
const PORT = 3000;

app.use(express.json());

let db = [];
let idCounter = 1;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.get("/users", (req, res) => {
  res.json(db);
});

app.post("/users", (req, res) => {
  const user = {
    id: idCounter++,
    name: req.body.name,
    email: req.body.email,
  };

  db.push(user);
  res.status(201).json(user);
});

app.patch("/users/:id", (req, res) => {
  const user = db.find(u => u.id == req.params.id);
  if (!user) return res.status(404).json({ message: "User not found" });

  if (req.body.name !== undefined) user.name = req.body.name;
  if (req.body.email !== undefined) user.email = req.body.email;

  res.json(user);
});

app.put("/users/:id", (req, res) => {
  const index = db.findIndex(u => u.id == req.params.id);
  if (index === -1) return res.status(404).json({ message: "User not found" });

  const updated = {
    id: Number(req.params.id),
    name: req.body.name,
    email: req.body.email,
  };

  db[index] = updated;
  res.json(updated);
});

app.delete("/users/:id", (req, res) => {
  const index = db.findIndex(u => u.id == req.params.id);
  if (index === -1) return res.status(404).json({ message: "User not found" });

  const removed = db.splice(index, 1);
  res.json(removed[0]);
});

app.listen(PORT, () => {
  console.log(`Listen on port: ${PORT}`);
});
