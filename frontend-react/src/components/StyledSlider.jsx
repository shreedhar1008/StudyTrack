function StyledSlider({ label, value, onChange, min = 1, max = 10, accent = "mint-bright" }) {
  const percent = ((value - min) / (max - min)) * 100

  return (
    <div className="bg-card border border-card-border rounded-2xl px-5 pt-4 pb-5 shadow-sm">
      <div className="flex items-center justify-between">
        <p className="font-mono text-[0.68rem] tracking-wider uppercase text-muted-dark">
          {label}
        </p>
        <span className="font-mono text-sm font-semibold text-mint-bright">{value}</span>
      </div>
      <input
        type="range"
        min={min}
        max={max}
        value={value}
        onChange={(e) => onChange(Number(e.target.value))}
        className="w-full mt-3 h-1.5 rounded-full appearance-none cursor-pointer accent-emerald-400"
        style={{
          background: `linear-gradient(to right, #34D399 ${percent}%, #2A3348 ${percent}%)`
        }}
      />
    </div>
  )
}

export default StyledSlider