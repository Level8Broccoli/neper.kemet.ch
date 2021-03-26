import Link from "next/link";

export default function Item({ item }) {
  return (
    <main>
      <h1>{item.title}</h1>
      <Link href="/">
        <a>Zurück zur Startseite</a>
      </Link>
    </main>
  );
}

export async function getStaticPaths() {
  const res = await fetch("http://localhost:8000/items");
  const items = await res.json();

  const paths = items.map((item) => ({
    params: { id: String(item.id) },
  }));

  return { paths, fallback: false };
}

export async function getStaticProps({ params }) {
  const res = await fetch(`http://localhost:8000/items/${params.id}`);
  const item = await res.json();

  // Pass post data to the page via props
  return { props: { item } };
}
