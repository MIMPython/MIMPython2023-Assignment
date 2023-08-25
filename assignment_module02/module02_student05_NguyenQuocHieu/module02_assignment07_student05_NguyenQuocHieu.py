class ROT13Coder:
    def __init__(self, text: str) -> None:
        self.text = text.upper()

    def encode(self) -> str:
        output = ""
        for character in self.text:
            if ord(character) <= 77:
                output += chr(ord(character) + 13)
            else:
                output += chr(ord(character) - 13)
        return output

    def decode(self) -> str:
        output = ""
        for character in self.text:
            if ord(character) <= 77:
                output += chr(ord(character) + 13)
            else:
                output += chr(ord(character) - 13)
        return output


if __name__ == "__main__":
    text = "PYTHON"
    coder = ROT13Coder(text=text)
    print(coder.encode())
    print(coder.decode())
