import Footer from '../components/Footer'
import { Link } from 'react-router-dom'

function Privacy() {
  return (
    <div className="min-h-screen bg-bg">
      <div className="flex items-center justify-between px-6 md:px-16 py-6 max-w-6xl mx-auto">
        <Link to="/" className="font-display font-bold text-xl text-ink">📚 StudyTrack</Link>
        <Link to="/log" className="font-mono text-xs tracking-wide text-mint border border-mint/40 rounded-full px-4 py-2 hover:bg-mint/10 transition">Get Started →</Link>
      </div>
      <div className="max-w-2xl mx-auto px-6 md:px-16 py-12">
        <h1 className="font-display font-bold text-3xl text-ink mb-2">Privacy Policy</h1>
        <p className="text-muted-light text-sm mb-8">Last updated: {new Date().toLocaleDateString()}</p>
        <div className="text-muted-light space-y-5 leading-relaxed text-sm">
          <div>
            <h2 className="font-display font-semibold text-ink text-base mb-2">What we collect</h2>
            <p>The study habit data you enter (study hours, sleep, stress, etc.) and an anonymous device identifier stored in your browser — no name, email, or account is required to use StudyTrack.</p>
          </div>
          <div>
            <h2 className="font-display font-semibold text-ink text-base mb-2">How it's used</h2>
            <p>Your inputs are sent to our AI models to generate your analysis and study plan, and saved so you can view your history. We do not sell or share your data with third parties.</p>
          </div>
          <div>
            <h2 className="font-display font-semibold text-ink text-base mb-2">Your control</h2>
            <p>Since we don't collect identifying information, your history is tied only to your browser's local device ID. Clearing your browser storage removes access to that history.</p>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  )
}

export default Privacy