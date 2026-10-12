import { createHash } from "node:crypto";
import express from "express";
import pg from "pg";

const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL, max: 5 });
await pool.query("CREATE TABLE IF NOT EXISTS visits (id serial PRIMARY KEY, at timestamptz DEFAULT now())");

const app = express();
app.get("/", (_, res) => res.send("<h1>Express</h1><p>with Postgres</p>"));
app.get("/health", (_, res) => res.send("ok"));
app.get("/db", async (_, res) => {
  await pool.query("INSERT INTO visits DEFAULT VALUES");
  const { rows } = await pool.query("SELECT count(*)::int AS n FROM visits");
  res.json(rows[0]);
});
app.get("/cpu", (_, res) => {
  let h = "seed";
  for (let i = 0; i < 20000; i++) h = createHash("sha256").update(h).digest("hex");
  res.send(h.slice(0, 8));
});
app.listen(3000);
