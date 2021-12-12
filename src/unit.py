""" A single model
        has a move which indicates its maximum movement in a single turn
        it is defined by its base with a given width and length
"""
class Model:
    def __init__(self, move:int, width: int, length: int) -> None:
        self.__move = move
        self.__width = width
        self.__length = length

    def getMove(self) -> int:
        return self.__move

    def getWidth(self) -> int:
        return self.__width

    def getLength(self) -> int: 
        return self.__length


""" A single unit
        is defined by its models and number of files
        it is organized in a number of ranks consisting of models in each file
"""
class Unit:
    """ Constructs a unit
            precondition: the number of files must be at least 5
    """
    def __init__(self, files: int) -> None:
        self.__models: list[Model] = []
        self.__files = files

    """ Adds an amount of models to the unit
    """
    def add(self, model: Model, amount: int) -> None:
        for i in range(amount):
            self.__models.append(model)

    """ Returns the size of the unit
    """
    def size(self) -> int:
        return len(self.__models)

    """ Returns the number of ranks in the unit
    """
    def ranks(self) -> int:
        return self.size() // self.__files
