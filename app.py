import streamlit as st
import time
import pandas as pd

st.title("TapStoic")

st.sidebar.markdown("**About the App:** Train to Increase *Attention Accuracy* during *Emotion turmoil* Can provide a time-window in *Real-Life* High-stakes Situations")
st.sidebar.markdown("Step-wise instructions: 1. Record your thought that is looping inside your mind; 2. Play it and point the cursor on Tap button; 3. Close your eyes and Tap at the start of each Inspiration till the record is playing")

st.header("Tap Interval Timer")
st.subheader("Tap on start of each Inspiration")

# Initialize session state variables
if 'last_tap_time' not in st.session_state:
    st.session_state.last_tap_time = None
if 'intervals' not in st.session_state:
    st.session_state.intervals = []


# Record audio from the user's microphone
audio_file = st.audio_input("Record a voice message")

# If an audio file is recorded, display the playback
if audio_file:
    st.audio(audio_file)

# Tap Button
if st.button("Tap"):
    current_time = time.time()
    
    # Calculate interval if a previous tap exists
    if st.session_state.last_tap_time is not None:
        interval = current_time - st.session_state.last_tap_time
        st.session_state.intervals.append(interval)
        st.success(f"Interval: {interval:.2f} seconds")
    else:
        st.info("First tap recorded. Tap again to measure interval.")
        
    # Update the last tap time
    st.session_state.last_tap_time = current_time

# Display data
if st.session_state.intervals:
    df = pd.DataFrame(st.session_state.intervals, columns=["Intervals_Seconds"])
   
# User can Stop the training by pressin STOP button.
if st.button("STOP"):
    st.session_state.last_tap_time = None
    st.session_state.intervals = []
    st.bar_chart(df.iloc[1:-1])  # To exclude first Two and last interval from Chart
    st.line_chart(df.iloc[1:-1])  # To exclude first Two and last interval from Chart
    st.dataframe(df) # Of all the data without exclusion 
    st.table(df.iloc[1:-1].describe()) #To exclude first Two and last interval from Analysis