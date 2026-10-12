import { createHash } from "node:crypto";

export const dynamic = "force-dynamic";
export const GET = () => {
  let h = "seed";
  for (let i = 0; i < 20000; i++) h = createHash("sha256").update(h).digest("hex");
  return new Response(h.slice(0, 8));
};
