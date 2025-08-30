import Link from 'next/link';

export default function Home() {
  return (
    <main className="p-6 space-y-4">
      <h1 className="text-2xl font-semibold">Binaai MVP v0</h1>
      <p>Login, open a sample pipeline, and run browser preview.</p>
      <Link className="underline text-blue-600" href="/canvas">
        Open Canvas
      </Link>
    </main>
  );
}
