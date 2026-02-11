#!/usr/bin/env python3
"""
Demo script to show SpurkAI in action without Discord.
This simulates learning and response generation.
"""
from spurk_ai import SpurkAI
import time

def demo():
    """Run a demo of the SpurkAI."""
    print("=" * 60)
    print("Spurk AI Demo - Learning and Response Generation")
    print("=" * 60)
    print()
    
    # Create AI instance
    ai = SpurkAI(data_file="demo_spurk_data.json")
    
    # Sample messages that Spurk might say
    sample_messages = [
        "hey everyone what's up",
        "just finished coding this awesome feature",
        "python is literally the best",
        "who wants to play some games later",
        "lol that's hilarious",
        "I'm working on a new project",
        "check out this cool thing I made",
        "discord bots are so fun to build",
        "anyone down for some valorant",
        "brb getting some food",
        "that's actually pretty cool",
        "yeah I agree with that",
        "let's do it",
        "sounds good to me",
        "nice work on that",
        "I'm thinking we should try something new",
        "what do you all think about this idea",
        "honestly that makes a lot of sense",
        "lmao no way",
        "that's what I was thinking too"
    ]
    
    # Simulate learning
    print("📚 Learning from Spurk's messages...\n")
    for i, msg in enumerate(sample_messages, 1):
        ai.learn_from_message(msg)
        print(f"  [{i:2d}] Learned: {msg}")
        time.sleep(0.1)  # Small delay for visual effect
    
    print()
    stats = ai.get_stats()
    print(f"✓ Training complete!")
    print(f"  - Total messages: {stats['total_messages']}")
    print(f"  - Word pairs: {stats['unique_word_pairs']}")
    print(f"  - Common phrases: {stats['common_phrases']}")
    print()
    
    # Generate responses
    print("=" * 60)
    print("🤖 Generating responses in Spurk's style:")
    print("=" * 60)
    print()
    
    # Generate several responses
    prompts = [
        "What do you think about this?",
        "Want to hang out?",
        "How's the project going?",
        "That's interesting",
        "Let me know your thoughts"
    ]
    
    for i, prompt in enumerate(prompts, 1):
        print(f"Prompt {i}: {prompt}")
        response = ai.generate_response(prompt)
        print(f"SpurkAI: {response}")
        print()
        time.sleep(0.3)
    
    # Show some random generations
    print("=" * 60)
    print("🎲 Random generations (no prompt):")
    print("=" * 60)
    print()
    
    for i in range(5):
        response = ai.generate_response()
        print(f"  {i+1}. {response}")
        time.sleep(0.2)
    
    print()
    print("=" * 60)
    print("Demo complete! The AI has learned Spurk's style.")
    print("In a real Discord bot, this learning happens automatically")
    print("as Spurk sends messages.")
    print("=" * 60)

if __name__ == '__main__':
    demo()
