# Quick Start Guide

## Step-by-Step Setup

### 1. Get Your Discord Bot Token

1. Visit https://discord.com/developers/applications
2. Click "New Application"
3. Name it "Spurk AI" (or whatever you prefer)
4. Go to "Bot" tab on the left
5. Click "Add Bot"
6. Click "Reset Token" and copy the token (save it somewhere safe!)
7. Enable these settings under "Privileged Gateway Intents":
   - ✅ Presence Intent
   - ✅ Server Members Intent
   - ✅ Message Content Intent

### 2. Invite Bot to Your Server

1. Go to "OAuth2" > "URL Generator"
2. Select scopes:
   - ✅ bot
3. Select bot permissions:
   - ✅ Read Messages/View Channels
   - ✅ Send Messages
   - ✅ Read Message History
   - ✅ Add Reactions
4. Copy the generated URL at the bottom
5. Paste it in your browser and select your server

### 3. Get Spurk's User ID

1. In Discord, go to Settings > Advanced
2. Enable "Developer Mode"
3. Right-click on Spurk/Oscar's username
4. Click "Copy User ID"

### 4. Configure the Bot

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and fill in:
   ```
   DISCORD_TOKEN=paste_your_bot_token_here
   SPURK_USER_ID=paste_spurk_user_id_here
   ```

### 5. Install and Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the bot
python bot.py
```

You should see:
```
SpurkAI#1234 has connected to Discord!
Monitoring user ID: 123456789
Loaded training data: {...}
```

### 6. Test It Out

In Discord, try these commands:

```
!spurk help
!spurk stats
!spurk talk
```

Or mention the bot:
```
@SpurkAI say something!
```

## Troubleshooting

**"Invalid Token" error:**
- Make sure you copied the entire token from Discord Developer Portal
- The token should have no spaces
- Try resetting the token and copying again

**Bot joins but doesn't respond:**
- Check that Message Content Intent is enabled in Discord Developer Portal
- Make sure the bot has permission to read messages in the channel
- Try `!spurk help` to test if commands work

**Bot doesn't learn from messages:**
- Verify SPURK_USER_ID is correct (should be just numbers)
- The bot needs to be in channels where Spurk talks
- Check console for "Learning from Spurk" messages

## What's Next?

- Let the bot run and collect messages from Spurk
- After 20-30 messages, try `!spurk talk` to see it in action
- Use `!spurk stats` to monitor training progress
- Mention the bot to get responses in Spurk's style

Enjoy your Spurk AI bot! 🤖
