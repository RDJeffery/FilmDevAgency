import React, { useState } from 'react';
import { MessageSquare, X } from 'lucide-react';
import { Button } from '../ui/button';
import { Input } from '../ui/input';
import { ChatMessage, type Message } from './ChatMessage';
import { ChatInput } from './ChatInput';

export function ChatBar() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>([]);

  const handleSendMessage = (content: string) => {
    const newMessage: Message = {
      id: Date.now().toString(),
      content,
      sender: 'user',
      timestamp: new Date(),
    };
    
    setMessages([...messages, newMessage]);
    
    // Simulate AI response
    setTimeout(() => {
      const aiResponse: Message = {
        id: (Date.now() + 1).toString(),
        content: 'I understand you want to discuss the script. How can I help?',
        sender: 'agent',
        timestamp: new Date(),
      };
      setMessages(prev => [...prev, aiResponse]);
    }, 1000);
  };

  return (
    <div className={`fixed bottom-4 right-4 transition-all ${isOpen ? 'w-96' : 'w-auto'}`}>
      {!isOpen ? (
        <Button
          onClick={() => setIsOpen(true)}
          className="rounded-full p-4 aspect-square"
        >
          <MessageSquare className="w-6 h-6" />
        </Button>
      ) : (
        <div className="bg-white rounded-lg shadow-xl">
          <div className="p-4 border-b flex justify-between items-center">
            <h3 className="font-semibold">FilmDevAgency Assistant</h3>
            <button
              onClick={() => setIsOpen(false)}
              className="text-gray-500 hover:text-gray-700"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
          <div className="h-96 p-4 overflow-y-auto">
            {messages.map((message) => (
              <ChatMessage key={message.id} message={message} />
            ))}
          </div>
          <ChatInput onSendMessage={handleSendMessage} />
        </div>
      )}
    </div>
  );
}