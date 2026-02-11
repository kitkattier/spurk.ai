"""
Simple test script for SpurkAI functionality.
"""
import os
import json
from spurk_ai import SpurkAI

def test_spurk_ai():
    """Test the SpurkAI learning and generation."""
    print("Testing SpurkAI...\n")
    
    # Create a test instance with a temporary file
    test_file = "test_spurk_data.json"
    if os.path.exists(test_file):
        os.remove(test_file)
    
    ai = SpurkAI(data_file=test_file)
    
    # Test 1: Initial stats
    print("Test 1: Initial stats")
    stats = ai.get_stats()
    assert stats['total_messages'] == 0, "Should start with 0 messages"
    print("✓ Passed\n")
    
    # Test 2: Learn from messages
    print("Test 2: Learning from messages")
    test_messages = [
        "Hey everyone, how's it going?",
        "I love coding in Python",
        "This is a great day for programming",
        "Let's build something amazing",
        "Python is my favorite language",
        "I'm working on a cool project",
        "Discord bots are fun to make",
        "Let me know what you think",
        "That sounds like a plan",
        "I agree with that idea"
    ]
    
    for msg in test_messages:
        ai.learn_from_message(msg)
    
    stats = ai.get_stats()
    assert stats['total_messages'] == len(test_messages), f"Should have {len(test_messages)} messages"
    assert stats['unique_word_pairs'] > 0, "Should have learned word pairs"
    print(f"✓ Learned {stats['total_messages']} messages")
    print(f"✓ Created {stats['unique_word_pairs']} word pairs")
    print(f"✓ Found {stats['common_phrases']} common phrases\n")
    
    # Test 3: Generate responses
    print("Test 3: Generating responses")
    for i in range(5):
        response = ai.generate_response()
        assert len(response) > 0, "Response should not be empty"
        print(f"  Response {i+1}: {response}")
    print("✓ Passed\n")
    
    # Test 4: Data persistence
    print("Test 4: Data persistence")
    assert os.path.exists(test_file), "Data file should be created"
    
    # Create a new instance and verify data is loaded
    ai2 = SpurkAI(data_file=test_file)
    stats2 = ai2.get_stats()
    assert stats2['total_messages'] == stats['total_messages'], "Data should persist"
    print("✓ Data saved and loaded successfully\n")
    
    # Test 5: Message limit (keep last 1000)
    print("Test 5: Message limit")
    for i in range(1100):
        ai.learn_from_message(f"Test message number {i}")
    
    stats = ai.get_stats()
    assert stats['total_messages'] == 1000, "Should cap at 1000 messages"
    print("✓ Message limit enforced\n")
    
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
    
    print("=" * 50)
    print("All tests passed! ✓")
    print("=" * 50)

if __name__ == '__main__':
    test_spurk_ai()
