const express = require("express");

const app = express();
const port = Number(process.env.PORT) || 3000;

const notes = [];

app.use(express.json());

app.get("/health", (_req, res) => {
  res.json({ status: "ok" });
});

app.get("/api/workshop-notes", (_req, res) => {
  res.json({ notes });
});

app.post("/api/workshop-notes", (req, res) => {
  const content = typeof req.body?.content === "string" ? req.body.content.trim() : "";

  if (!content) {
    res.status(400).json({ error: "content is required" });
    return;
  }

  const note = {
    id: notes.length + 1,
    content,
    createdAt: new Date().toISOString(),
  };

  notes.push(note);
  res.status(201).json(note);
});

if (require.main === module) {
  app.listen(port, "0.0.0.0", () => {
    console.log(`iet-workshop API listening on http://0.0.0.0:${port}`);
  });
}

module.exports = app;
