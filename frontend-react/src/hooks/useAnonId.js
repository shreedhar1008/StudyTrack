const ANON_ID_KEY = 'studytrack_anon_id'

function generateId() {
  return 'anon_' + Math.random().toString(36).slice(2, 10) + Date.now().toString(36)
}

export function getAnonId() {
  let id = localStorage.getItem(ANON_ID_KEY)
  if (!id) {
    id = generateId()
    localStorage.setItem(ANON_ID_KEY, id)
  }
  return id
}