// No database: the route exists so every app answers the same paths.
export const dynamic = "force-dynamic";
export const GET = () => Response.json({ n: 0 });
