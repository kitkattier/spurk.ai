# spurk.ai

A Discord chatbot that learns from Spurk (Oscar) in real-time and mimics their communication style. The bot monitors messages from a specified user and trains itself to generate responses that sound like them.

## Features

- **Real-time Learning**: Automatically learns from Spurk's messages as they chat
- **AI Response Generation**: Generates responses in Spurk's style using learned patterns
- **Random Message Sending**: Bot randomly sends messages to active channels like a real person
- **Random Replies**: Bot randomly replies to messages in conversations, not just when mentioned
- **Multiple Generation Strategies**: Uses common phrases, word pair patterns (Markov chains), and random message selection
- **Discord Integration**: Works as a Discord bot with commands and mention responses
- **Persistent Storage**: Saves training data to JSON file for continuity across restarts

## How It Works

The bot uses several techniques to learn and mimic Spurk's style:

1. **Message Collection**: Stores the last 1000 messages from Spurk
2. **Word Pair Analysis**: Builds word pair relationships for Markov chain-like text generation
3. **Phrase Extraction**: Identifies and stores common phrases (3-10 words)
4. **Response Generation**: Combines these techniques to generate natural-sounding responses

## Setup

### Prerequisites

- Python 3.8 or higher
- A Discord account
- A Discord bot token (see below)

### Creating a Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name (e.g., "Spurk AI")
3. Go to the "Bot" section and click "Add Bot"
4. Under the bot's token section, click "Copy" to copy your bot token
5. Enable these Privileged Gateway Intents:
   - Message Content Intent
   - Server Members Intent
6. Go to OAuth2 > URL Generator
7. Select scopes: `bot`
8. Select bot permissions: `Send Messages`, `Read Message History`, `Read Messages/View Channels`
9. Copy the generated URL and open it to invite the bot to your server

### Installation

1. Clone the repository:
```bash
git clone https://github.com/kitkattier/spurk.ai.git
cd spurk.ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file from the example:
```bash
cp .env.example .env
```

4. Edit `.env` and add your configuration:
```env
DISCORD_TOKEN=your_bot_token_here
SPURK_USER_ID=user_id_to_learn_from
RANDOM_REPLY_CHANCE=0.05
RANDOM_MESSAGE_INTERVAL=600
```

Configuration options:
- `DISCORD_TOKEN`: Your Discord bot token
- `SPURK_USER_ID`: The Discord user ID to learn from
- `RANDOM_REPLY_CHANCE`: Probability (0.0-1.0) that the bot will reply to a random message (default: 0.05 = 5%)
- `RANDOM_MESSAGE_INTERVAL`: Interval in seconds for sending random messages (default: 600 = 10 minutes, set to 0 to disable)

To find a user's Discord ID:
- Enable Developer Mode in Discord (Settings > Advanced > Developer Mode)
- Right-click on the user and select "Copy User ID"

### Running the Bot

```bash
python bot.py
```

The bot will start and connect to Discord. It will begin learning from Spurk's messages automatically.

## Usage

### Commands

- **!spurk talk** - Generate a random message in Spurk's style
- **!spurk stats** - Show statistics about training data
- **!spurk help** - Show help information

### Automatic Learning

The bot automatically learns from messages sent by the specified user (Spurk/Oscar). No action needed!

### Random Behavior

The bot now acts more like a real person:
- **Random Replies**: The bot will randomly reply to messages in conversations (5% chance by default)
- **Random Messages**: The bot will periodically send messages to active channels (every 10 minutes by default)
- Both behaviors can be configured in the `.env` file

### Getting Responses

Mention the bot in any message to get a response in Spurk's style:
```
@SpurkAI what do you think?
```

## Data Storage

Training data is stored in `spurk_data.json` in the same directory as the bot. This file contains:
- Recent messages (last 1000)
- Word pair relationships
- Common phrases

The file is automatically created and updated as the bot learns.

## Limitations

- The bot needs at least 5 messages before it can generate responses
- Response quality improves with more training data
- The AI is relatively simple - it uses pattern matching and Markov chains, not advanced language models
- Maximum 1000 messages stored to keep data file manageable

## Future Improvements

Potential enhancements:
- Integration with OpenAI GPT for more sophisticated responses
- Sentiment analysis to match Spurk's mood
- Context awareness for more relevant responses
- Web interface for monitoring training progress
- Multiple personality profiles

## Troubleshooting

**Bot doesn't start:**
- Check that your `DISCORD_TOKEN` is correct in `.env`
- Ensure you've installed all requirements: `pip install -r requirements.txt`

**Bot doesn't learn:**
- Verify `SPURK_USER_ID` is set correctly in `.env`
- Make sure the bot has permission to read messages in channels where Spurk talks
- Check the console output for "Learning from Spurk" messages

**Bot gives poor responses:**
- The bot needs more training data (at least 20-30 messages for decent results)
- Keep the bot running while Spurk/Oscar chats to collect more data

## License

MIT

## Contributing

Contributions welcome! Feel free to open issues or pull requests.
