import axios from 'axios'

const API_URL = 'https://studytrack-backend-68aq.onrender.com'

const client = axios.create({
  baseURL: API_URL,
  timeout: 60000, // 60s — Render free tier can be slow to wake up from sleep
})

export async function analyzeStudent(payload) {
  const res = await client.post('/analyze', payload)
  return res.data
}

export async function getStudyPlan(payload) {
  const res = await client.post('/plan', payload)
  return res.data
}

export async function getHistory(anonId) {
  const res = await client.get(`/history/${anonId}`)
  return res.data
}

export async function getUserHistory(userId) {
  const res = await client.get(`/user-history/${userId}`)
  return res.data
}