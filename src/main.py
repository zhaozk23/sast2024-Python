import json
import sys
import streamlit as st


def load_data(filepath):
    data_dict = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                data = json.loads(line)
                data_dict[data['id']] = data
            return data_dict
    except OSError:
        st.error("读取文件失败")
        sys.exit()


def save_data(filepath, student):
    # 保存数据到JSON文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(json.dumps(student) + '\n')


if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'student_id' not in st.session_state:
    st.session_state['student_id'] = None
if 'student_info' not in st.session_state:
    st.session_state['student_info'] = {}
if 'course_info' not in st.session_state:
    st.session_state['course_info'] = {}
if 'student' not in st.session_state:
    st.session_state['student'] = None
if 'searched' not in st.session_state:
    st.session_state['searched'] = False
if 'student_path' not in st.session_state:
    st.session_state['student_path'] = ""


def login():
    st.header('登录页')
    st.session_state['student_id'] = st.text_input(label="输入学号", help="如：001")
    student = st.session_state['student_info'].get(st.session_state['student_id'])
    if st.button('登录'):
        if student is None:
            st.error("学号不存在，请重新输入")
            if st.button(label="重试"):
                st.rerun()
        else:
            st.session_state['logged_in'] = True
            st.session_state['student'] = student
            student['selected'].sort()
            st.success("登录成功")
            st.rerun()


def logout():
    if st.session_state['student'] is not None:
        save_data(st.session_state['student_path'], st.session_state['student'])
        st.session_state['student'] = None
    st.session_state['logged_in'] = False
    st.session_state['student_id'] = None
    st.session_state['student_info'] = {}
    st.session_state['course_info'] = {}
    st.session_state['searched'] = False
    st.session_state['student_path'] = ""
    st.rerun()


logout_page = st.Page(logout, title="退出")
choose_course_page = st.Page("choose_course.py", title="选择课程")
view_courses_page = st.Page("view_courses.py", title="查看已选课程")


def main(student_file, courses_file):
    st.session_state['student_info'] = load_data(student_file)
    st.session_state['student_path'] = student_file
    st.session_state['course_info'] = load_data(courses_file)
    st.title('选课系统')
    if not st.session_state['logged_in']:
        pg = st.navigation([st.Page(login)])
    else:
        pg = st.navigation([choose_course_page, view_courses_page, logout_page])
    pg.run()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <student_filepath> <courses_filepath>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
