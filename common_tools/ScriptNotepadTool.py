from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Optional
import gradio as gr
import time

# Shared notepad
notepad_content = ""
edit_history = []
locked_by = None
lock_time = None
LOCK_TIMEOUT = 60  # Lock expires after 60 seconds

class ScriptNotepadTool(BaseTool):
    """
    A collaborative notepad tool for scriptwriter agents to create, review, and edit scripts.
    Features include editing, reviewing content, and tracking changes.
    """
    agent_id: str = Field(..., description="Unique identifier of the agent using the tool.")
    action: str = Field(..., description="Action to perform: 'view', 'edit', or 'unlock'.")
    content: Optional[str] = Field(None, description="The content to add or replace when editing.")
    replace: bool = Field(
        False, 
        description="If True, replaces the notepad's content with the provided content. Defaults to appending."
    )

    def check_lock(self):
        """Check if lock has expired"""
        global locked_by, lock_time
        if locked_by and lock_time:
            if time.time() - lock_time > LOCK_TIMEOUT:
                locked_by = None
                lock_time = None
                return True
        return False

    def run(self):
        global notepad_content, edit_history, locked_by, lock_time

        # Check for expired lock
        self.check_lock()

        if self.action == "view":
            return {
                "notepad_content": notepad_content,
                "edit_history": edit_history,
                "locked_by": locked_by
            }

        if self.action == "edit":
            if locked_by is not None and locked_by != self.agent_id:
                return f"Notepad is currently locked by Agent {locked_by}. Please wait and try again."

            # Set or refresh lock
            locked_by = self.agent_id
            lock_time = time.time()

            try:
                if self.replace:
                    old_content = notepad_content
                    notepad_content = self.content or ""
                    edit_history.append({
                        "agent_id": self.agent_id,
                        "action": "replace",
                        "old_content": old_content,
                        "new_content": notepad_content
                    })
                else:
                    notepad_content += "\n" + (self.content or "")
                    edit_history.append({
                        "agent_id": self.agent_id,
                        "action": "append",
                        "new_content": self.content or ""
                    })
                
                # Auto-unlock after successful edit
                locked_by = None
                lock_time = None
                return "Edit successful. Notepad automatically unlocked."
            
            except Exception as e:
                # Ensure unlock on error
                locked_by = None
                lock_time = None
                return f"Error during edit: {str(e)}"

        if self.action == "unlock":
            if locked_by == self.agent_id or self.check_lock():
                locked_by = None
                lock_time = None
                return "Notepad unlocked successfully."
            return f"Only Agent {locked_by} can unlock the notepad (or wait for timeout)."

        return "Invalid action. Please specify 'view', 'edit', or 'unlock'."

    @staticmethod
    def create_ui():
        """Create a Gradio interface for the notepad"""
        with gr.Blocks() as notepad_ui:
            with gr.Row():
                with gr.Column(scale=2):
                    gr.Markdown("## 📝 Script Notepad")
                    # View-only content area
                    view_area = gr.TextArea(
                        value=notepad_content,
                        label="Current Content",
                        lines=10,
                        interactive=False
                    )
                    status = gr.Markdown(f"Status: {'🔒 Locked by ' + locked_by if locked_by else '🔓 Unlocked'}")
                    
                    # User edit area
                    gr.Markdown("### ✏️ User Edit Area")
                    user_edit_area = gr.TextArea(
                        label="Enter your changes here",
                        lines=5,
                        placeholder="Type your changes here..."
                    )
                    with gr.Row():
                        append_btn = gr.Button("📝 Append")
                        replace_btn = gr.Button("🔄 Replace All")
                        unlock_btn = gr.Button("🔓 Force Unlock")
                
                with gr.Column(scale=1):
                    gr.Markdown("## 📋 Edit History")
                    history_md = gr.Markdown(format_history())
            
            refresh_btn = gr.Button("🔄 Refresh", visible=False)
            auto_refresh = gr.Number(value=time.time(), visible=False, every=5)
            
            def update_ui(timestamp):
                history_text = format_history()
                status_text = f"Status: {'🔒 Locked by ' + locked_by if locked_by else '🔓 Unlocked'}"
                return notepad_content, status_text, history_text
            
            def handle_append(text):
                global notepad_content, edit_history, locked_by
                if locked_by is not None:
                    return "Cannot edit: Notepad is locked by " + locked_by
                if text.strip():
                    notepad_content += "\n" + text
                    edit_history.append({
                        "agent_id": "User",
                        "action": "append",
                        "new_content": text
                    })
                return "Changes appended successfully"
            
            def handle_replace(text):
                global notepad_content, edit_history, locked_by
                if locked_by is not None:
                    return "Cannot edit: Notepad is locked by " + locked_by
                old_content = notepad_content
                notepad_content = text
                edit_history.append({
                    "agent_id": "User",
                    "action": "replace",
                    "old_content": old_content,
                    "new_content": text
                })
                return "Content replaced successfully"
            
            def handle_unlock():
                global locked_by
                locked_by = None
                return "Notepad forcefully unlocked"
            
            # Connect buttons to functions
            append_btn.click(
                fn=handle_append,
                inputs=[user_edit_area],
                outputs=[gr.Textbox(label="Status")]
            )
            
            replace_btn.click(
                fn=handle_replace,
                inputs=[user_edit_area],
                outputs=[gr.Textbox(label="Status")]
            )
            
            unlock_btn.click(
                fn=handle_unlock,
                outputs=[gr.Textbox(label="Status")]
            )
            
            refresh_btn.click(
                fn=update_ui,
                inputs=[auto_refresh],
                outputs=[view_area, status, history_md]
            )
            
            # Auto-refresh using Number component
            auto_refresh.change(
                fn=update_ui,
                inputs=[auto_refresh],
                outputs=[view_area, status, history_md]
            )
            
        return notepad_ui

def format_history():
    """Format edit history for display"""
    if not edit_history:
        return "No edits yet"
    
    history_text = "### Recent Changes:\n"
    for entry in reversed(edit_history[-5:]):  # Show last 5 edits
        action = entry["action"].capitalize()
        agent = entry["agent_id"]
        if action == "Replace":
            history_text += f"- 🔄 {agent} replaced content\n"
        else:
            history_text += f"- ✏️ {agent} appended content\n"
    return history_text

if __name__ == "__main__":
    # Launch UI for testing
    ui = ScriptNotepadTool.create_ui()
    ui.launch() 