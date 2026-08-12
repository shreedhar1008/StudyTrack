function PrimaryButton({ children, onClick, type = "button", disabled = false }) {
  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      className="w-full bg-gradient-to-br from-mint to-mint-bright text-[#06251A] font-display font-bold rounded-full py-3.5 shadow-[0_8px_24px_rgba(34,181,124,0.3)] hover:-translate-y-0.5 hover:shadow-[0_10px_28px_rgba(34,181,124,0.4)] transition disabled:opacity-50 disabled:cursor-not-allowed"
    >
      {children}
    </button>
  )
}

export default PrimaryButton