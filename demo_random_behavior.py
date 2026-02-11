"""
Demo script to demonstrate the new random behavior features.
This simulates how the bot will behave with random replies and random messages.
"""
import random
import sys

try:
    from spurk_ai import SpurkAI
except ImportError:
    print("Error: Could not import spurk_ai module.")
    print("Make sure spurk_ai.py is in the same directory as this script.")
    sys.exit(1)

def demo_random_behavior():
    """Demonstrate random reply and random message behavior."""
    print("=" * 70)
    print("Spurk AI - Random Behavior Demo")
    print("=" * 70)
    print()
    
    # Initialize the AI with some training data
    ai = SpurkAI(data_file="demo_data.json")
    
    # Train with some sample messages
    print("📚 Training the AI with sample messages...\n")
    training_messages = [
        "Hey everyone, how's it going?",
        "I love working on Discord bots",
        "Python is such a great language",
        "Let's build something cool today",
        "What do you all think about this?",
        "That's a really good idea",
        "I'm excited about this project",
        "This is going to be awesome",
        "Anyone want to collaborate?",
        "I'll work on that feature next"
    ]
    
    for msg in training_messages:
        ai.learn_from_message(msg)
        print(f"  Learned: {msg}")
    
    print(f"\n✅ Training complete! Stats: {ai.get_stats()}\n")
    
    # Demo 1: Random replies
    print("-" * 70)
    print("Demo 1: Random Reply Behavior (5% chance)")
    print("-" * 70)
    print()
    print("Simulating 20 messages in a channel...\n")
    
    RANDOM_REPLY_CHANCE = 0.05
    incoming_messages = [
        "Hey, what's up?",
        "Did anyone see the game last night?",
        "I'm thinking about learning Python",
        "The weather is nice today",
        "What should we do for lunch?",
        "This project is coming along well",
        "Has anyone used Discord.py before?",
        "I need help with my code",
        "Great job on that feature!",
        "Who wants to join the voice chat?",
        "I'm working on a new project",
        "Does anyone know JavaScript?",
        "Let's have a meeting tomorrow",
        "I fixed that bug finally",
        "The documentation is really helpful",
        "Anyone free this weekend?",
        "I love this community",
        "Thanks for all the help",
        "See you all later!",
        "Good morning everyone"
    ]
    
    random.seed(42)  # For reproducible demo
    for i, msg in enumerate(incoming_messages, 1):
        print(f"{i}. User: {msg}")
        
        # Simulate random reply logic
        if random.random() < RANDOM_REPLY_CHANCE:
            response = ai.generate_response(msg)
            print(f"   🤖 Bot replies: {response}")
        print()
    
    # Demo 2: Random messages
    print("-" * 70)
    print("Demo 2: Random Message Sending (every 10 minutes)")
    print("-" * 70)
    print()
    print("Simulating periodic random messages...\n")
    
    for i in range(1, 4):
        print(f"⏰ After {i * 10} minutes:")
        response = ai.generate_response()
        print(f"   🤖 Bot says: {response}\n")
    
    print("=" * 70)
    print("Demo Complete!")
    print("=" * 70)
    print()
    print("💡 Configuration Options:")
    print("   • RANDOM_REPLY_CHANCE: Adjust the probability of random replies (0.0-1.0)")
    print("   • RANDOM_MESSAGE_INTERVAL: Change how often random messages are sent (seconds)")
    print()
    
    # Cleanup
    import os
    if os.path.exists("demo_data.json"):
        os.remove("demo_data.json")

if __name__ == '__main__':
    demo_random_behavior()
