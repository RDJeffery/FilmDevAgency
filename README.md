# 🎬 FilmDevAgency - AI-Powered Film Development Suite

An innovative AI-powered film development agency that streamlines the creative process in film and television development using a team of specialized AI agents. Built using the powerful [Agency Swarm](https://github.com/VRSEN/agency-swarm) framework.

## 🙏 Acknowledgments

This project is powered by the incredible [Agency Swarm](https://github.com/VRSEN/agency-swarm) framework. Special thanks to the Agency Swarm development team for creating such a powerful and flexible framework for building multi-agent AI systems.

## 🤖 Meet the Team

- **👨‍💼 Creative Director**: The visionary leader coordinating all aspects of the creative process
- **🔍 Researcher**: Gathers real-time information and trends using Tavily AI
- **🧠 Brainstorming Agent**: Generates innovative story concepts
- **💡 Ideation Agent**: Refines and elevates story ideas
- **✍️ Scriptwriter 1**: Specializes in dark humor and analytical storytelling
- **📝 Scriptwriter 2**: Focuses on emotional depth and human experiences

## 🔄 Workflow

1. Creative Director oversees the entire process and manages communication
2. Researcher gathers relevant information and industry insights
3. Brainstorming Agent generates initial story concepts
4. Ideation Agent refines and enhances the ideas
5. Both Scriptwriters develop scripts with their unique perspectives
6. All agents collaborate and iterate to create compelling narratives

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/FilmDevAgency.git
cd FilmDevAgency
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\\Scripts\\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your environment variables:
   - Create a `.env` file in the root directory
   - Add your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### 🎯 Running the Application

Launch the application with:
```bash
python agency.py
```

This will start the Gradio interface where you can interact with the agency.

## 🔧 Troubleshooting

### Common Issues and Solutions

1. **API Rate Limits**
   - Error: "OpenAI API rate limit exceeded"
   - Solution: Reduce the frequency of requests or upgrade your API plan

2. **Token Limits**
   - Error: "Request too large for gpt-3.5-turbo"
   - Solution: The conversation history is too long. Start a new session

3. **Tavily API Connection Issues**
   - Error: "Failed to resolve 'api.tavily.com'"
   - Solution: Check your internet connection and verify your Tavily API key

4. **Import Errors**
   - Error: "ModuleNotFoundError"
   - Solution: Ensure you're in the virtual environment and all dependencies are installed

### 🪖 Work in Progress

1. Notebook that the team of agents can share and use to collaborate
2. A way to save files and documents the agents create


### 📋 Best Practices

1. Always use a virtual environment
2. Keep your API keys secure and never commit them to version control
3. Monitor your API usage to avoid hitting rate limits
4. Regularly update your dependencies

## 🔒 Security Notes

- Never commit your `.env` file
- Keep your API keys confidential
- Regularly rotate your API keys
- Add `.env` and `__pycache__` to your `.gitignore`

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
