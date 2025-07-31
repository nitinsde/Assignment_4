doc1 = "sample.txt"
try:
    doc1 = open("sample.txt", "r")
    file_data = doc1.read()
    print(file_data)
    doc1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")


