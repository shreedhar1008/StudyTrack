function SectionLabel({ children, accent = "mint" }) {
  const color = accent === "amber" ? "text-amber" : "text-mint"
  return (
    <div className={`font-mono text-xs tracking-widest uppercase ${color} font-semibold mt-8 mb-3`}>
      {children}
    </div>
  )
}

export default SectionLabel