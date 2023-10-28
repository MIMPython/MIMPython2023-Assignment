def run():
    """
    Example:
    
    Input: [1, 2, 3]
    Output: 2.0
    
    Input: [1]
    Output: 1.0
    """
    try:
        arrayString = input("Input a list: ")
        arrayString = arrayString[1:-1]
        comma = arrayString.split(",")
        array = []
        for element in comma:
            array.append(int(element))
        print("Average: ", sum(array) / len(array))
    except ValueError:
       print("Input must be a list")

if __name__ == "__main__":
    run()
