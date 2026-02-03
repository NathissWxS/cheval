import "./index.css";
import { createBrowserRouter, RouterProvider } from "react-router";
import { createRoot } from "react-dom/client";
import { StrictMode } from "react";
import Home from "./pages/home";
import Armurerie from "./pages/armurerie";
import Taverne from "./pages/taverne";
import Battle from "./pages/battle";
import Login from "./pages/login";
import Register from "./pages/register";
import RequireAuth from "./hooks/RequireAuth";

const router = createBrowserRouter([
  { path: "/", element: <Home /> },
  {
    element: <RequireAuth />,
    children: [
      { path: "/armurerie", element: <Armurerie /> },
      { path: "/champ-de-bataille", element: <Battle /> },
    ],
  },
  { path: "/taverne", element: <Taverne /> },
  { path: "/login", element: <Login /> },
  { path: "/register", element: <Register /> },
]);

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
);
