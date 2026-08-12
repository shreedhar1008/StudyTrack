import { NavLink, Outlet } from 'react-router-dom'

const navItems = [
  { to: '/', label: 'Home', icon: '🏠' },
  { to: '/analysis', label: 'Analysis', icon: '📊' },
  { to: '/plan', label: 'Plan', icon: '📅' },
  { to: '/profile', label: 'Profile', icon: '👤' },
]

function NavShell() {
  return (
    <div className="min-h-screen bg-bg flex">
      {/* Desktop sidebar */}
      <aside className="hidden md:flex flex-col w-56 border-r border-card-border bg-card min-h-screen p-6 gap-2">
        <h2 className="font-display font-bold text-mint-bright text-xl mb-6">📚 StudyTrack</h2>
        {navItems.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            end={item.to === '/'}
            className={({ isActive }) =>
              `flex items-center gap-3 px-4 py-3 rounded-xl font-mono text-sm transition ${
                isActive ? 'bg-mint/10 text-mint-bright' : 'text-muted-dark hover:bg-white/5'
              }`
            }
          >
            <span>{item.icon}</span>
            {item.label}
          </NavLink>
        ))}
      </aside>

      {/* Main content */}
      <main className="flex-1 pb-20 md:pb-0">
        <Outlet />
      </main>

      {/* Mobile bottom nav */}
      <nav className="md:hidden fixed bottom-0 left-0 right-0 bg-card border-t border-card-border flex justify-around py-2 z-50">
        {navItems.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            end={item.to === '/'}
            className={({ isActive }) =>
              `flex flex-col items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-mono ${
                isActive ? 'text-mint-bright' : 'text-muted-dark'
              }`
            }
          >
            <span className="text-lg">{item.icon}</span>
            {item.label}
          </NavLink>
        ))}
      </nav>
    </div>
  )
}

export default NavShell