import { useEffect, useState } from "react";
import Header from "../components/Header";

export default function Armurerie() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/equipements", {
      method: "GET",
      credentials: "include",
    })
      .then((response) => response.json())
      .then((data) => setItems(data));
  }, []);

  function HandleEquip(id: number, isEquip: boolean) {
    if (isEquip) {
      fetch(`http://localhost:8000/api/chevalier/equipements/equiper`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({ equipement_id: id }),
      });
    } else {
      fetch(`http://localhost:8000/api/chevalier/equipements/retirer`, {
        method: "DELETE",
        credentials: "include",
        body: JSON.stringify({ equipement_id: id }),
      });
    }
  }

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
          <>
            <li key={item.id}>{item.nom}</li>
            {item.equiped ? (
              <button onClick={() => HandleEquip(item.id, false)}>
                Déséquiper
              </button>
            ) : (
              <button onClick={() => HandleEquip(item.id, true)}>
                Equiper
              </button>
            )}
          </>
        ))}
      </ul>
    </>
  );
}
