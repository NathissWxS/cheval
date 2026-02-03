import { Navigate, Outlet } from "react-router";

export default function RequireAuth() {
  let isAuthenticated = false;

  fetch("http://localhost:8000/api/me", {
    method: "GET",
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
    credentials: "include",
  })
    .then((response) => {
      if (response.status === 200) {
        isAuthenticated = true;
      } else {
        throw new Error("Failed to fetch user data");
      }
    })
    .catch((error) => {
      console.error("Error fetching user data:", error);
    });

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return <Outlet />;
}
