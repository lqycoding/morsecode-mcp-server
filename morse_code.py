class MorseCode:
    def __init__(self):
        self.morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
            '9': '----.', ' ': ' ', '.': '.-.-.-', ',': '--..--', '?': '..--..',
            '!': '-.-.--', '@': '.--.-.'
        }
        self.reverse_morse_dict = {v: k for k, v in self.morse_dict.items()}
    
    def encode(self, text):
        """将文本转换为摩尔斯电码"""
        if not text:
            return ''
        
        text = text.upper()
        morse_code = []
        
        for char in text:
            if char in self.morse_dict:
                morse_code.append(self.morse_dict[char])
        
        return ' '.join(morse_code)
    
    def decode(self, morse_code):
        """将摩尔斯电码转换为文本"""
        if not morse_code:
            return ''
        
        text = []
        morse_words = morse_code.split('  ')
        
        for word in morse_words:
            morse_chars = word.split()
            decoded_chars = []
            
            for char in morse_chars:
                if char in self.reverse_morse_dict:
                    decoded_chars.append(self.reverse_morse_dict[char])
            
            text.append(''.join(decoded_chars))
        
        return ' '.join(text)