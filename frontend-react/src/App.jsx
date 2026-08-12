import { useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import NavShell from './components/NavShell'
import Home from './pages/Home'
import Analysis from './pages/Analysis'
import Plan from './pages/Plan'
import Profile from './pages/Profile'

function App() {
  const [results, setResults] = useState(null) // { analysis, plan }
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  return (
    <BrowserRouter>
      <Routes>
        <Route element={<NavShell />}>
          <Route
            path="/"
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