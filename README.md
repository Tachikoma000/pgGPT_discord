# pgGPT_Discord Bot

The pgGPT Discord Bot is a multi-faceted integration designed for Discord servers. With a primary focus on leveraging the capabilities of the Playgrounds GraphQL API, this bot aims to provide a seamless interface for querying decentralized subgraphs directly within Discord. Further enhancing its capabilities is the integration of a sophisticated AI language model, enabling intelligent interactions and in-depth assistance for `Subgrounds`.

---

## 📌 Table of Contents:
- [pgGPT\_Discord Bot](#pggpt_discord-bot)
  - [📌 Table of Contents:](#-table-of-contents)
  - [1. 🏗 System Architecture:](#1--system-architecture)
    - [Key Components:](#key-components)
  - [2. 🚀 Features \& Workflows:](#2--features--workflows)
    - [AI Conversations:](#ai-conversations)
    - [Subgraph Query Workflow:](#subgraph-query-workflow)
  - [3. 📜 Codebase Overview:](#3--codebase-overview)
  - [4. 🔧 Setup \& Installation:](#4--setup--installation)
  - [5. 💡 Usage \& Commands:](#5--usage--commands)
  - [6. 🤝 Contributing:](#6--contributing)
  - [7. 📄 License \& Contact:](#7--license--contact)

---

## 1. 🏗 System Architecture:

![Alt text](assets/pgGPT_diagram.png)

```plaintext
+------------------------+
|    Discord Server      |
|                        |
|  +------------------+  |
|  |    pgGPT Bot     |<--------- GraphQL Queries ----------> [Playgrounds GraphQL API]
|  +------------------+  |
|           |             |
|           | API Key     |
|           |             |
+-----------v-------------+
            |
            v
+------------------------+
| User's DM Channel      |
+------------------------+
```

### Key Components:
- **Discord Server**: The primary environment where the bot operates.
- **pgGPT Bot**: Our main bot module, responsible for processing commands and interactions.
- **Playgrounds GraphQL API**: External GraphQL API for querying decentralized subgraphs.
- **User's DM Channel**: Private channel for sensitive interactions like API key collection.

## 2. 🚀 Features & Workflows:

### AI Conversations:
1. **Command Initiation**: Users trigger the AI by using the `/ask_ai` command.
2. **AI Backend Processing**: Utilizing a combination of retrieval and generative methods, the bot fetches or constructs responses based on the provided `Subgrounds` document.
3. **Response Delivery**: The AI's response is presented to the user in a structured embed format.

### Subgraph Query Workflow:
1. **Command Start**: Users initiate with the `/query_subgraph` command.
2. **API Key Collection**: A DM is sent to the user to gather their Playgrounds API key securely.
3. **Entity Listing**: Post key retrieval, the bot fetches and displays available entities from the specified subgraph.
4. **Entity Querying**: Users select an entity. The bot performs the query and generates the results.
5. **Result Presentation**: Query results are presented to users in a downloadable CSV format.

## 3. 📜 Codebase Overview:
- **main.py**: Entry point of the bot. Handles command registration, Discord events, and utility functions.
- **pgai_v2.py**: Contains the AI's backend logic, integrating OpenAI language models and the retrieval mechanism.
- **graphql_handler.py**: Responsible for GraphQL interactions, schema introspections, and query executions.

## 4. 🔧 Setup & Installation:
1. **Repository Setup**: Clone the repository.
2. **Environment Prep**: Activate a Python virtual environment.
3. **Dependency Management**: Use `pip install -r requirements.txt`.
4. **Environment Variables**: Configure necessary environment variables (e.g., bot token, OpenAI API key).
5. **Starting the Bot**: Execute `python main.py`.

## 5. 💡 Usage & Commands:
- **Bot Onboarding**: Invite the bot to your Discord server.
- **Hello Command**: Begin a conversation using `/hello`.
- **Subgraph Queries**: Use `/query_subgraph` to start a query process.
- **AI Interactions**: Engage with the AI via `/ask_ai` followed by a question.
- **Help**: Unsure about commands? Just type `/help`.

## 6. 🤝 Contributing:
Developers are encouraged to contribute. Start by forking the repository and then submit your pull requests. Ensure that you follow code style guidelines and provide adequate documentation.

## 7. 📄 License & Contact:
- **License**: MIT license.
- **Contact**: For questions or technical issues, open an issue on our GitHub repository.


