from agency_swarm.agents import Agent


class BrainstormingAgent(Agent):
    def __init__(self, name="Brainstorming Agent"):
        super().__init__(
            name=name,
            description="The Brainstorming Agent collaborates with the Researcher to generate story ideas and communicates with the Creative Director, Researcher, and Ideation Agent to ensure the development of innovative story concepts.",
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
