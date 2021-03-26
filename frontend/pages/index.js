import Link from "next/link";

export default function Home({ data }) {
  return (
    <main>
      <h1>Alle Items</h1>
      <ul>
        {data.map((item) => (
          <li key={item.id}>
            <h2>{item.title}</h2>
            <p>{item.description}</p>
            <Link href={'/' + String(item.id)}>
              <a>Zur Item-Seite</a>
            </Link>
          </li>
        ))}
      </ul>
    </main>
  );
}

export async function getStaticProps(context) {
  const res = await fetch('http://localhost:8000/items');
  const data = await res.json();

  if (!data) {
    return {
      notFound: true,
    };
  }

  return {
    props: { data },
  };
}
