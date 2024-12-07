import React from 'react';
import { Plus, Trash2 } from 'lucide-react';
import { Scene } from '../../types/script';
import { useScriptStore } from '../../store/scriptStore';

interface SceneManagerProps {
  scenes: Scene[];
  onSceneSelect: (sceneId: string) => void;
  currentSceneId?: string;
}

export function SceneManager({ scenes, onSceneSelect, currentSceneId }: SceneManagerProps) {
  const { addScene, removeScene } = useScriptStore();

  return (
    <div className="w-64 border-r border-gray-200 p-4">
      <div className="flex justify-between items-center mb-4">
        <h2 className="font-semibold">Scenes</h2>
        <button
          onClick={() => addScene()}
          className="p-2 hover:bg-gray-100 rounded-full"
          title="Add new scene"
        >
          <Plus className="w-4 h-4" />
        </button>
      </div>
      
      <div className="space-y-2">
        {scenes.map((scene) => (
          <div
            key={scene.id}
            className={`p-3 rounded-lg cursor-pointer flex justify-between items-center ${
              currentSceneId === scene.id
                ? 'bg-purple-100 text-purple-900'
                : 'hover:bg-gray-100'
            }`}
            onClick={() => onSceneSelect(scene.id)}
          >
            <div>
              <div className="text-sm font-medium">Scene {scene.sceneNumber}</div>
              <div className="text-xs text-gray-500 truncate">{scene.heading}</div>
            </div>
            <button
              onClick={(e) => {
                e.stopPropagation();
                removeScene(scene.id);
              }}
              className="opacity-0 group-hover:opacity-100 p-1 hover:bg-gray-200 rounded"
            >
              <Trash2 className="w-4 h-4 text-gray-500" />
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}