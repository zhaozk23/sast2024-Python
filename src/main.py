import json
import sys


def load_data(filepath):
    students_dict = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            student = json.loads(line)
            students_dict[student['id']] = student
    return students_dict


def select_course(student, courses):
    while True:
        search_key = input("Do you want to search by name/course id/teacher?\n")
        print("Type 'quit' to quit")
        found = False
        if search_key == 'name':
            name = input("Name of course: ")
            for c in courses.values():
                if c.get('name') == name:
                    student['selected'].append(c['id'])
                    found = True
        elif search_key == 'course id':
            course_id = input("Course ID: ")
            for c in courses.values():
                if c.get('id') == course_id:
                    student['selected'].append(c['id'])
                    found = True
        elif search_key == 'teacher':
            teacher = input("Teacher: ")
            for c in courses.values():
                if c.get('teacher') == teacher:
                    student['selected'].append(c['id'])
                    found = True
        elif search_key == 'quit':
            break
        else:
            print("Invalid input")
        if found:
            print(f"Course with given {search_key} is selected.")
        else:
            print(f"Course with given {search_key} does not exist.")


def view_selected_courses(student):
    # 查看已选课程
    print(f"Student {student['name']} has selected:\n {student['selected']}")


def save_data(filepath, data):
    # 保存数据到JSON文件
    with open(filepath, 'w', encoding='utf-8') as f:
        for student in data.values():
            f.write(json.dumps(student) + '\n')


def print_menu():
    print("\n选课系统菜单：")
    print("1. 选课")
    print("2. 查看已选课程")
    print("3. 退出")


def main(student_file, courses_file):
    students = load_data(student_file)
    courses = load_data(courses_file)

    while True:
        print_menu()
        choice = input("请选择一个操作（1-3）：")

        if choice == '1':
            # 示例：选课操作
            # select_course(students['some_student_id'], courses)
            student_id = input("Please input your student id:")
            select_course(students[student_id], courses)
        elif choice == '2':
            # 示例：查看已选课程
            # view_selected_courses(students['some_student_id'])
            student_id = input("Please input your student id:")
            view_selected_courses(students[student_id])
        elif choice == '3':
            print("退出系统。")
            break
        else:
            print("无效的输入，请重新选择。")

    # 保存学生数据
    save_data(student_file, students)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <student_filepath> <courses_filepath>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
