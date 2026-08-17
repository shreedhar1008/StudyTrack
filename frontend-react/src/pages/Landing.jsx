import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import Footer from '../components/Footer'

const features = [
  { icon: '🎯', title: 'Personalized Recommendations', desc: 'Every suggestion is benchmarked against real peer data — not generic advice.' },
  { icon: '📅', title: '7-Day Study Plans', desc: 'A structured weekly plan built around your actual habits and goals.' },
  { icon: '📈', title: 'Track Your Progress', desc: 'See how your habits and risk level evolve over time, check-in by check-in.' },
]

const steps = [
  { num: '01', title: 'Log your habits', desc: 'Study hours, sleep, stress, motivation — takes under a minute.' },
  { num: '02', title: 'Get AI-powered analysis', desc: 'Your closest behavioral match, plus prioritized, honest recommendations.' },
  { num: '03', title: 'Follow your plan', desc: 'A personalized 7-day schedule built around what actually needs to change.' },
]

const fadeUp = {
  hidden: { opacity: 0, y: 24 },
  show: { opacity: 1, y: 0, transition: { duration: 0.5, ease: 'easeOut' } },
}

const stagger = {
  hidden: {},
  show: { transition: { staggerChildren: 0.12 } },
}

function Landing() {
  return (
    <div className="min-h-screen bg-bg relative overflow-hidden">
      {/* Animated background blobs */}
      <motion.div
        className="pointer-events-none absolute -top-32 -left-32 w-96 h-96 rounded-full blur-3xl"
        style={{ background: 'radial-gradient(circle, rgba(34,181,124,0.18), transparent 70%)' }}
        animate={{ x: [0, 30, 0], y: [0, 20, 0] }}
        transition={{ duration: 12, repeat: Infinity, ease: 'easeInOut' }}
      />
      <motion.div
        className="pointer-events-none absolute top-40 -right-32 w-96 h-96 rounded-full blur-3xl"
        style={{ background: 'radial-gradient(circle, rgba(45,190,219,0.15), transparent 70%)' }}
        animate={{ x: [0, -25, 0], y: [0, 25, 0] }}
        transition={{ duration: 14, repeat: Infinity, ease: 'easeInOut' }}
      />

      {/* Top bar */}
      <motion.div
        initial={{ opacity: 0, y: -12 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4 }}
        className="relative flex items-center justify-between px-6 md:px-16 py-6 max-w-6xl mx-auto"
      >
        <span className="font-display font-bold text-xl text-ink">📚 StudyTrack</span>
        <Link
          to="/log"
          className="font-mono text-xs tracking-wide text-mint border border-mint/40 rounded-full px-4 py-2 hover:bg-mint/10 hover:scale-105 transition-all"
        >
          Get Started →
        </Link>
      </motion.div>

      {/* Hero */}
      <motion.section
        initial="hidden"
        animate="show"
        variants={stagger}
        className="relative px-6 md:px-16 max-w-6xl mx-auto pt-12 md:pt-20 pb-16 grid md:grid-cols-2 gap-10 items-center"
      >
        <div className="text-center md:text-left">
          <motion.span
            variants={fadeUp}
            className="inline-block font-mono text-[0.7rem] tracking-wider text-mint bg-mint/10 border border-mint/30 rounded-full px-3.5 py-1.5 mb-6"
          >
            AI STUDY MENTOR
          </motion.span>
          <motion.h1
            variants={fadeUp}
            className="font-display font-bold text-4xl md:text-5xl leading-tight text-ink"
          >
            Study smarter,{' '}
            <span className="bg-gradient-to-r from-mint via-mint-bright to-cyan-500 bg-clip-text text-transparent">
              not just harder.
            </span>
          </motion.h1>
          <motion.p variants={fadeUp} className="text-muted-light text-lg mt-5 max-w-md mx-auto md:mx-0">
            StudyTrack analyzes your real habits against thousands of student patterns and gives you
            honest, personalized guidance — not generic study tips.
          </motion.p>
          <motion.div variants={fadeUp}>
            <Link to="/log">
              <motion.span
                whileHover={{ scale: 1.05, y: -2 }}
                whileTap={{ scale: 0.97 }}
                animate={{
                  boxShadow: [
                    '0 8px 24px rgba(34,181,124,0.3)',
                    '0 12px 32px rgba(34,181,124,0.5)',
                    '0 8px 24px rgba(34,181,124,0.3)',
                  ],
                }}
                transition={{ boxShadow: { duration: 2.5, repeat: Infinity, ease: 'easeInOut' } }}
                className="inline-block mt-8 bg-gradient-to-br from-mint to-mint-bright text-[#06251A] font-display font-bold rounded-full px-8 py-4 cursor-pointer"
              >
                ✨ Start Your Free Analysis
              </motion.span>
            </Link>
          </motion.div>
        </div>

        <motion.div
          variants={fadeUp}
          className="relative rounded-3xl overflow-hidden aspect-[4/3] bg-gradient-to-br from-mint/20 via-cyan-500/10 to-amber/10 border border-card-border"
        >
          <img
            src="/hero-mentor.jpg"
            alt="Student studying with AI-powered guidance"
            className="w-full h-full object-cover"
            onError={(e) => { e.target.style.display = 'none' }}
          />
        </motion.div>
      </motion.section>

      {/* How it works */}
      <section className="relative px-6 md:px-16 max-w-5xl mx-auto py-12">
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          className="font-mono text-xs tracking-widest uppercase text-mint font-semibold mb-6 text-center"
        >
          How It Works
        </motion.div>
        <motion.div
          initial="hidden"
          whileInView="show"
          viewport={{ once: true, amount: 0.3 }}
          variants={stagger}
          className="grid md:grid-cols-3 gap-5"
        >
          {steps.map((s) => (
            <motion.div
              key={s.num}
              variants={fadeUp}
              whileHover={{ y: -6, borderColor: 'rgba(34,211,153,0.5)' }}
              className="bg-card border border-card-border rounded-2xl p-6 transition-colors"
            >
              <div className="font-mono text-mint-bright text-sm mb-2">{s.num}</div>
              <div className="font-display font-semibold text-text-dark text-lg mb-2">{s.title}</div>
              <div className="text-muted-dark text-sm leading-relaxed">{s.desc}</div>
            </motion.div>
          ))}
        </motion.div>
      </section>

      {/* Features */}
      <section className="relative px-6 md:px-16 max-w-5xl mx-auto py-12">
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          className="font-mono text-xs tracking-widest uppercase text-amber font-semibold mb-6 text-center"
        >
          What You Get
        </motion.div>
        <motion.div
          initial="hidden"
          whileInView="show"
          viewport={{ once: true, amount: 0.3 }}
          variants={stagger}
          className="grid md:grid-cols-3 gap-5"
        >
          {features.map((f) => (
            <motion.div
              key={f.title}
              variants={fadeUp}
              whileHover={{ y: -6, scale: 1.02 }}
              className="bg-white border border-gray-200 rounded-2xl p-6 shadow-sm hover:shadow-lg transition-shadow"
            >
              <motion.div
                className="text-2xl mb-3"
                whileHover={{ rotate: [0, -10, 10, 0], scale: 1.2 }}
                transition={{ duration: 0.4 }}
              >
                {f.icon}
              </motion.div>
              <div className="font-display font-semibold text-ink text-lg mb-2">{f.title}</div>
              <div className="text-muted-light text-sm leading-relaxed">{f.desc}</div>
            </motion.div>
          ))}
        </motion.div>
      </section>

      {/* Bottom CTA */}
      <motion.section
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.5 }}
        className="relative px-6 md:px-16 max-w-3xl mx-auto text-center py-16"
      >
        <h2 className="font-display font-bold text-2xl md:text-3xl text-ink mb-4">
          Ready to see your patterns?
        </h2>
        <Link to="/log">
          <motion.span
            whileHover={{ scale: 1.05, y: -2 }}
            whileTap={{ scale: 0.97 }}
            className="inline-block bg-gradient-to-br from-mint to-mint-bright text-[#06251A] font-display font-bold rounded-full px-8 py-4 shadow-[0_8px_24px_rgba(34,181,124,0.3)] cursor-pointer"
          >
            ✨ Get My Personalized Analysis
          </motion.span>
        </Link>
      </motion.section>

      <Footer />
    </div>
  )
}

export default Landing