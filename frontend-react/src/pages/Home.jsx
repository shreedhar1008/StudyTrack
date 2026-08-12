import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import StatCard from '../components/StatCard'
import StyledSlider from '../components/StyledSlider'
import SectionLabel from '../components/SectionLabel'
import PrimaryButton from '../components/PrimaryButton'
import { analyzeStudent, getStudyPlan } from '../api/studytrack'
import { getAnonId } from '../hooks/useAnonId'

function Home({ setResults, loading, setLoading, error, setError }) {
  const navigate = useNavigate()
  const [form, setForm] = useState({
    study_hours_per_day: 3.0,
    sleep_hours: 7.0,
    social_media_hours: 2.0,
    exercise_frequency: 2.0,
    netflix_hours: 1.0,
    screen_time: 8.0,
    attendance_percentage: 80,
    motivation_level: 5,
    exam_anxiety_score: 5,
    stress_level: 5,
    time_management_score: 5,
    major: '',
  })

  const update = (key) => (value) => setForm((prev) => ({ ...prev, [key]: value }))

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    try {
      const payload = { ...form, major: form.major || 'not specified', anon_id: getAnonId() }
      const [analysis, plan] = await Promise.all([
        analyzeStudent(payload),
        getStudyPlan(payload),
      ])
      setResults({ analysis, plan })
      navigate('/analysis')
    } catch (err) {
      setError('Could not reach the server. The free backend may be waking up — please try again in a few seconds.')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="p-6 md:p-10 max-w-2xl mx-auto pb-24 md:pb-10">
      <span className="inline-block font-mono text-[0.7rem] tracking-wider text-mint bg-mint/10 border border-mint/30 rounded-full px-3.5 py-1.5 mb-3">
        AI STUDY COACH
      </span>
      <h1 className="font-display text-3xl font-bold text-ink">📚 Daily Log</h1>
      <p className="text-muted-light mt-2 mb-6">
        Track your habits to get a personalized analysis, recommendations, and a 7-day study plan.
      </p>

      {error && (
        <div className="bg-coral/10 border border-coral/30 text-coral rounded-xl px-4 py-3 mb-4 text-sm">
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit} className={loading ? 'opacity-60 pointer-events-none transition' : 'transition'}>
        <SectionLabel>Study &amp; Time</SectionLabel>
        <div className="grid grid-cols-2 gap-3">
          <StatCard label="Study Hours/Day" value={form.study_hours_per_day} onChange={update('study_hours_per_day')} step={0.5} max={24} />
          <StatCard label="Sleep Hours" value={form.sleep_hours} onChange={update('sleep_hours')} step={0.5} max={24} />
          <StatCard label="Social Media Hrs" value={form.social_media_hours} onChange={update('social_media_hours')} step={0.5} max={24} />
          <StatCard label="Exercise Sessions/Wk" value={form.exercise_frequency} onChange={update('exercise_frequency')} step={1} max={14} />
          <StatCard label="Netflix/Streaming Hrs" value={form.netflix_hours} onChange={update('netflix_hours')} step={0.5} max={24} />
          <StatCard label="Total Screen Time" value={form.screen_time} onChange={update('screen_time')} step={0.5} max={24} />
        </div>

        <div className="mt-3">
          <StyledSlider label="Class Attendance (%)" value={form.attendance_percentage} onChange={update('attendance_percentage')} min={0} max={100} />
        </div>

        <SectionLabel accent="amber">Wellbeing &amp; Mindset</SectionLabel>
        <div className="grid grid-cols-2 gap-3">
          <StyledSlider label="Motivation" value={form.motivation_level} onChange={update('motivation_level')} min={1} max={10} />
          <StyledSlider label="Anxiety" value={form.exam_anxiety_score} onChange={update('exam_anxiety_score')} min={1} max={10} />
          <StyledSlider label="Stress" value={form.stress_level} onChange={update('stress_level')} min={1} max={10} />
          <StyledSlider label="Time Management" value={form.time_management_score} onChange={update('time_management_score')} min={1} max={10} />
        </div>

        <div className="mt-5">
          <label className="font-mono text-[0.68rem] tracking-wider uppercase text-muted-light block mb-2">
            Your major/field of study (optional)
          </label>
          <input
            type="text"
            value={form.major}
            onChange={(e) => update('major')(e.target.value)}
            className="w-full bg-white border border-gray-200 rounded-2xl px-4 py-3 text-ink font-display outline-none focus:border-mint transition"
            placeholder="e.g. Computer Science"
          />
        </div>

        <div className="mt-6">
          <PrimaryButton type="submit" disabled={loading} loading={loading}>
            {loading ? 'Analyzing your habits...' : '✨ Get My Personalized Analysis'}
          </PrimaryButton>
        </div>
      </form>
    </div>
  )
}

export default Home