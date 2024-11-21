import React from 'react';
import { diagnosticQuestions } from '../data/questions';
import { useDiagnosticStore } from '../store/diagnosticStore';

interface DiagnosticQuestionProps {
  questionId: number;
  onAnswer: (answer: boolean) => void;
}

export const DiagnosticQuestion: React.FC<DiagnosticQuestionProps> = ({ questionId, onAnswer }) => {
  const question = diagnosticQuestions.find(q => q.id === questionId);
  
  if (!question) return null;

  return (
    <div className="bg-white rounded-lg p-4 shadow-sm">
      <p className="text-sm text-purple-600 font-medium mb-2">{question.category}</p>
      <p className="text-gray-800 mb-4">{question.text}</p>
      <div className="flex gap-2">
        <button
          onClick={() => onAnswer(true)}
          className="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 focus:ring-2 focus:ring-green-300"
        >
          Yes
        </button>
        <button
          onClick={() => onAnswer(false)}
          className="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600 focus:ring-2 focus:ring-red-300"
        >
          No
        </button>
      </div>
    </div>
  );
};