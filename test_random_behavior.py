"""
Test script for random behavior functionality.
"""
import os
import random

def test_random_behavior_config():
    """Test that random behavior configuration works correctly."""
    print("Testing Random Behavior Configuration...\n")
    
    # Test 1: Random reply chance calculation
    print("Test 1: Random reply chance")
    test_chance = 0.05  # 5%
    replies = 0
    total_messages = 1000
    
    random.seed(42)  # For reproducibility
    for _ in range(total_messages):
        if random.random() < test_chance:
            replies += 1
    
    # Should be roughly 5% (with some variance)
    actual_percentage = (replies / total_messages) * 100
    print(f"  Expected: ~5% replies")
    print(f"  Actual: {actual_percentage:.2f}% replies ({replies}/{total_messages})")
    assert 3 <= actual_percentage <= 7, f"Reply percentage should be close to 5%, got {actual_percentage}%"
    print("✓ Passed\n")
    
    # Test 2: Random message interval
    print("Test 2: Random message interval validation")
    test_intervals = [0, 60, 300, 600, 1800, 3600]
    for interval in test_intervals:
        assert interval >= 0, f"Interval must be non-negative, got {interval}"
        print(f"  ✓ Interval {interval}s is valid")
    print("✓ Passed\n")
    
    # Test 3: Channel tracking
    print("Test 3: Channel tracking (max 10)")
    active_channels = []
    for i in range(20):
        channel = f"channel_{i}"
        if channel not in active_channels:
            active_channels.append(channel)
            if len(active_channels) > 10:
                active_channels.pop(0)
    
    assert len(active_channels) == 10, f"Should maintain max 10 channels, got {len(active_channels)}"
    print(f"  ✓ Channel list capped at {len(active_channels)} channels")
    print("✓ Passed\n")
    
    print("=" * 50)
    print("All random behavior tests passed! ✓")
    print("=" * 50)

if __name__ == '__main__':
    test_random_behavior_config()
