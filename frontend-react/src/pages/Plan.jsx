import { useState } from 'react'

const ICON_MAP = {
  morning: '🌤️',
  afternoon: '📖',
  evening: '🌙',
  night: '😴',
  'before study block': '🧘',
  'mid-session': '⏱️',
}

function getIcon(timeLabel) {
  return ICON_MAP[timeLabel.trim().toLowerCase()] || '•'
}

function Plan({ results }) {
  const [activeDay, setActiveDay] = useState(null)

  if (!results) {
    return (
      <div className="p-6 md:p-10 max-w-2xl mx-auto text-center">
        <p className="text-muted-light mt-10">
          Fill in your habits on the Home tab to see your 7-day study plan.
        </p>
      </div>
    )
  }

  const { plan } = results
  const days = Object.keys(plan.weekly_plan)
  const selectedDay = activeDay || days[0]

  const delta = +(plan.target_study_hours_per_day - plan.current_study_hours_per_day).toFixed(1)
  const deltaStr = delta >= 0 ? `+${delta}h from current` : `${delta}h from current`

  return (
    <div className="p-6 md:p-10 max-w-2xl mx-auto pb-24 md:pb-10">
      <span className="inline-block font-mono text-[0.7rem] tracking-wider text-mint bg-mint/10 border border-mint/30 rounded-full px-3.5 py-1.5 mb-3">
        7-DAY PLAN
      </span>
      <h1 className="font-display text-2xl font-bold text-ink mb-2">Your Study Plan</h1>
      <p className="text-muted-light mb-6">{plan.plan_summary}</p>

      {/* Metric card */}
      <div className="bg-card border border-card-border rounded-2xl px-6 py-5 shadow-sm mb-6">
        <div className="font-mono text-[0.7rem] tracking-widest uppercase text-muted-dark">
          Target study hours/day
        </div>
        <div className="font-display text-4xl font-bold text-mint-bright mt-1">
          {plan.target_study_hours_per_day}h
        </div>
        <span className="inline-block font-mono text-xs text-mint-bright bg-mint-bright/15 rounded-full px-3 py-1 mt-2">
          {deltaStr}
        </span>
      </div>

      {/* Day tabs */}
      <div className="flex gap-2 overflow-x-auto pb-2 mb-4">
        {days.map((day) => (
          <button
            key={day}
            onClick={() => setActiveDay(day)}
            className={`font-mono text-xs whitespace-nowrap px-4 py-2 rounded-full border transition ${
              selectedDay === day
                ? 'bg-mint text-white border-mint'
                : 'bg-white text-muted-light border-gray-200 hover:border-mint/50'
            }`}
          >
            {day}
          </button>
        ))}
      </div>

      {/* Timeline for selected day */}
      <div className="space-y-3">
        {plan.weekly_plan[selectedDay].map((block, i) => (
          <div
            key={i}
            className="bg-card border border-card-border rounded-2xl px-5 py-4 flex gap-3 items-start shadow-sm"
          >
            <div className="text-xl leading-none mt-0.5">{getIcon(block.time)}</div>
            <div>
              <div className="font-mono text-[0.68rem] tracking-widest uppercase text-amber font-semibold">
                {block.time}
              </div>
              <div className="text-text-dark text-sm mt-1">{block.activity}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default Plan