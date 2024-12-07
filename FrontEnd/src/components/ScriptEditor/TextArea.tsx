import React from 'react';

interface TextAreaProps {
  content: string;
  isLocked: boolean;
  onChange: (content: string) => void;
}

export function TextArea({ content, isLocked, onChange }: TextAreaProps) {
  return (
    <div className="p-4">
      <textarea
        className="w-full h-[calc(100vh-12rem)] font-mono text-base leading-relaxed resize-none focus:outline-none"
        value={content}
        onChange={(e) => onChange(e.target.value)}
        disabled={isLocked}
        style={{ fontFamily: 'Courier New' }}
        placeholder="INT. COFFEE SHOP - DAY"
      />
    </div>
  );
}