import { useEffect, useState } from 'react'
import { getAnonId } from '../hooks/useAnonId'
import { useAuth } from '../hooks/useAuth'
import { getHistory, getUserHistory } from '../api/studytrack'

function formatDate(isoString) {
  const d = new Date(isoString)
  return d.toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' })
}

function Profile() {
  const [submissions, setSubmissions] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const { user } = useAuth()

  useEffect(() => {
  const fetchHistory = user
    ? getUserHistory(user.id)
    : getHistory(getAnonId())

  fetchHistory
    .then((data) => setSubmissions(data.submissions))
    .catch((err) => {
      console.error(err)
      setError('Could not load your history.')
    })
    .finally(() => setLoading(false))
}, [user])

  return (
    <div className="p-6 md:p-10 max-w-2xl mx-auto pb-24 md:pb-10">
      <span className="inline-block font-mono text-[0.7rem] tracking-wider text-mint bg-mint/10 border border-mint/30 rounded-full px-3.5 py-1.5 mb-3">
        YOUR HISTORY
      </span>
      <h1 className="font-display text-2xl font-bold text-ink mb-2">Profile</h1>
      <p className="text-muted-light mb-6">
        Every check-in you've submitted from this device.
      </p>

      {loading && <p className="text-muted-light">Loading your history...</p>}
      {error && (
        <div className="bg-coral/10 border border-coral/30 text-coral rounded-xl px-4 py-3 mb-4 text-sm">
          {error}
        </div>
      )}

      {!loading && !error && submissions.length === 0 && (
        <div className="bg-card border border-card-border rounded-2xl px-6 py-8 text-center">
          <p className="text-muted-dark text-sm">
            No check-ins yet — submit the form on Home to start building your history.
          </p>
        </div>
      )}

      <div className="space-y-3">
        {submissions.map((sub) => (
          <div
            key={sub.id}
            className="bg-card border border-card-border rounded-2xl px-5 py-4 shadow-sm"
          >
            <div className="flex items-center justify-between">
              <span className="font-mono text-[0.68rem] tracking-widest uppercase text-muted-dark">
                {formatDate(sub.created_at)}
              </span>
              <span
                className={`font-mono text-[0.65rem] px-2.5 py-1 rounded-full ${
                  sub.risk_level === 'High'
                    ? 'bg-coral/15 text-coral'
                    : sub.risk_level === 'Moderate'
                    ? 'bg-amber/15 text-amber'
                    : 'bg-mint-bright/15 text-mint-bright'
                }`}
              >
                {sub.risk_level} risk
              </span>
            </div>
            <div className="font-display text-text-dark font-semibold mt-2">
              {sub.cluster}
            </div>
            <div className="text-muted-dark text-xs mt-1">
              Study: {sub.study_hours_per_day}h/day · Sleep: {sub.sleep_hours}h · Stress: {sub.stress_level}/10
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default Profile