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


class Unit:
    def __init__(self, files: int) -> None:
        self.__models: list[Model] = []
        self.__ranks: int = 0
        self.__files = files

    def addModel(self, model: Model) -> None:
        self.__models.append(model)

    def size(self) -> int:
        return len(self.__models)
