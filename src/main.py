import json
import sys

def load_data(filepath):
    # 加载JSON文件数据
    pass

def select_course(student, courses):
    # 实现选课逻辑
    pass

def view_selected_courses(student):
    # 查看已选课程
    pass

def save_data(filepath, data):
    # 保存数据到JSON文件
    pass

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
            pass
        elif choice == '2':
            # 示例：查看已选课程
            # view_selected_courses(students['some_student_id'])
            pass
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