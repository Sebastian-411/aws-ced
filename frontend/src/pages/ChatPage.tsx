import React, { useEffect, useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';
import { useDiagnosticStore } from '../store/diagnosticStore';
import { ChatDatabase } from '../lib/db';
import { ChatMessage } from '../components/ChatMessage';
import { DiagnosticQuestion } from '../components/DiagnosticQuestion';
import { ConversationList } from '../components/ConversationList';
import { LogOut, AlertCircle } from 'lucide-react';

export const ChatPage = () => {
  const { user, signOut } = useAuthStore();
  const { currentQuestions, initialize, addAnswer, submitDiagnosis } = useDiagnosticStore();
  const navigate = useNavigate();
  const [messages, setMessages] = useState<any[]>([]);
  const [conversations, setConversations] = useState<any[]>([]);
  const [currentConversationId, setCurrentConversationId] = useState<number | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const [db, setDb] = useState<ChatDatabase | null>(null);

  useEffect(() => {
    if (!user) {
      navigate('/');
      return;
    }

    const initDb = async () => {
      try {
        const chatDb = await ChatDatabase.getInstance();
        setDb(chatDb);
        const userConversations = chatDb.getConversations(user.id);
        setConversations(userConversations);
        
        if (userConversations.length > 0) {
          const latestConversationId = userConversations[0][0];
          setCurrentConversationId(latestConversationId);
          const conversationMessages = chatDb.getMessages(latestConversationId);
          setMessages(conversationMessages);
        }
      } catch (err) {
        setError('Failed to initialize chat. Please refresh the page.');
      } finally {
        setLoading(false);
      }
    };

    initDb();
    initialize();
  }, [user, navigate, initialize]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleNewConversation = async () => {
    if (!db || !user) return;

    try {
      const title = `Diagnostic Session ${new Date().toLocaleString()}`;
      const conversationId = await db.createConversation(user.id, title);
      setCurrentConversationId(conversationId);
      setMessages([]);
      setCurrentQuestionIndex(0);
      initialize();
      
      const updatedConversations = db.getConversations(user.id);
      setConversations(updatedConversations);
    } catch (err) {
      setError('Failed to create new conversation');
    }
  };

  const handleSelectConversation = (conversationId: number) => {
    if (!db) return;
    
    const conversationMessages = db.getMessages(conversationId);
    setMessages(conversationMessages);
    setCurrentConversationId(conversationId);
  };

  const handleQuestionAnswer = async (answer: boolean) => {
    if (!db || !user || !currentConversationId) return;

    try {
      const questionId = currentQuestions[currentQuestionIndex];
      if (answer) {
        addAnswer(questionId);
      }

      await db.saveMessage(
        currentConversationId,
        user.id,
        `Question ${currentQuestionIndex + 1}: ${answer ? 'Yes' : 'No'}`,
        false
      );
      
      if (currentQuestionIndex === currentQuestions.length - 1) {
        try {
          var response = await submitDiagnosis();



          console.log(response.recommendations)

            await Promise.all(
            Object.entries(response.recommendations).map(async ([key, recommendation]: [string, any]) => {
              console.log(recommendation);
              await db.saveMessage(
              currentConversationId,
              user.id,
              `Recommendation: ${recommendation}`,
              true
              );
            })
            );
        } catch (error) {
          await db.saveMessage(
            currentConversationId,
            user.id,
            'Failed to submit diagnosis. The diagnostic service might be unavailable.',
            true
          );
        }
      } else {
        setCurrentQuestionIndex(prev => prev + 1);
      }
      
      const updatedMessages = db.getMessages(currentConversationId);
      setMessages(updatedMessages);
    } catch (err) {
      setError('Failed to process your answer. Please try again.');
    }
  };

  const handleSignOut = async () => {
    await signOut();
    navigate('/');
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-4 border-purple-500 border-t-transparent"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      <header className="bg-white shadow-sm">
        <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
          <h1 className="text-xl font-semibold text-gray-900">
            Vehicle Diagnostic Chat
          </h1>
          <button
            onClick={handleSignOut}
            className="flex items-center gap-2 text-gray-600 hover:text-gray-900"
          >
            <LogOut className="h-5 w-5" />
            Sign Out
          </button>
        </div>
      </header>

      <main className="flex-1 max-w-6xl w-full mx-auto flex">
        <ConversationList
          conversations={conversations.map(([id, title, created_at]) => ({
            id,
            title,
            created_at,
          }))}
          currentConversationId={currentConversationId}
          onSelectConversation={handleSelectConversation}
          onNewConversation={handleNewConversation}
        />

        <div className="flex-1 p-4 flex flex-col">
          {error && (
            <div className="mb-4 bg-red-50 border border-red-200 rounded-lg p-4 flex items-center gap-2 text-red-700">
              <AlertCircle className="h-5 w-5 flex-shrink-0" />
              <p>{error}</p>
            </div>
          )}
          
          <div className="flex-1 space-y-4 overflow-y-auto mb-4">
            {messages.map((msg, index) => (
              <ChatMessage
                key={index}
                content={msg[3]}
                isBot={msg[4]}
                timestamp={msg[5]}
              />
            ))}
            {currentConversationId && currentQuestionIndex < currentQuestions.length && (
              <DiagnosticQuestion
                questionId={currentQuestions[currentQuestionIndex]}
                onAnswer={handleQuestionAnswer}
              />
            )}
            <div ref={messagesEndRef} />
          </div>
        </div>
      </main>
    </div>
  );
};