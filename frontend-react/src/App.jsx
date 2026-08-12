import { BrowserRouter, Routes, Route } from 'react-router-dom'
import NavShell from './components/NavShell'
import Home from './pages/Home'
import Analysis from './pages/Analysis'
import Plan from './pages/Plan'
import Profile from './pages/Profile'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<NavShell />}>
          <Route path="/" element={<Home />} />
          <Route path="/analysis" element={<Analysis />} />
          <Route path="/plan" element={<Plan />} />
          <Route path="/profile" element={<Profile />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App