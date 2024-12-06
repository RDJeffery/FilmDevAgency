from agency_swarm import Agency
import logging  # Add logging
import time

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Debug imports
logger.info("Starting to import modules...")

try:
    from CreativeDirector import CreativeDirector
    logger.info("CreativeDirector imported successfully")
    from Researcher import Researcher
    logger.info("Researcher imported successfully")
    from BrainstormingAgent import BrainstormingAgent
    logger.info("BrainstormingAgent imported successfully")
    from IdeationAgent import IdeationAgent
    logger.info("IdeationAgent imported successfully")
    from Scriptwriter1 import Scriptwriter1
    logger.info("Scriptwriter1 imported successfully")
    from Scriptwriter2 import Scriptwriter2
    logger.info("Scriptwriter2 imported successfully")
except ImportError as e:
    logger.error(f"Import error occurred: {e}")
    raise

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI API Key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

logger.info("Creating agent instances...")
creative_director = CreativeDirector('Creative Director')
researcher = Researcher('Researcher')
brainstorming_agent = BrainstormingAgent('Brainstorming Agent')
ideation_agent = IdeationAgent('Ideation Agent')
scriptwriter1 = Scriptwriter1('Scriptwriter 1')
scriptwriter2 = Scriptwriter2('Scriptwriter 2')
logger.info("All agent instances created successfully")

logger.info("Setting up agency...")
agency = Agency([
       creative_director,  # Creative Director will be the entry point for communication with the user 
       [creative_director, researcher],  # Creative Director can initiate communication with Researcher
       [researcher, creative_director],  # Researcher can initiate communication with Creative Director
       [creative_director, brainstorming_agent],  # Creative Director can initiate communication with Brainstorming Agent
       [creative_director, ideation_agent],  # Creative Director can initiate communication with Ideation Agent
       [creative_director, scriptwriter1],  # Creative Director can initiate communication with Scriptwriter 1
       [creative_director, scriptwriter2],  # Creative Director can initiate communication with Scriptwriter 2
       [researcher, brainstorming_agent],  # Researcher can initiate communication with Brainstorming Agent
       [brainstorming_agent, ideation_agent],  # Brainstorming Agent can initiate communication with Ideation Agent
       [ideation_agent, scriptwriter1],  # Ideation Agent can initiate communication with Scriptwriter 1
       [ideation_agent, scriptwriter2],  # Ideation Agent can initiate communication with Scriptwriter 2
       [scriptwriter1, scriptwriter2],  # Scriptwriter 1 can initiate communication with Scriptwriter 2
       [scriptwriter2, researcher],  # Scriptwriter 2 can initiate communication with Researcher
       [scriptwriter1, researcher],  # Scriptwriter 1 can initiate communication with Researcher
       [scriptwriter1, creative_director],  # Scriptwriter 1 can initiate communication with Creative Director
     ],
     shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
     temperature=0.3,  # default temperature for all agents
     max_prompt_tokens=25000,  # reduced max tokens to prevent rate limit issues
)
logger.info("Agency setup completed")

if __name__ == '__main__':
    logger.info("Starting Gradio demo...")
    agency.demo_gradio()
