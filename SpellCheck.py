import re, time


def main():
    dictionary = loadWordsFromFile("Data\dictionary.txt")
    aliceWords = loadWordsFromFile("Data\AliceInWonderLand.txt")

    for i in range(len(aliceWords)):
        aliceWords[i] = aliceWords[i].lower()

    loop = True
    while loop:
        #print main menu
        print('\nMain Menu')
        print('1: Spell Check a Word (Linear)')
        print('2: Spell Check a Word (Binary)')
        print('3: Spell Check Alice in Wonderland (Linear)')
        print('4: Spell Check Alice in Wonderland (Binary)')

        #Selection
        selection = input("Enter selection (1-5): ")

        if selection == '1':
            print('\nSpell Check a Word (Linear)')
            word = input("Look up a word: ")
            index = linearSearch(dictionary, word)
            TimeStart = time.perf_counter()
            if index == -1:
                TimeEnd = time.perf_counter()
                TimeOutput = TimeEnd - TimeStart
                print(f"{word} cannot be found under {TimeOutput} seconds")
            else:
                TimeEnd = time.perf_counter()
                TimeOutput = TimeEnd - TimeStart
                print(
                    f"{word} was found at position {index} under {TimeOutput} seconds"
                )

        if selection == '2':
            print('\nSpell Check a Word (Binary)')
            word = input("Look up a word: ")
            index = binarySearch(dictionary, word)
            TimeStart = time.perf_counter()
            if index == -1:
                TimeEnd = time.perf_counter()
                TimeOutput = TimeEnd - TimeStart
                print(f"{word} cannot be found under {TimeOutput} seconds")
            else:
                TimeEnd = time.perf_counter()
                TimeOutput = TimeEnd - TimeStart
                print(
                    f"{word} was found at position {index} under {TimeOutput} seconds"
                )

        if selection == '3':
            print('\nSpell Check Alice in Wonderland (Linear)')
            result = 0
            TimeStart = time.perf_counter()
            print("This will take ~1 minute")
            for word in aliceWords:
                index = linearSearch(dictionary, word)
                TimeEnd = time.perf_counter()
                if index == -1:
                    result += 1
            TimeOutput = TimeEnd - TimeStart
            print(
                f"{result} words were not found in the dictionary under {TimeOutput} seconds"
            )

        if selection == '4':
            print('\nSpell Check Alice in Wonderland (Binary)')
            result = 0
            TimeStart = time.perf_counter()
            for word in aliceWords:
                index = binarySearch(dictionary, word)
                TimeEnd = time.perf_counter()
                if index == -1:
                    result += 1
            TimeOutput = TimeEnd - TimeStart
            print(
                f"{result} words were not found in the dictionary under {TimeOutput} seconds"
            )


def linearSearch(anArray, anItem):
    for i in range(len(anArray)):
        if anArray[i] == anItem:
            return i
    return -1


def binarySearch(anArray, anItem):
    low = 0
    high = len(anArray) - 1

    while low <= high:
        mid = (low + high) // 2
        if anArray[mid] == anItem:
            return mid
        elif anItem < anArray[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def loadWordsFromFile(fileName):
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    return re.split('\s+', textData)


main()
