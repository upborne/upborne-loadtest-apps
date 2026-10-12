import hashlib
import os
from contextlib import asynccontextmanager

import asyncpg
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse

pool: asyncpg.Pool


@asynccontextmanager
async def lifespan(_):
    global pool
    pool = await asyncpg.create_pool(os.environ["DATABASE_URL"], min_size=1, max_size=5)
    await pool.execute("CREATE TABLE IF NOT EXISTS visits (id serial PRIMARY KEY, at timestamptz DEFAULT now())")
    yield
    await pool.close()


app = FastAPI(lifespan=lifespan)


@app.get("/", response_class=HTMLResponse)
async def index():
    return "<h1>FastAPI</h1><p>with Postgres</p>"


@app.get("/health", response_class=PlainTextResponse)
async def health():
    return "ok"


@app.get("/db")
async def db():
    async with pool.acquire() as c:
        await c.execute("INSERT INTO visits DEFAULT VALUES")
        return {"n": await c.fetchval("SELECT count(*) FROM visits")}


@app.get("/cpu", response_class=PlainTextResponse)
def cpu():
    h = b"seed"
    for _ in range(20000):
        h = hashlib.sha256(h).digest()
    return h.hex()[:8]
