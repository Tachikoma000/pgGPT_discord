# pgGPT Discord Bot

pgGPT Discord Bot is an advanced Discord bot that enhances the functionality and interaction within your Discord server. It uses the Playgrounds GraphQL API to fetch data from decentralized subgraphs, allowing for direct querying from the Discord interface. It also allows for creating and managing conversation threads, providing a handy way to keep discussions organized and on-topic.

## Features

- **Hello Command**: Start a new conversation thread with the bot by using the `/hello` command.
- **Subgraph Query Command**: The bot uses the `/query_subgraph` command to fetch data from a subgraph. This powerful command guides users through the process of obtaining an API key, selecting a subgraph, and running a query. The results are delivered conveniently in a CSV file.
- **Help Command**: Use the `/help` command to see a list of all commands and their descriptions.
- **Rate Limiting**: To prevent spam and abuse of bot commands, rate limiting is implemented. This ensures a seamless experience for all users.

## Detailed Workflow of Subgraph Query Command

1. **Starting the Query**: When a user runs the `/query_subgraph` command, the bot creates a new thread and sends an initial message explaining the process. It then sends a direct message to the user asking for their Playgrounds API key.

2. **Obtaining the API Key**: The user replies to the direct message with their API key. The bot confirms receipt of the key and uses it to fetch a list of entities from the specified subgraph.

3. **Querying an Entity**: The bot returns the list of entities to the user, who then sends the name of the entity they wish to query. The bot runs the query and saves the result in a CSV file.

4. **Returning the Results**: The bot sends the CSV file with the query result to the user in the thread. The file is then deleted from the bot's storage for security and space efficiency.

## Setup

1. Clone the repository and navigate to the root directory.
2. Create a Python virtual environment and activate it.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Set up your bot token as an environment variable.
5. Run `python main.py` to start the bot.

## Usage

To use the bot in your Discord server:

1. Invite the bot to your server.
2. Run `/hello` to create a new thread for conversation.
3. Run `/query_subgraph` to query a subgraph and return the result in a new thread. The bot will guide you through the process.
4. Run `/help` to see a list of all commands and their descriptions.

## Contributing

Contributions are welcome. Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the terms of the MIT license.

## Contact

For any questions or concerns, please raise an issue in the GitHub repository.
