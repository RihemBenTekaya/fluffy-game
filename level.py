def load_level(level1):
    with open(level1, "r") as file:
        return [list(line.strip()) for line in file.readlines()]
