import os
import csv
import json


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found.")
            return False

    def create_output_folder(self, folder="output"):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.students = list(reader)

            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students

        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return []

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-" * 30)

        for student in self.students[:n]:
            print(
                f"{student['student_id']} | "
                f"{student['age']} | "
                f"{student['gender']} | "
                f"{student['country']} | "
                f"GPA: {student['GPA']}"
            )

        print("-" * 30)


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        sorted_students = sorted(
            self.students,
            key=lambda x: float(x["final_exam_score"]),
            reverse=True
        )

        top10 = sorted_students[:10]

        top_10_list = []

        for i in range(len(top10)):
            student = top10[i]

            top_10_list.append({
                "rank": i + 1,
                "student_id": student["student_id"],
                "country": student["country"],
                "major": student["major"],
                "final_exam_score": float(student["final_exam_score"]),
                "GPA": float(student["GPA"])
            })

        self.result = {
            "analysis": "Top 10 Students by Exam Score",
            "total_students": len(self.students),
            "top_10": top_10_list
        }

        return self.result

    def print_results(self):
        print("-" * 30)
        print("Top 10 Students by Exam Score")
        print("-" * 30)

        for student in self.result["top_10"]:
            print(
                f"{student['rank']}. "
                f"{student['student_id']} | "
                f"{student['country']} | "
                f"{student['major']} | "
                f"Score: {student['final_exam_score']} | "
                f"GPA: {student['GPA']}"
            )

        print("-" * 30)


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, "w", encoding="utf-8") as file:
                json.dump(self.result, file, indent=4)

            print(f"Result saved to {self.output_path}")

        except Exception as e:
            print(f"Error while saving file: {e}")


fm = FileManager("students.csv")

if not fm.check_file():
    print("Stopping program.")
    exit()

fm.create_output_folder()

dl = DataLoader("students.csv")
dl.load()
dl.preview()

analyser = DataAnalyser(dl.students)
analyser.analyse()
analyser.print_results()

saver = ResultSaver(analyser.result, "output/result.json")
saver.save_json()