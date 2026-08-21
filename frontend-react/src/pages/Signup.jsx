import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../hooks/useAuth'
import { useLocation } from 'react-router-dom'

function Signup() {
  const { signUp } = useAuth()
  const navigate = useNavigate()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(false)
  const location = useLocation()
  const trialEnded = location.state?.trialEnded

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    const { error } = await signUp(email, password)
    setLoading(false)
    if (error) {
      setError(error.message)
    } else {
      navigate('/log')
    }
  }

  return (
    <div className="min-h-screen bg-bg flex items-center justify-center px-6">
      <div className="w-full max-w-sm">
        <Link to="/" className="font-display font-bold text-xl text-ink block text-center mb-8">
          📚 StudyTrack
        </Link>
        <div className="bg-card border border-card-border rounded-2xl p-7 shadow-sm">
          <h1 className="font-display font-bold text-xl text-text-dark mb-1">Create your account</h1>
          <p className="text-muted-dark text-sm mb-6">
            {trialEnded
              ? "You've used your free check-in! Create a free account to keep tracking — unlimited check-ins, saved history across devices."
              : 'Free forever — unlimited check-ins, saved history across devices.'}
          </p>

          {error && (
            <div className="bg-coral/10 border border-coral/30 text-coral rounded-xl px-4 py-2.5 mb-4 text-sm">
              {error}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-3">
            <input
              type="email"
              required
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full bg-white/5 border border-card-border rounded-xl px-4 py-3 text-text-dark placeholder:text-muted-dark outline-none focus:border-mint transition"
            />
            <input
              type="password"
              required
              minLength={6}
              placeholder="Password (min. 6 characters)"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full bg-white/5 border border-card-border rounded-xl px-4 py-3 text-text-dark placeholder:text-muted-dark outline-none focus:border-mint transition"
            />
            <button
              type="submit"
              disabled={loading}
              className="w-full bg-gradient-to-br from-mint to-mint-bright text-[#06251A] font-display font-bold rounded-full py-3 mt-2 disabled:opacity-60 transition"
            >
              {loading ? 'Creating account...' : 'Create Free Account'}
            </button>
          </form>

          <p className="text-muted-dark text-sm text-center mt-5">
            Already have an account?{' '}
            <Link to="/login" className="text-mint-bright font-semibold">Log in</Link>
          </p>
        </div>
      </div>
    </div>
  )
}

export default Signup