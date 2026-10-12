// A background worker: queues a job every 200 ms and works through the queue.
// The HTTP side only reports; the load is the loop.
import { createHash } from "node:crypto";
import { createServer } from "node:http";
import { createClient } from "redis";

const producer = await createClient({ url: process.env.REDIS_URL }).connect();
const consumer = producer.duplicate();
await consumer.connect();
let done = 0;

setInterval(() => producer.lPush("jobs", String(Date.now())), 200);
(async () => {
  for (;;) {
    const job = await consumer.brPop("jobs", 0);
    let h = job.element;
    for (let i = 0; i < 20000; i++) h = createHash("sha256").update(h).digest("hex");
    done++;
  }
})();

createServer(async (req, res) => {
  if (req.url === "/health") return res.end("ok");
  if (req.url === "/db") return res.end(JSON.stringify({ queued: await producer.lLen("jobs"), done }));
  res.end(`<h1>Worker</h1><p>${done} jobs done</p>`);
}).listen(3000);
