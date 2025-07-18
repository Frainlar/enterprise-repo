import TaskList from './TaskList';

export default function Home() {
  return (
    <main className="p-8">
      <h1 className="text-2xl font-bold">Welcome to the Enterprise Platform</h1>
      <TaskList />
    </main>
  );
}
