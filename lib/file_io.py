def write_file(file_name, file_content):
    """Write file_content to a .txt file with the given file_name."""
    file_path = f"lib/{file_name}.txt"
    with open(file_path, mode="w", encoding="UTF-8") as file:
        file.write(file_content)


def append_file(file_name, append_content):
    """Append append_content to a .txt file with the given file_name."""
    file_path = f"lib/{file_name}.txt"
    with open(file_path, mode="a", encoding="UTF-8") as file:
        file.write(append_content)


def read_file(file_name):
    """Read and return the content of a .txt file with the given file_name."""
    file_path = f"lib/{file_name}.txt"
    with open(file_path, mode="r", encoding="UTF-8") as file:
        return file.read()
