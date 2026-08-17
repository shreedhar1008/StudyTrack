import { useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import NavShell from './components/NavShell'
import Landing from './pages/Landing'
import Home from './pages/Home'
import Analysis from './pages/Analysis'
import Plan from './pages/Plan'
import Profile from './pages/Profile'
import About from './pages/About'
import Contact from './pages/Contact'
import Privacy from './pages/Privacy'
import Terms from './pages/Terms'

function App() {
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/privacy" element={<Privacy />} />
        <Route path="/terms" element={<Terms />} />
        <Route element={<NavShell />}>
          <Route
            path="/log"
            element={
              <Home
                setResults={setResults}
                loading={loading}
                setLoading={setLoading}
                error={error}
                setError={setError}
              />
            }
          />
          <Route path="/analysis" element={<Analysis results={results} />} />
          <Route path="/plan" element={<Plan results={results} />} />
          <Route path="/profile" element={<Profile />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App