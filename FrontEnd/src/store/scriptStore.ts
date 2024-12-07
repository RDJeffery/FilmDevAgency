import { create } from 'zustand';
import * as Y from 'yjs';
import { WebsocketProvider } from 'y-websocket';
import { Script, Scene } from '../types/script';

interface ScriptState {
  currentScript: Script | null;
  isLocked: boolean;
  lockedBy: string | undefined;
  currentScene: Scene | null;
  yDoc: Y.Doc;
  awareness: WebsocketProvider | null;
  
  setScript: (script: Script) => void;
  updateContent: (content: string) => void;
  lockScript: (userId: string) => void;
  unlockScript: () => void;
  addScene: () => void;
  removeScene: (sceneId: string) => void;
  setCurrentScene: (scene: Scene) => void;
  updateFormatting: (style: string, range: Range) => void;
}

const yDoc = new Y.Doc();

export const useScriptStore = create<ScriptState>((set, get) => ({
  currentScript: null,
  isLocked: false,
  lockedBy: undefined,
  currentScene: null,
  yDoc,
  awareness: null,
  
  setScript: (script) => set({ currentScript: script }),
  
  updateContent: (content) => {
    const { currentScript, yDoc } = get();
    if (!currentScript) return;
    
    const yText = yDoc.getText('script');
    yText.delete(0, yText.length);
    yText.insert(0, content);
    
    set((state) => ({
      currentScript: { ...state.currentScript!, content }
    }));
  },
  
  lockScript: (userId) => set({ isLocked: true, lockedBy: userId }),
  unlockScript: () => set({ isLocked: false, lockedBy: undefined }),
  
  addScene: () => {
    const { currentScript } = get();
    if (!currentScript) return;
    
    const newScene: Scene = {
      id: crypto.randomUUID(),
      sceneNumber: currentScript.scenes.length + 1,
      heading: 'New Scene',
      content: '',
    };
    
    set((state) => ({
      currentScript: {
        ...state.currentScript!,
        scenes: [...state.currentScript!.scenes, newScene],
      },
    }));
  },
  
  removeScene: (sceneId) => {
    set((state) => ({
      currentScript: state.currentScript
        ? {
            ...state.currentScript,
            scenes: state.currentScript.scenes.filter(
              (scene) => scene.id !== sceneId
            ),
          }
        : null,
    }));
  },
  
  setCurrentScene: (scene) => set({ currentScene: scene }),
  
  updateFormatting: (style, range) => {
    // Implementation for formatting updates
  },
}));