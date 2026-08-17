import { Link } from 'react-router-dom'

function Footer() {
  return (
    <footer className="bg-card text-text-dark mt-8">
      <div className="max-w-6xl mx-auto px-6 md:px-16 py-14 grid md:grid-cols-4 gap-10">
        <div>
          <span className="font-display font-bold text-lg text-mint-bright">📚 StudyTrack</span>
          <p className="text-muted-dark text-sm mt-3 leading-relaxed">
            Turn your daily habits into a personalized path to better grades — powered by real
            student data, not generic advice.
          </p>
          <p className="text-muted-dark text-xs mt-4">Made with 💚 for students everywhere</p>
        </div>

        <div>
          <div className="font-display font-semibold mb-4">Product</div>
          <ul className="space-y-2.5 text-sm text-muted-dark">
            <li><Link to="/log" className="hover:text-mint-bright transition">Daily Log</Link></li>
            <li><Link to="/analysis" className="hover:text-mint-bright transition">Analysis</Link></li>
            <li><Link to="/plan" className="hover:text-mint-bright transition">Study Plan</Link></li>
            <li><Link to="/profile" className="hover:text-mint-bright transition">Profile</Link></li>
          </ul>
        </div>

        <div>
          <div className="font-display font-semibold mb-4">Company</div>
          <ul className="space-y-2.5 text-sm text-muted-dark">
            <li><Link to="/about" className="hover:text-mint-bright transition">About</Link></li>
            <li><Link to="/contact" className="hover:text-mint-bright transition">Contact</Link></li>
          </ul>
        </div>

        <div>
          <div className="font-display font-semibold mb-4">Legal</div>
          <ul className="space-y-2.5 text-sm text-muted-dark">
            <li><Link to="/privacy" className="hover:text-mint-bright transition">Privacy Policy</Link></li>
            <li><Link to="/terms" className="hover:text-mint-bright transition">Terms of Service</Link></li>
          </ul>
        </div>
      </div>

      <div className="border-t border-card-border">
        <div className="max-w-6xl mx-auto px-6 md:px-16 py-5 flex flex-col md:flex-row items-center justify-between gap-3 text-xs text-muted-dark">
          <span>© {new Date().getFullYear()} StudyTrack. All rights reserved.</span>
          <div className="flex gap-5">
            <Link to="/privacy" className="hover:text-mint-bright transition">Privacy Policy</Link>
            <Link to="/terms" className="hover:text-mint-bright transition">Terms of Service</Link>
          </div>
        </div>
      </div>
    </footer>
  )
}

export default Footer