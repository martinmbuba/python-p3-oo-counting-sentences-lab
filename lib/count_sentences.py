#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        """Initialize MyString with a string value."""
        self.value = value
    
    @property
    def value(self):
        """Get the string value."""
        return self._value
    
    @value.setter
    def value(self, new_value):
        """Set the string value, printing message if not a string."""
        if not isinstance(new_value, str):
            print("The value must be a string.")
            self._value = ''
        else:
            self._value = new_value
    
    def is_sentence(self):
        """Return True if the value ends with a period."""
        return self.value.endswith('.')
    
    def is_question(self):
        """Return True if the value ends with a question mark."""
        return self.value.endswith('?')
    
    def is_exclamation(self):
        """Return True if the value ends with an exclamation mark."""
        return self.value.endswith('!')
    
    def count_sentences(self):
        """Count the number of sentences in the value."""
        if not self.value:
            return 0
        
        # Split on sentence-ending punctuation followed by space or end of string
        import re
        
        # Split on ., !, or ? followed by optional whitespace
        sentences = re.split(r'[.!?]+', self.value)
        
        # Filter out empty strings and strings with only whitespace
        sentences = [s.strip() for s in sentences if s.strip()]
        
        return len(sentences)
