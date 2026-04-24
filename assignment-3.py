import csv
import json
import os


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        print(f"Error: {self.filename} not found. Please download the file from LMS.")
        return False

    def create_output_folder(self, folder="output"):
        print("Checking output folder...")
        if os.path.exists(folder):
            print(f"Output folder already exists: {folder}/")
        else:
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.students = list(csv.DictReader(file))
            print(f"Data loaded successfully: {len(self.students)} students")
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
        except Exception as error:
            print(f"Error: could not load data: {error}")
        return self.students

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
        gpas = []
        high_performers = 0

        for student in self.students:
            try:
                gpa = float(student["GPA"])
            except ValueError:
                print(
                    f"Warning: could not convert value for student "
                    f"{student['student_id']} — skipping row."
                )
                continue

            gpas.append(gpa)
            if gpa > 3.5:
                high_performers += 1

        average_gpa = round(sum(gpas) / len(gpas), 2)
        max_gpa = max(gpas)
        min_gpa = min(gpas)

        high_gpa = list(filter(lambda s: float(s["GPA"]) > 3.8, self.students))
        gpa_values = list(map(lambda s: float(s["GPA"]), self.students))
        hard_workers = list(
            filter(lambda s: float(s["study_hours_per_day"]) > 4, self.students)
        )

        print("-" * 30)
        print("Lambda / Map / Filter")
        print("-" * 30)
        print(f"GPA > 3.8 : {len(high_gpa)}")
        print(f"GPA values (first 5) : {gpa_values[:5]}")
        print(f"study_hours_per_day > 4 : {len(hard_workers)}")
        print("-" * 30)

        self.result = {
            "analysis": "GPA Statistics",
            "total_students": len(self.students),
            "average_gpa": average_gpa,
            "max_gpa": max_gpa,
            "min_gpa": min_gpa,
            "high_performers": high_performers,
        }
        return self.result

    def print_results(self):
        print("-" * 30)
        print("GPA Analysis")
        print("-" * 30)
        print(f"Total students: {self.result['total_students']}")
        print(f"Average GPA: {self.result['average_gpa']}")
        print(f"Highest GPA: {self.result['max_gpa']}")
        print(f"Lowest GPA: {self.result['min_gpa']}")
        print(f"Students GPA>3.5 : {self.result['high_performers']}")
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
        except OSError as error:
            print(f"Error: could not save result to '{self.output_path}': {error}")


def main():
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

    DataLoader("wrong_file.csv").load()


if __name__ == "__main__":
    main()