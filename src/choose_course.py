import pandas as pd
import streamlit as st

all_courses = st.session_state['course_info']
all_students = st.session_state['student_info']
student = all_students[st.session_state['student_id']]


def search_course():
    res = []
    for course in all_courses.values():
        if (search_term.lower() in course['name'].lower() or
                search_term.lower() in course['id'].lower() or
                search_term.lower() in course['teacher'].lower()):
            course['selected'] = False
            res.append(course)
    return res


st.header("选择课程")
search_term = st.text_input(label="搜索课程ID/课程名称/课程教师", help="不区分大小写")
search_term = search_term.strip()
results = search_course()
st.write("可选课程：")
df = pd.DataFrame(results)
editor = st.data_editor(df, disabled=("id", "name", "teacher", "department", "time"))
if st.button(label="提交选课"):
    for (idx, choice) in enumerate(editor['selected']):
        if choice:
            student['selected'].append(editor.loc[idx, 'id'])
    st.success("成功选课")
