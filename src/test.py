import json


def main():
    with open("D:\\PythonProjects\\pythonProject\\sast2024-Python\\data\\student.json") as json_file:
        data = json.load(json_file)
        print(data)
