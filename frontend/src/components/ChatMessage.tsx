import React from 'react';
import { Bot, User } from 'lucide-react';

interface ChatMessageProps {
  content: string;
  isBot: boolean;
  timestamp: string;
}

export const ChatMessage: React.FC<ChatMessageProps> = ({ content, isBot, timestamp }) => {
  return (
    <div className={`flex gap-3 ${isBot ? 'flex-row' : 'flex-row-reverse'}`}>
      <div className={`flex-shrink-0 h-8 w-8 rounded-full flex items-center justify-center ${
        isBot ? 'bg-purple-100' : 'bg-gray-100'
      }`}>
        {isBot ? (
          <Bot className="h-5 w-5 text-purple-600" />
        ) : (
          <User className="h-5 w-5 text-gray-600" />
        )}
      </div>
      
      <div className={`flex flex-col max-w-[80%] ${isBot ? 'items-start' : 'items-end'}`}>
        <div className={`rounded-lg px-4 py-2 ${
          isBot ? 'bg-purple-100 text-purple-900' : 'bg-gray-100 text-gray-900'
        }`}>
          {content}
        </div>
        <span className="text-xs text-gray-500 mt-1">
          {new Date(timestamp).toLocaleTimeString()}
        </span>
      </div>
    </div>
  );
};