def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip().split("\n")