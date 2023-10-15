# Bài tập 3:
import matplotlib.pyplot as plt

class plotting:
    def __init__(self, x, y):
        self.x = x  
        self.y = y  
        
    def point(self):
        fig, ax = plt.subplots()
        ax.scatter(self.x, self.y)
        fig.show()
        
    def line(self, other):
        fig, ax = plt.subplots()
        A = [self.x, self.y]
        B = [other.x, other.y]
        ax.plot(A, B)
        fig.show()
        
    def circle(self, R):
        fig, ax = plt.subplots()
        ax.scatter(self.x, self.y, s=R*2000)
        fig.show()
        
if __name__ == '__main__':
    A = plotting(3,5)
    B = plotting(1,2)
    A.point()
    A.line(B)
    A.circle(31)