import { useState } from "react";
import { Navigate, Outlet } from "react-router";

export default function RequireAuth() {
  const [isAuthenticated, setisAuthenticated] = useState(false);

  //let isAuthenticated = false;

  fetch("http://localhost:8000/api/me", {
    method: "GET",
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
    credentials: "include",
  })
    .then((response) => {
      if (response.status === 200) {
        setisAuthenticated(true);

        if (!isAuthenticated) {
          console.log("User has a problem " + isAuthenticated);
          return <Navigate to="/login" replace />;
        } else {
          console.log("User is authenticated");
        }
      } else {
        throw new Error("Failed to fetch user data");
      }
    })
    .catch((error) => {
      console.error("Error fetching user data:", error);
    });

  return <Outlet />;
}
