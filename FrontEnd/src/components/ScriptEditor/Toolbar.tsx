import React from 'react';
import { Lock } from 'lucide-react';
import { ToolbarButton } from './ToolbarButton';

interface ToolbarProps {
  isLocked: boolean;
  lockedBy?: string;
}

export function Toolbar({ isLocked, lockedBy }: ToolbarProps) {
  return (
    <div className="border-b border-gray-200 p-4 flex items-center justify-between">
      <div className="flex items-center space-x-4">
        <ToolbarButton>
          <span className="font-mono">B</span>
        </ToolbarButton>
        <ToolbarButton>
          <span className="font-mono italic">I</span>
        </ToolbarButton>
        <ToolbarButton>
          <span className="font-mono underline">U</span>
        </ToolbarButton>
      </div>
      {isLocked && (
        <div className="flex items-center text-amber-500">
          <Lock className="w-4 h-4 mr-2" />
          <span className="text-sm">Locked by {lockedBy || 'another user'}</span>
        </div>
      )}
    </div>
  );
}