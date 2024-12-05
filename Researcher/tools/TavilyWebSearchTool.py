from agency_swarm.tools import BaseTool
from pydantic import Field
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variables
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')

class TavilyWebSearchTool(BaseTool):
    """
    TavilyWebSearchTool integrates with the Tavily AI API to perform web searches.
    It accepts a query string as input and returns the search results in a structured format.
    The tool handles authentication and error handling related to the Tavily AI API.
    """

    query: str = Field(
        ..., description="The search query string to be sent to the Tavily AI API."
    )

    def run(self):
        """
        Sends a search query to the Tavily AI API and processes the response to extract relevant information.
        Handles any exceptions or errors that may occur during the API call.
        """
        api_endpoint = "https://api.tavily.com/search"
        
        # Only include API key in the payload as per REST API docs
        payload = {
            "api_key": TAVILY_API_KEY,
            "query": self.query,
            "search_depth": "advanced",
            "include_answer": True
        }

        try:
            # Make the API request
            response = requests.post(api_endpoint, json=payload, timeout=30)
            
            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()
                return data  # Return the complete response from Tavily
            else:
                error_message = f"Error: API returned status code {response.status_code}"
                if response.text:
                    try:
                        error_data = response.json()
                        error_message += f" - {error_data.get('message', '')}"
                    except:
                        error_message += f" - {response.text}"
                return error_message

        except requests.exceptions.Timeout:
            return "Search request timed out. Please try again."
        except requests.exceptions.RequestException as e:
            return f"An error occurred during the search: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"