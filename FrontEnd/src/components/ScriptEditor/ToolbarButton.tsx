import React from 'react';

interface ToolbarButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
}

export function ToolbarButton({ children, onClick }: ToolbarButtonProps) {
  return (
    <button 
      onClick={onClick}
      className="p-2 hover:bg-gray-100 rounded transition-colors"
    >
      {children}
    </button>
  );
}