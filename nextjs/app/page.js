// Rendered on each request, as a server-rendered page would be.
export const dynamic = "force-dynamic";

export default function Page() {
  const items = Array.from({ length: 50 }, (_, i) => `Item ${i}`);
  return (
    <main>
      <h1>Next.js</h1>
      <p>Rendered at {new Date().toISOString()}</p>
      <ul>{items.map((item) => <li key={item}>{item}</li>)}</ul>
    </main>
  );
}
