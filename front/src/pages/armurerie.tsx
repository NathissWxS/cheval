import { useEffect, useState } from "react";
import Header from "../components/Header";

export default function Armurerie() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch("/api/items")
      .then((response) => response.json())
      .then((data) => setItems(data));
  }, []);

  return (
    <>
      <Header />
      <h1>Welcome to the armory of the Castle of Valdrak</h1>
      <p>
        Everyday, knights present themselves at the armory to equip themselves
        before going to battle… <br /> or unequip themselves and relax at the
        tavern.
      </p>

      <ul>
        {items.map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </>
  );
}
