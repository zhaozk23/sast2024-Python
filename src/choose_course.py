import pandas as pd
import streamlit as st
import bisect

all_courses = st.session_state['course_info']
student = st.session_state['student']


def click():
    st.session_state['searched'] = True


def search_course(search: str):
    res = []
    for course in all_courses.values():
        if (search.lower() in course['name'].lower() or
                search.lower() in course['id'].lower() or
                search.lower() in course['teacher'].lower()):
            course['selected'] = False
            res.append(course)
    return res


st.header("选择课程")
search_term = st.text_input(label="搜索课程ID/课程名称/课程教师", help="不区分大小写")
search_term = search_term.strip()
st.button("搜索", on_click=click)
if st.session_state['searched']:
    results = search_course(search_term)
else:
    results = search_course("")
if len(results) == 0:
    st.error("课程不存在")
else:
    st.write("可选课程：")
    df = pd.DataFrame(results)
    editor = st.data_editor(
        df,
        column_config={
            "id": "课程ID",
            "name": "课程名称",
            "teacher": "课程教师",
            "department": "开课院系",
            "time": "上课时间",
            "selected": "是否选课",
        },
        disabled=["id", "name", "teacher", "department", "time"])
    if st.button(label="提交选课"):
        for (idx, choice) in enumerate(editor['selected']):
            if choice:
                bisect.insort_left(student['selected'], editor.loc[idx, 'id'])
        st.success("成功选课")
