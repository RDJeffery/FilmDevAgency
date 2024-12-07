import React from 'react';
import { useScriptStore } from '../../store/scriptStore';

interface FormattingOption {
  label: string;
  style: string;
  shortcut?: string;
}

const FORMATTING_OPTIONS: FormattingOption[] = [
  { label: 'Scene Heading', style: 'scene-heading', shortcut: 'Alt+H' },
  { label: 'Action', style: 'action', shortcut: 'Alt+A' },
  { label: 'Character', style: 'character', shortcut: 'Alt+C' },
  { label: 'Dialogue', style: 'dialogue', shortcut: 'Alt+D' },
  { label: 'Parenthetical', style: 'parenthetical', shortcut: 'Alt+P' },
  { label: 'Transition', style: 'transition', shortcut: 'Alt+T' },
];

export function ScriptFormatting() {
  const { currentScript, updateFormatting } = useScriptStore();

  const applyFormatting = (style: string) => {
    if (!currentScript) return;
    
    // Get selected text and apply formatting
    const selection = window.getSelection();
    if (!selection || selection.rangeCount === 0) return;
    
    const range = selection.getRangeAt(0);
    const selectedText = range.toString();
    
    if (selectedText) {
      updateFormatting(style, range);
    }
  };

  return (
    <div className="flex flex-col space-y-2 p-4 border-r border-gray-200">
      {FORMATTING_OPTIONS.map((option) => (
        <button
          key={option.style}
          onClick={() => applyFormatting(option.style)}
          className="text-left px-4 py-2 hover:bg-gray-100 rounded-lg transition-colors"
        >
          <div className="text-sm font-medium">{option.label}</div>
          {option.shortcut && (
            <div className="text-xs text-gray-500">{option.shortcut}</div>
          )}
        </button>
      ))}
    </div>
  );
}