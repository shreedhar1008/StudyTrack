const ACCENT_MAP = {
  Attendance: '#E08A1F',
  'Time Management': '#E08A1F',
  'Stress Management': '#E5566E',
  'Exam Anxiety': '#E5566E',
  Motivation: '#34D399',
  'Study Time': '#34D399',
  Exercise: '#34D399',
  Sleep: '#34D399',
  'Screen Time': '#E5566E',
  'Social Media': '#E5566E',
  'Entertainment Time': '#E5566E',
}

function Analysis({ results }) {
  if (!results) {
    return (
      <div className="p-6 md:p-10 max-w-2xl mx-auto text-center">
        <p className="text-muted-light mt-10">
          Fill in your habits on the Home tab to see your personalized analysis.
        </p>
      </div>
    )
  }

  const { analysis } = results

  return (
    <div className="p-6 md:p-10 max-w-2xl mx-auto pb-24 md:pb-10">
      <span className="inline-block font-mono text-[0.7rem] tracking-wider text-mint bg-mint/10 border border-mint/30 rounded-full px-3.5 py-1.5 mb-3">
        PERSONALIZED ANALYSIS
      </span>

      <h1 className="font-display font-bold text-2xl leading-snug mb-4 bg-gradient-to-r from-ink via-mint to-cyan-500 bg-clip-text text-transparent">
        Closest match: {analysis.cluster}
      </h1>

      <div className="bg-gradient-to-br from-mint/5 to-white/60 border border-mint/25 rounded-2xl px-6 py-5 text-ink leading-relaxed backdrop-blur-sm">
        {analysis.personalized_message}
      </div>

      {analysis.recommendations?.length > 0 && (
        <>
          <div className="font-mono text-xs tracking-widest uppercase text-mint font-semibold mt-8 mb-3">
            Priority Recommendations
          </div>
          <div className="space-y-3">
            {analysis.recommendations.map((rec, i) => {
              const accent = ACCENT_MAP[rec.area] || '#34D399'
              return (
                <div
                  key={i}
                  className="bg-card border border-card-border rounded-2xl px-5 py-4 shadow-sm"
                  style={{ borderLeft: `4px solid ${accent}` }}
                >
                  <div
                    className="font-mono text-[0.68rem] tracking-widest uppercase font-semibold"
                    style={{ color: accent }}
                  >
                    {rec.area}
                  </div>
                  <div className="text-muted-dark text-sm mt-1.5 leading-relaxed">
                    {rec.recommendation}
                  </div>
                </div>
              )
            })}
          </div>
        </>
      )}
    </div>
  )
}

export default Analysis