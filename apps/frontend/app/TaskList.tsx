'use client';
import { useEffect, useState } from 'react';
import { getTaskListContainer } from '@enterprise/realtime';

export default function TaskList() {
  const [tasks, setTasks] = useState<string[]>([]);
  const [input, setInput] = useState('');

  useEffect(() => {
    let map: any;
    getTaskListContainer('tasks').then(({ tasks: sharedMap }) => {
      map = sharedMap;
      const update = () => setTasks(Array.from(sharedMap.values()));
      sharedMap.on('valueChanged', update);
      update();
    });
    return () => {
      if (map) map.off('valueChanged');
    };
  }, []);

  const addTask = () => {
    getTaskListContainer('tasks').then(({ tasks: sharedMap }) => {
      sharedMap.set(Date.now().toString(), input);
      setInput('');
    });
  };

  return (
    <div>
      <div className="flex space-x-2 mt-4">
        <input
          className="border p-1"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Add task"
        />
        <button className="px-2 py-1 bg-blue-500 text-white" onClick={addTask}>Add</button>
      </div>
      <ul className="list-disc pl-5 mt-2">
        {tasks.map((t, i) => (
          <li key={i}>{t}</li>
        ))}
      </ul>
    </div>
  );
}
