import { create } from 'zustand';
import { diagnosticQuestions } from '../data/questions';

interface DiagnosticState {
  currentQuestions: number[];
  answers: Set<number>;
  initialize: () => void;
  addAnswer: (id: number) => void;
  removeAnswer: (id: number) => void;
  getRandomQuestions: (count: number) => void;
  submitDiagnosis: () => Promise<any>;
}

export const useDiagnosticStore = create<DiagnosticState>((set, get) => ({
  currentQuestions: [],
  answers: new Set(),

  initialize: () => {
    set({ answers: new Set(), currentQuestions: [] });
    get().getRandomQuestions(10);
  },

  addAnswer: (id: number) => {
    const answers = new Set(get().answers);
    answers.add(id);
    set({ answers });
  },

  removeAnswer: (id: number) => {
    const answers = new Set(get().answers);
    answers.delete(id);
    set({ answers });
  },

  getRandomQuestions: (count: number) => {
    const allQuestions = [...Array(54)].map((_, i) => i + 1);
    const shuffled = allQuestions.sort(() => Math.random() - 0.5).slice(0, count);
    set({ currentQuestions: shuffled });
  },

  submitDiagnosis: async () => {
    const response = await fetch('http://localhost:5000/diagnostic', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        symptoms: Array.from(get().answers),
      }),
    });
    
    if (!response.ok) {
      throw new Error('Failed to submit diagnosis');
    }

    return response.json();
  },
}));