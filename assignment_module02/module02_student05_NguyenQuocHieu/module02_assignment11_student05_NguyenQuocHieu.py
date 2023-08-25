class UniversityScoring:
    def __init__(self, regularScore: float, midtermScore: float, finalExamScore: float) -> None:
        self.regularScore = regularScore
        self.midtermScore = midtermScore
        self.finalExamScore = finalExamScore

    def average(self) -> float:
        """
        Calculate the average score 
        """
        return self.regularScore * 0.1 + self.midtermScore * 0.3 + self.finalExamScore * 0.6

    def rate(self) -> str:
        value = self.average()
        if value < 4.0:
            return "F"
        elif value < 5.0:
            return "D"
        elif value < 5.5:
            return "D+"
        elif value < 6.5:
            return "C"
        elif value < 7.0:
            return "C+"
        elif value < 8.0:
            return "B"
        elif value < 8.5:
            return "B+"
        elif value < 9.0:
            return "A"
        else:
            return "A+"


if __name__ == "__main__":
    scoring = UniversityScoring(
        regularScore=8.0, midtermScore=10.0, finalExamScore=6.0)
    print(scoring.rate())
