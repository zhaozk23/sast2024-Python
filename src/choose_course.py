import pandas as pd
import streamlit as st
import bisect

all_courses = st.session_state['course_info']
student = st.session_state['student']


def conv_time(time_str):
    weekday, time = time_str.split(' ', 1)
    start, end = time.split('-', 1)
    start = int(start.split(':')[0]) * 60 + int(start.split(':')[1])
    end = int(end.split(':')[0]) * 60 + int(end.split(':')[1])
    weekday = st.session_state['week'][weekday]
    return weekday, start, end


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


def conflicting_course(selected, course_id):
    for i in selected:
        stime = conv_time(all_courses[i]['time'])
        ctime = conv_time(all_courses[course_id]['time'])
        if (i != course_id and stime[0] == ctime[0]
                and min(stime[2], ctime[2]) > max(stime[1], ctime[1])):
            return True, i
    return False, None


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
        conf = False
        for (idx, choice) in enumerate(editor['selected']):
            if choice:
                conf, si = conflicting_course(student['selected'], editor.loc[idx, 'id'])
                if conf:
                    st.error(f"所选课程{editor.loc[idx, 'id']}与已选课程{si}时间冲突")
                    break
                else:
                    bisect.insort_left(student['selected'], editor.loc[idx, 'id'])
        if not conf:
            st.success("成功选课")
