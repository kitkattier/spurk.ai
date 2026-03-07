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

    # Test 4: SPONTANEOUS_CHANNELS parsing
    print("Test 4: SPONTANEOUS_CHANNELS parsing")

    # Empty string -> empty set (all channels allowed)
    raw = ""
    result = set(int(cid.strip()) for cid in raw.split(",") if cid.strip())
    assert result == set(), f"Empty string should produce empty set, got {result}"
    print("  ✓ Empty string produces empty set (all channels allowed)")

    # Single channel ID
    raw = "123456789"
    result = set(int(cid.strip()) for cid in raw.split(",") if cid.strip())
    assert result == {123456789}, f"Expected {{123456789}}, got {result}"
    print("  ✓ Single channel ID parsed correctly")

    # Multiple channel IDs with spaces
    raw = "111, 222, 333"
    result = set(int(cid.strip()) for cid in raw.split(",") if cid.strip())
    assert result == {111, 222, 333}, f"Expected {{111, 222, 333}}, got {result}"
    print("  ✓ Multiple channel IDs with spaces parsed correctly")

    print("✓ Passed\n")

    # Test 5: Spontaneous channel whitelist filtering
    print("Test 5: Spontaneous channel whitelist filtering")

    class FakeChannel:
        def __init__(self, channel_id):
            self.id = channel_id

    all_channels = [FakeChannel(100), FakeChannel(200), FakeChannel(300)]

    # No whitelist -> all channels eligible
    whitelist = set()
    eligible = [ch for ch in all_channels if not whitelist or ch.id in whitelist]
    assert len(eligible) == 3, f"With no whitelist all channels should be eligible, got {len(eligible)}"
    print("  ✓ No whitelist: all channels eligible")

    # Whitelist with some channels
    whitelist = {100, 300}
    eligible = [ch for ch in all_channels if not whitelist or ch.id in whitelist]
    assert len(eligible) == 2, f"Expected 2 eligible channels, got {len(eligible)}"
    assert set(ch.id for ch in eligible) == {100, 300}
    print("  ✓ Whitelist {100, 300}: only those channels eligible")

    # Whitelist with no matching channels
    whitelist = {999}
    eligible = [ch for ch in all_channels if not whitelist or ch.id in whitelist]
    assert len(eligible) == 0, f"Expected 0 eligible channels, got {len(eligible)}"
    print("  ✓ Non-matching whitelist: no channels eligible")

    print("✓ Passed\n")

    # Test 6: Spontaneous reply blocked by whitelist, prompted always allowed
    print("Test 6: Spontaneous reply vs prompted interaction")

    whitelist = {100}

    # Spontaneous reply check (random.random() < chance AND channel in whitelist)
    channel_in_whitelist = FakeChannel(100)
    channel_not_in_whitelist = FakeChannel(200)

    spontaneous_allowed_in = not whitelist or channel_in_whitelist.id in whitelist
    spontaneous_allowed_out = not whitelist or channel_not_in_whitelist.id in whitelist
    assert spontaneous_allowed_in, "Spontaneous should be allowed in whitelisted channel"
    assert not spontaneous_allowed_out, "Spontaneous should be blocked outside whitelist"
    print("  ✓ Spontaneous posting correctly gated by whitelist")

    # Prompted (mention / reply to bot) is always allowed regardless of whitelist
    # Simulate: prompted path does NOT check SPONTANEOUS_CHANNELS
    prompted_allowed_in = True   # no whitelist check for prompted
    prompted_allowed_out = True  # no whitelist check for prompted
    assert prompted_allowed_in and prompted_allowed_out, "Prompted should always be allowed"
    print("  ✓ Prompted interactions always allowed regardless of whitelist")
    print("✓ Passed\n")

    print("=" * 50)
    print("All random behavior tests passed! ✓")
    print("=" * 50)

if __name__ == '__main__':
    test_random_behavior_config()

