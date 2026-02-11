# Architecture Overview

## System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                         Discord Server                        │
│                                                               │
│  ┌──────────────┐                    ┌────────────────┐     │
│  │ Spurk/Oscar  │ ─────messages────> │   SpurkAI Bot  │     │
│  │  (Real User) │                    │                │     │
│  └──────────────┘                    │  - Learns      │     │
│                                      │  - Responds    │     │
│  ┌──────────────┐                    │  - Commands    │     │
│  │ Other Users  │ <──responses────── │                │     │
│  └──────────────┘                    └────────────────┘     │
│                                              │               │
└──────────────────────────────────────────────┼───────────────┘
                                               │
                                               ▼
                                      ┌─────────────────┐
                                      │  spurk_data.json│
                                      │                 │
                                      │  - Messages     │
                                      │  - Word Pairs   │
                                      │  - Phrases      │
                                      └─────────────────┘
```

## Component Breakdown

### 1. bot.py (Discord Integration)
- Connects to Discord using discord.py
- Event handlers:
  - `on_ready`: Bot startup
  - `on_message`: Message monitoring and learning
- Commands:
  - `!spurk talk`: Generate random response
  - `!spurk stats`: Show training data statistics
  - `!spurk help`: Display help information
- Mention detection: Responds when @mentioned

### 2. spurk_ai.py (AI Engine)
- **Learning Module**:
  - Stores messages (max 1000)
  - Builds word pair relationships (Markov chains)
  - Extracts common phrases (3-10 words)
  
- **Generation Module**:
  - Strategy 1: Use common phrases (50% chance)
  - Strategy 2: Generate using word pairs (70% chance)
  - Strategy 3: Return random message (fallback)

- **Persistence**:
  - JSON file storage
  - Auto-save on learning
  - Auto-load on startup

### 3. Data Flow

```
1. Spurk sends message in Discord
        ↓
2. Bot detects message from SPURK_USER_ID
        ↓
3. SpurkAI.learn_from_message()
   - Store message
   - Extract word pairs
   - Find phrases
   - Save to JSON
        ↓
4. User mentions bot or uses command
        ↓
5. SpurkAI.generate_response()
   - Choose strategy
   - Generate text
   - Return response
        ↓
6. Bot sends response to Discord
```

## AI Generation Strategies

### Strategy 1: Common Phrases (50%)
Returns a stored phrase that Spurk commonly uses.
- **Pros**: Authentic, exactly what Spurk would say
- **Cons**: Limited variety, needs good training data

### Strategy 2: Word Pair Generation (70%)
Builds sentences using learned word relationships.
- **Pros**: Creates new combinations, more variety
- **Cons**: Can be nonsensical, needs context

### Strategy 3: Random Message (Fallback)
Returns a random stored message.
- **Pros**: Always authentic
- **Cons**: May not fit context

## Training Process

### Initial Phase (0-10 messages)
- Bot collects basic data
- Limited word pairs
- Few common phrases
- Responses: "I'm still learning..."

### Learning Phase (10-50 messages)
- Building word relationships
- Identifying patterns
- Responses becoming more varied

### Mature Phase (50+ messages)
- Rich vocabulary
- Good phrase library
- Natural-sounding responses

## File Structure

```
spurk.ai/
├── bot.py                 # Main Discord bot
├── spurk_ai.py           # AI learning/generation engine
├── requirements.txt       # Python dependencies
├── .env.example          # Environment template
├── .env                  # Environment config (gitignored)
├── .gitignore            # Git ignore rules
├── README.md             # Full documentation
├── QUICKSTART.md         # Setup guide
├── demo.py               # Standalone demo
├── test_spurk_ai.py      # Unit tests
└── spurk_data.json       # Training data (gitignored)
```

## Security Considerations

✅ **Implemented:**
- Environment variables for sensitive data
- .gitignore for secrets and data files
- No hardcoded tokens or IDs
- CodeQL security scanning passed

✅ **Best Practices:**
- Token in .env file only
- User ID configurable
- Data files excluded from repo
- Safe JSON handling with error checking

## Scalability

### Current Limits:
- 1000 stored messages (prevents file bloat)
- 100 common phrases (keeps quality high)
- Single user learning (focused training)

### Future Improvements:
- Multi-user support with weights
- Advanced NLP (sentiment analysis)
- Context-aware responses
- Machine learning models (GPT integration)
- Database storage (PostgreSQL/MongoDB)
- Web dashboard for monitoring

## Testing

### Automated Tests (test_spurk_ai.py):
- ✓ Initial state verification
- ✓ Message learning
- ✓ Response generation
- ✓ Data persistence
- ✓ Message limit enforcement

### Manual Testing (demo.py):
- Simulates real-world usage
- Shows learning progression
- Demonstrates response quality

### Integration Testing:
- Run bot with real Discord server
- Monitor learning from real user
- Test commands and mentions
- Verify data persistence

## Monitoring

Check bot health via:
- Console output: "Learning from Spurk" messages
- `!spurk stats` command in Discord
- Review `spurk_data.json` file
- Bot status in Discord (online/offline)

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Bot offline | Invalid token | Check .env file |
| Not learning | Wrong user ID | Verify SPURK_USER_ID |
| Poor responses | Insufficient data | Collect more messages |
| No responses | Missing intents | Enable Message Content Intent |
