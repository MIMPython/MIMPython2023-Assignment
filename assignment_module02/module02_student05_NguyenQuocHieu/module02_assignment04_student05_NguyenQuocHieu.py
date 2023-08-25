class TextEditor:
    def __init__(self, text: str) -> None:
        self.text = text

    def contains(self, keyword: str) -> bool:
        """
        Check whether the text contains the keyword.

        Arguments:
            keyword {str} -- Keyword which you want to check

        Returns:
            bool -- True if the text contains the keyword
        """
        if self.text.find(keyword) < 0:
            return False
        return True

    def countFrequency(self, keyword: str) -> int:
        """
        Calculate the frequency of the keyword appearing in the text.
        Arguments: 
            keyword {str} -- Keyword which you want to count

        Returns:
            int -- Number of times the keyword appearing in the text    
        """
        return self.text.count(keyword)

    def countNumberOfWords(self) -> int:
        """
        Count the number of words in the text.
        Returns:
            int -- Number of words in the text
        """
        numberOfSpace = self.text.count(" ")
        return (numberOfSpace + 1)

    def upper(self) -> str:
        """
        Convert all characters in the first sentence of the text to upper case
        Returns:
            str -- The text which first sentence is in upper case
        """
        firstPoint = self.text.find(".")
        if firstPoint >= 0:
            firstSentence = self.text[0: firstPoint]
            firstSentence = firstSentence.upper()
            lastSentence = self.text[firstPoint: len(self.text)]
            return firstSentence + lastSentence
        else:
            output = self.text
            return output.upper()


if __name__ == "__main__":
    text = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."

    textEditor = TextEditor(text=text)
    print("a)")
    keywords = ["Python", "contains", "experience", "difficult"]
    for keyword in keywords:
        message = "Is \"" + keyword + "\" in the text? "
        print(message, textEditor.contains(keyword=keyword))
    print("b)")
    print("What is the frequency of \"Python\"?",
          textEditor.countFrequency("Python"))
    print("c)")
    print("How many words are there in the text? ",
          textEditor.countNumberOfWords())
    print("d)")
    print("Rewrite the text:\n ", textEditor.upper())
