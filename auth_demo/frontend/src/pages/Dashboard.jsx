
import { useNavigate } from "react-router-dom"

function Dashboard() {

  const navigate = useNavigate()

  const handleLogout = () => {

    // Remove token
    localStorage.removeItem("token")

    // Redirect to login
    navigate("/")
  }

  return (
    <div>

      <h1>Dashboard</h1>

      <p>
        Welcome to protected dashboard 😎
      </p>

      <button onClick={handleLogout}>
        Logout
      </button>

    </div>
  )
}

export default Dashboard

