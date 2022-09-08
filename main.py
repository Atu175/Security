import os
PERMISSION = ["public", "secret", "top", "majestys"]


class Documents:
    def __init__(self, permission, filename):
        pass


class Person:
    def __init__(self, permission):
        self.permission = permission

    def createFile(self, filename):
        if ".txt" not in filename:
            filename = filename + ".txt"
        path = "files"
        file_directory = os.listdir(path)
        if filename not in file_directory:
            f = open("file/" + filename, "w")
            f.write(str(self.permission) + "\n")
            f.close()
            print(f"{filename} created succesfully!")
        else:
            print(f"Sorry , but the file already exist")

    def readFile(self, document):
        with open(document.filename, "r") as f:
            if PERMISSION.index(self.permission) >= PERMISSION.index(document.permission):
                f.readlines()
            else:
                print("Permission denied to read from {} to {}".format(self.permission, document.permission))

    def writeFile(self, document, text):
        with open(document.filename, "a") as f:
            if PERMISSION.index(self.permission) <= PERMISSION.index(document.permission):
                f.writelines("\n")
                f.writelines(text)
            else:
                print("Permission denied to write from {} to {}".format(self.permission, document.permission))
if __name__ == "__main__":
    pass


