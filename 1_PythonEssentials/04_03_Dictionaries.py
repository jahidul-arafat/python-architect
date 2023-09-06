from collections import defaultdict
# add a dictOperation method
def dictOperation():
    # add an animal dictionary
    animals = {
        "cat": "meow",
        "dog": "woof",
        "bird": "chirp"
    }
    print(animals)

    print(animals["cat"])
    print(animals["dog"])
    print(animals["bird"])

    # modify the animal cat value
    animals["cat"] = "puchka-pota"
    print(animals)

    # get the dictionary keys
    print(animals.keys())
    print(animals.values())

    # convert the dictionary to a list
    dictItemList = list(animals.items())
    print(dictItemList)
    print(dictItemList[0])
    print(animals.get("toot"))

    print(len(animals))

    # add a bird dictionary
    birds = {
        "a": ["aaa","abc"],
        "b":["bbb","cde"]
    }
    print(birds)
    if "c" not in birds:
        birds['c']=[]
        birds['c'].append('cccc')
    print(birds)

    # create a new default dictionary
    animalDefaultDict = defaultdict(list)
    print(animalDefaultDict)
    animalDefaultDict['e'].append('eee')
    print(animalDefaultDict)
    print(animalDefaultDict['f'])








# add a main method
def main():
    print("Hello World")
    dictOperation()

if __name__ == "__main__":
    main()