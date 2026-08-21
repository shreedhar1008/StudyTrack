import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://rrwguzqvebkekcpnhkhs.supabase.co'
const supabaseKey = 'sb_publishable_erbRP_EOLnceZllnwmdN6Q_iwhGFE8o'

export const supabase = createClient(supabaseUrl, supabaseKey)