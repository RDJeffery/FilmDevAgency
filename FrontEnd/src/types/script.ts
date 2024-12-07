export interface Script {
  id: string;
  title: string;
  content: string;
  lockedBy?: string;
  lastModified: Date;
  scenes: Scene[];
}

export interface Scene {
  id: string;
  sceneNumber: number;
  heading: string;
  content: string;
  lockedBy?: string;
}