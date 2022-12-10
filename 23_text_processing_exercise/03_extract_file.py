def file_extract(filepath: list):
    file, extension = filepath[-1].split(".")
    return f"File name: {file}\nFile extension: {extension}"


path = input().split("\\")
print(file_extract(path))
