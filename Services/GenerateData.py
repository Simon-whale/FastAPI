class DataGenerator:
    def __init__(self):
        pass

    @staticmethod
    def create(start: int = 0, end: int = 100): # -> list[int]:
        values = []

        if start == 0 and end == 0:
            return values

        if start == end: return  values

        for index in range(start, end):
            values.append(index)

        return values
