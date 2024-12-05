from agency_swarm.agents import Agent


class Researcher(Agent):
    def __init__(self, name="Researcher"):
        super().__init__(
            name=name,
            description="The Researcher agent conducts research on given topics and assists other team members by providing information. It uses the Tavily AI API for web search and follows a specific thought pattern.",
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
