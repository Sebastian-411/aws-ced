import React from 'react';
import { MessageSquarePlus } from 'lucide-react';

interface Conversation {
  id: number;
  title: string;
  created_at: string;
}

interface ConversationListProps {
  conversations: Conversation[];
  currentConversationId: number | null;
  onSelectConversation: (id: number) => void;
  onNewConversation: () => void;
}

export const ConversationList: React.FC<ConversationListProps> = ({
  conversations,
  currentConversationId,
  onSelectConversation,
  onNewConversation,
}) => {
  return (
    <div className="w-64 bg-gray-50 border-r border-gray-200 p-4 flex flex-col h-full">
      <button
        onClick={onNewConversation}
        className="w-full mb-4 bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 focus:ring-4 focus:ring-purple-300 flex items-center justify-center gap-2"
      >
        <MessageSquarePlus className="h-5 w-5" />
        New Conversation
      </button>
      
      <div className="flex-1 overflow-y-auto space-y-2">
        {conversations.map((conversation) => (
          <button
            key={conversation.id}
            onClick={() => onSelectConversation(conversation.id)}
            className={`w-full text-left px-3 py-2 rounded-lg transition-colors ${
              currentConversationId === conversation.id
                ? 'bg-purple-100 text-purple-900'
                : 'hover:bg-gray-100 text-gray-700'
            }`}
          >
            <p className="font-medium truncate">{conversation.title}</p>
            <p className="text-xs text-gray-500">
              {new Date(conversation.created_at).toLocaleDateString()}
            </p>
          </button>
        ))}
      </div>
    </div>
  );
};