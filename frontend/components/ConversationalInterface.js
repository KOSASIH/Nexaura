import React, { useState, useEffect } from 'react';
import { ChatBot } from 'react-chatbot-kit';
import { Message } from './Message';

const ConversationalInterface = () => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');

  useEffect(() => {
    fetch('/api/conversations')
      .then(response => response.json())
      .then(data => setMessages(data));
  }, []);

  const handleSendMessage = () => {
    const message = {
      text: inputValue,
      sender: 'user',
    };
    setMessages([...messages, message]);
    setInputValue('');
    fetch('/api/conversations', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(message),
    });
  };

  return (
    <ChatBot
      headerTitle="Conversational Interface"
      placeholder="Type a message..."
      handleSendMessage={handleSendMessage}
      messages={messages}
      MessageComponent={Message}
    />
  );
};

export default ConversationalInterface;
