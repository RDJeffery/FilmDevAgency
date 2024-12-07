import React from 'react';
import { ScriptEditor } from './components/ScriptEditor';
import { ChatBar } from './components/ChatBar';
import { FileText } from 'lucide-react';

function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-gray-900 text-white">
        <div className="container mx-auto px-4">
          <div className="h-16 flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <FileText className="w-6 h-6" />
              <h1 className="text-xl font-semibold">Script Project</h1>
            </div>
            <button className="bg-purple-600 px-4 py-2 rounded-lg hover:bg-purple-700">
              Share
            </button>
          </div>
        </div>
      </header>

      <main className="container mx-auto px-4 py-8">
        <div className="bg-white rounded-lg shadow-lg min-h-[calc(100vh-8rem)]">
          <ScriptEditor
            content=""
            isLocked={false}
            onContentChange={() => {}}
          />
        </div>
      </main>

      <ChatBar />
    </div>
  );
}

export default App;