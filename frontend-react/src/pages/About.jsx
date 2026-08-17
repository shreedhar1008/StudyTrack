import Footer from '../components/Footer'
import { Link } from 'react-router-dom'

function About() {
  return (
    <div className="min-h-screen bg-bg">
      <div className="flex items-center justify-between px-6 md:px-16 py-6 max-w-6xl mx-auto">
        <Link to="/" className="font-display font-bold text-xl text-ink">📚 StudyTrack</Link>
        <Link to="/log" className="font-mono text-xs tracking-wide text-mint border border-mint/40 rounded-full px-4 py-2 hover:bg-mint/10 transition">Get Started →</Link>
      </div>
      <div className="max-w-2xl mx-auto px-6 md:px-16 py-12">
        <h1 className="font-display font-bold text-3xl text-ink mb-6">About StudyTrack</h1>
        <div className="text-muted-light space-y-4 leading-relaxed">
          <p>
            StudyTrack was built to solve a simple problem: most study advice is generic. "Study more,"
            "reduce stress," "manage your time better" — true, but not actionable.
          </p>
          <p>
            We analyzed real behavioral patterns from thousands of students to build a system that
            compares your actual habits against students with similar profiles who perform well — then
            tells you specifically what's holding you back, backed by real gaps in the data.
          </p>
          <p>
            Every recommendation is grounded in your real numbers. No invented statistics, no generic
            filler — just an honest, personalized read on your habits and a practical plan to improve them.
          </p>
        </div>
      </div>
      <Footer />
    </div>
  )
}

export default About