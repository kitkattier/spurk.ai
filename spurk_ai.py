import json
import os
from typing import List, Dict
from collections import defaultdict
import random

# Constants
MIN_RESPONSE_LENGTH = 10
MAX_STORED_MESSAGES = 1000
MAX_COMMON_PHRASES = 100

class SpurkAI:
    """
    AI model that learns from Spurk's messages and generates responses in their style.
    """
    
    def __init__(self, data_file: str = "spurk_data.json"):
        self.data_file = data_file
        self.messages: List[str] = []
        self.word_pairs: Dict[str, List[str]] = defaultdict(list)
        self.common_phrases: List[str] = []
        self.load_data()
    
    def load_data(self):
        """Load training data from file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.messages = data.get('messages', [])
                    self.word_pairs = defaultdict(list, data.get('word_pairs', {}))
                    self.common_phrases = data.get('common_phrases', [])
                    print(f"Loaded {len(self.messages)} messages from training data")
            except Exception as e:
                print(f"Error loading data: {e}")
    
    def save_data(self):
        """Save training data to file."""
        try:
            data = {
                'messages': self.messages,
                'word_pairs': dict(self.word_pairs),
                'common_phrases': self.common_phrases
            }
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def learn_from_message(self, message: str):
        """Learn from a new message from Spurk."""
        if not message or len(message.strip()) == 0:
            return
        
        # Store the message
        self.messages.append(message)
        
        # Keep only last MAX_STORED_MESSAGES to prevent data file from growing too large
        if len(self.messages) > MAX_STORED_MESSAGES:
            self.messages = self.messages[-MAX_STORED_MESSAGES:]
        
        # Extract word pairs for Markov chain-like generation
        words = message.split()
        for i in range(len(words) - 1):
            self.word_pairs[words[i].lower()].append(words[i + 1])
        
        # Store common phrases (messages with 3-10 words)
        if 3 <= len(words) <= 10:
            if message not in self.common_phrases:
                self.common_phrases.append(message)
                if len(self.common_phrases) > MAX_COMMON_PHRASES:
                    self.common_phrases = self.common_phrases[-MAX_COMMON_PHRASES:]
        
        self.save_data()
    
    def generate_response(self, trigger_message: str = "") -> str:
        """
        Generate a response in Spurk's style.
        Uses learned patterns and phrases.
        """
        # If we don't have enough data, return a default response
        if len(self.messages) < 5:
            return "I'm still learning from Spurk... give me some time!"
        
        # Strategy 1: Use a common phrase (50% chance if we have them)
        if self.common_phrases and random.random() < 0.5:
            return random.choice(self.common_phrases)
        
        # Strategy 2: Generate using word pairs (Markov chain approach)
        if self.word_pairs and random.random() < 0.7:
            # Try to start with a word from the trigger message
            start_words = trigger_message.lower().split() if trigger_message else []
            start_word = None
            
            for word in start_words:
                if word in self.word_pairs:
                    start_word = word
                    break
            
            # If no matching word, pick a random start
            if not start_word:
                start_word = random.choice(list(self.word_pairs.keys()))
            
            # Generate a sentence
            response_words = [start_word]
            current_word = start_word
            
            for _ in range(random.randint(3, 15)):
                if current_word.lower() in self.word_pairs:
                    next_word = random.choice(self.word_pairs[current_word.lower()])
                    response_words.append(next_word)
                    current_word = next_word
                else:
                    break
            
            response = ' '.join(response_words)
            if len(response) > MIN_RESPONSE_LENGTH:
                return response
        
        # Strategy 3: Return a random message
        return random.choice(self.messages)
    
    def get_stats(self) -> Dict:
        """Get statistics about the training data."""
        return {
            'total_messages': len(self.messages),
            'unique_word_pairs': len(self.word_pairs),
            'common_phrases': len(self.common_phrases)
        }
