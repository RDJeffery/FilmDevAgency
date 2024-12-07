import React, { useEffect } from 'react';
import { SceneManager } from './SceneManager';
import { ScriptFormatting } from './ScriptFormatting';
import { Toolbar } from './Toolbar';
import { TextArea } from './TextArea';
import { useScriptStore } from '../../store/scriptStore';

export function ScriptEditor() {
  const {
    currentScript,
    isLocked,
    lockedBy,
    currentScene,
    updateContent,
    setCurrentScene,
  } = useScriptStore();

  useEffect(() => {
    // Initialize with first scene if none selected
    if (currentScript?.scenes.length && !currentScene) {
      setCurrentScene(currentScript.scenes[0]);
    }
  }, [currentScript, currentScene, setCurrentScene]);

  return (
    <div className="flex h-full">
      <SceneManager
        scenes={currentScript?.scenes || []}
        onSceneSelect={(sceneId) => {
          const scene = currentScript?.scenes.find((s) => s.id === sceneId);
          if (scene) setCurrentScene(scene);
        }}
        currentSceneId={currentScene?.id}
      />
      
      <ScriptFormatting />
      
      <div className="flex-1 flex flex-col">
        <Toolbar isLocked={isLocked} lockedBy={lockedBy} />
        <TextArea
          content={currentScene?.content || ''}
          isLocked={isLocked}
          onChange={(content) => {
            if (currentScene) {
              updateContent(content);
            }
          }}
        />
      </div>
    </div>
  );
}