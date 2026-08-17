import Footer from '../components/Footer'
import { Link } from 'react-router-dom'

function Contact() {
  return (
    <div className="min-h-screen bg-bg">
      <div className="flex items-center justify-between px-6 md:px-16 py-6 max-w-6xl mx-auto">
        <Link to="/" className="font-display font-bold text-xl text-ink">📚 StudyTrack</Link>
        <Link to="/log" className="font-mono text-xs tracking-wide text-mint border border-mint/40 rounded-full px-4 py-2 hover:bg-mint/10 transition">Get Started →</Link>
      </div>
      <div className="max-w-2xl mx-auto px-6 md:px-16 py-12">
        <h1 className="font-display font-bold text-3xl text-ink mb-6">Get in Touch</h1>
        <p className="text-muted-light mb-8">
          Questions, feedback, or found something that doesn't feel right? We'd like to hear about it.
        </p>
        <div className="bg-card border border-card-border rounded-2xl p-6">
          <p className="font-mono text-sm text-muted-dark">EMAIL</p>
          <p className="text-mint-bright font-display text-lg mt-1">hello@studytrack.app</p>
        </div>
      </div>
      <Footer />
    </div>
  )
}

export default Contact