import time
import streamlit as st

def show_diff_page():
  st.title("Live Feed")
  run = st.checkbox('Run',key="1")
  #FRAME_WINDOW = st.image([])
  #F1 = st.image([])
  F2 = st.image([])







  #F3 = st.image([])
   #F4 = st.image([])
  #http://192.168.29.220:81/stream
  camera = cv2.VideoCapture(0)
  detection = False
  frame_count = 0
  _, image_video = video_augment.read()
  if st.button("REMOVE BACKGROUND"):
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
