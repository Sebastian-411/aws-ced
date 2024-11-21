import { createClient } from '@supabase/supabase-js';

const supabaseUrl = 'https://ouswqesmrkhmaujqdnje.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im91c3dxZXNtcmtobWF1anFkbmplIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIxNTY2MDAsImV4cCI6MjA0NzczMjYwMH0.OBf4_L0zcw2Czl5IXSpzBNRyM2rbICb5rA_WnBu-HzQ';

export const supabase = createClient(supabaseUrl, supabaseKey);