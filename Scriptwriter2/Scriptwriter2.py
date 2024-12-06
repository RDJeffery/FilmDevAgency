from agency_swarm.agents import Agent
from common_tools.ScriptNotepadTool import ScriptNotepadTool


class Scriptwriter2(Agent):
    def __init__(self, name="Scriptwriter 2"):
        super().__init__(
            name=name,
            description="The second Scriptwriter agent writes scripts with a specific emotional perspective or bias. It communicates with the Creative Director and Ideation Agent to ensure the scripts align with the agency's vision.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[ScriptNotepadTool],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )

    def response_validator(self, message):
        return message
