function StatCard({ label, value, onChange, step = 0.5, min = 0, max = 24 }) {
  const decrement = () => onChange(Math.max(min, +(value - step).toFixed(2)))
  const increment = () => onChange(Math.min(max, +(value + step).toFixed(2)))

  return (
    <div className="bg-card border border-card-border rounded-2xl px-4 pt-3 pb-2 shadow-sm">
      <p className="font-mono text-[0.68rem] tracking-wider uppercase text-muted-dark">
        {label}
      </p>
      <div className="flex items-center justify-between mt-1">
        <span className="font-display text-2xl font-semibold text-mint-bright">
          {value.toFixed(2)}
        </span>
        <div className="flex gap-2">
          <button
            type="button"
            onClick={decrement}
            className="w-8 h-8 rounded-full bg-white/5 text-text-dark flex items-center justify-center hover:bg-white/10 transition"
          >
            −
          </button>
          <button
            type="button"
            onClick={increment}
            className="w-8 h-8 rounded-full bg-white/5 text-text-dark flex items-center justify-center hover:bg-white/10 transition"
          >
            +
          </button>
        </div>
      </div>
    </div>
  )
}

export default StatCard