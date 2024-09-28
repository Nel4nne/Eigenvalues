from datetime import datetime



class Printer:
    __file_name: str = None
    __file_path: str = None

    @staticmethod
    def SetFileName(file_name: str) -> None:
        Printer.__file_name = file_name

    @staticmethod
    def SetFilePath(file_path: str) -> None:
        Printer.__file_path = file_path

    @staticmethod
    def print(text: str) -> None:
        if Printer.__file_path is None:
            Printer.__file_path = "Results/"
        if Printer.__file_name is None:
            Printer.__file_name = f"result-{datetime.timestamp(datetime.now())}.txt"
        with open(Printer.__file_path + Printer.__file_name, "a", encoding="utf-8") as file:
            file.write(text + "\n")
        