from agency_swarm.agents import Agent


class IdeationAgent(Agent):
    def __init__(self, name="Ideation Agent"):
        super().__init__(
            name=name,
            description="The Ideation Agent works with the Brainstorming Agent to elevate story ideas and ensure they align with the unified vision. It communicates with the Creative Director, Brainstorming Agent, and Scriptwriters.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )

    def response_validator(self, message):
        return message
