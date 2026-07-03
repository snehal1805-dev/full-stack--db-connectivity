
import { useState } from "react"
import { useNavigate } from "react-router-dom"

import API from "../api"

function Login() {

  const navigate = useNavigate()

  const [formData, setFormData] = useState({
    username: "",
    password: ""
  })

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = async (e) => {

    e.preventDefault()

    try {

      const form = new FormData()

      form.append(
        "username",
        formData.username
      )

      form.append(
        "password",
        formData.password
      )

      const response = await API.post(
        "/login",
        form
      )

      // Save token
      localStorage.setItem(
        "token",
        response.data.access_token
      )

      alert("Login Successful 😎")

      navigate("/dashboard")

    } catch (error) {

      alert(
        error.response.data.detail
      )
    }
  }

  return (

    <div>

      <h1>Login</h1>

      <form onSubmit={handleSubmit}>

        <input
          type="email"
          name="username"
          placeholder="Email"
          onChange={handleChange}
        />

        <br /><br />

        <input
          type="password"
          name="password"
          placeholder="Password"
          onChange={handleChange}
        />

        <br /><br />

        <button type="submit">
          Login
        </button>

      </form>

    </div>
  )
}

export default Login
