import streamlit as st
import pandas as pd


all_courses = st.session_state['course_info']
student = st.session_state['student']

st.header('查看选课')
st.write(f"{student['name']} 已选课程:\n")
selected_courses = {}
for course_id in student['selected']:
    selected_courses[course_id] = all_courses[course_id]['name']
df = pd.DataFrame.from_dict(selected_courses, orient='index', columns=["已选课程"])
st.dataframe(df)
