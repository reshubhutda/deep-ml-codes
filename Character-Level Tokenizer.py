class CharTokenizer:
    def __init__(self, text: str):

        self.BOS = 0
        self.EOS = 1
        self.text = text
        self.len_text = len(self.text)
        self.sort_text = sorted(set(self.text))

        self.stoi = {
            "<BOS>": self.BOS,
            "<EOS>": self.EOS
        }

        for i, j in enumerate(self.sort_text, start=2):
            self.stoi[j] = i

        self.itos = {value: key for key, value in self.stoi.items()}

        self.vocab_size = len(self.stoi)
    def encode(self, text: str) -> list:
        self.encoded_text = []
        self.encoded_text.append(self.BOS)

        for i in range(len(text)):
            self.encoded_text.append(self.stoi[text[i]])

        self.encoded_text.append(self.EOS)

        return self.encoded_text
    
    def decode(self, indices: list) -> str:
        decoded_text = ""
        for i in indices:
            decoded_text += self.itos[i]
        return decoded_text
        