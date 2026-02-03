import { useNavigate } from "react-router";

export default function Header() {
  const navigate = useNavigate();

  function handleNavigate(selectedMap: string) {
    navigate("/" + selectedMap);
  }
  return (
    <div>
      <h1> cheval </h1>

      <button onClick={() => handleNavigate("armurerie")}>Go to armory</button>
      <button onClick={() => handleNavigate("champ-de-bataille")}>
        Go to battlefield
      </button>
      <button onClick={() => handleNavigate("taverne")}>Go to tavern</button>
    </div>
  );
}
