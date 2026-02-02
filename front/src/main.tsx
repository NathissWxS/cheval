import "./index.css";
import { createBrowserRouter, RouterProvider } from "react-router";
import { createRoot } from "react-dom/client";
import { StrictMode } from "react";
import Home from "./pages/home";

const router = createBrowserRouter([
  { path: "/", element: <Home /> },
  { path: "/armurerie", element: <Home /> },
  { path: "/champ-de-bataille", element: <Home /> },
  { path: "/taverne", element: <Home /> },
]);

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
);
