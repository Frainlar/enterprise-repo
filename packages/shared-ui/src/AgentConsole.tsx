import { useState } from 'react';
import { Button } from './Button';

export const AgentConsole = () => {
  const [messages, setMessages] = useState<string[]>([]);
  const [input, setInput] = useState('');

  const send = () => {
    setMessages([...messages, input]);
    setInput('');
  };

  return (
    <div className="border rounded p-4 space-y-2 bg-gray-50">
      <div className="h-40 overflow-y-auto border p-2 bg-white">
        {messages.map((m, i) => (
          <div key={i} className="mb-1">
            {m}
          </div>
        ))}
      </div>
      <div className="flex space-x-2">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="border flex-1 p-1"
          placeholder="Type a message"
        />
        <Button onClick={send}>Send</Button>
      </div>
    </div>
  );
};
