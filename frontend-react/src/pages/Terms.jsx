import Footer from '../components/Footer'
import { Link } from 'react-router-dom'

function Terms() {
  return (
    <div className="min-h-screen bg-bg">
      <div className="flex items-center justify-between px-6 md:px-16 py-6 max-w-6xl mx-auto">
        <Link to="/" className="font-display font-bold text-xl text-ink">📚 StudyTrack</Link>
        <Link to="/log" className="font-mono text-xs tracking-wide text-mint border border-mint/40 rounded-full px-4 py-2 hover:bg-mint/10 transition">Get Started →</Link>
      </div>
      <div className="max-w-2xl mx-auto px-6 md:px-16 py-12">
        <h1 className="font-display font-bold text-3xl text-ink mb-2">Terms of Service</h1>
        <p className="text-muted-light text-sm mb-8">Last updated: {new Date().toLocaleDateString()}</p>
        <div className="text-muted-light space-y-5 leading-relaxed text-sm">
          <div>
            <h2 className="font-display font-semibold text-ink text-base mb-2">Educational purpose</h2>
            <p>StudyTrack provides study habit recommendations for informational purposes. It is not a substitute for academic, medical, or mental health advice.</p>
          </div>
          <div>
            <h2 className="font-display font-semibold text-ink text-base mb-2">No guarantees</h2>
            <p>Recommendations are based on statistical patterns in aggregate student data and do not guarantee any specific academic outcome.</p>
          </div>
          <div>
            <h2 className="font-display font-semibold text-ink text-base mb-2">Fair use</h2>
            <p>This is a free educational tool. Please don't attempt to abuse, scrape, or overload the service.</p>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  )
}

export default Terms