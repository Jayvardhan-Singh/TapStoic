import streamlit as st
import time
import pandas as pd

st.set_page_config(
    page_title= "TapStoic",
    initial_sidebar_state= 'expanded',
    menu_items={
        "About": 'Training to Increase *Attention Accuracy* during *Emotion turmoil* Can provide a time-window in *Real-Life* High-stakes Situations'
    }
)

st.title("TapStoic")

with st.sidebar:
    side = st.radio("Select the Stage: ", ["Stage 1: Simple Tap", "Stage 2: Skip 5th", "Stage 3: Audio", "Stage 4: Visual", "Stage 5: Audio + Visual"])

# Initialize session state variables
if 'last_tap_time' not in st.session_state:
    st.session_state.last_tap_time = None
if 'intervals' not in st.session_state:
    st.session_state.intervals = []

###############################################################################################
###############################################################################################
if side == "Stage 1: Simple Tap":
    st.header("Tap Interval Timer")
    st.markdown("Step-wise instructions: 1. Point the cursor on Tap button. 2. Close your eyes and Tap at the start of each Inspiration. 3. Press the Stop Button to end the session.")

    if st.button("TAP", width='stretch'):
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
    if st.button("STOP", width='stretch'):
        st.session_state.last_tap_time = None
        st.session_state.intervals = []
        st.bar_chart(df.iloc[1:-1])  # To exclude first Two and last interval from Chart
        st.line_chart(df.iloc[1:-1])  # To exclude first Two and last interval from Chart
        st.dataframe(df) # Of all the data without exclusion 
        st.table(df.iloc[1:-1].describe()) #To exclude first Two and last interval from Analysis

###############################################################################################
###############################################################################################
elif side == "Stage 2: Skip 5th":
    st.header("Tap Interval Timer")
    st.markdown("Step-wise instructions: 1. Point the cursor on Tap button. 2. Close your eyes and Tap at the start of Inspiration. 3. Skip Tap on each 5th Inspiration. 4. Press the Stop Button to end the session.")

    if st.button("TAP", width='stretch'):
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
    if st.button("STOP", width='stretch'):
        st.session_state.last_tap_time = None
        st.session_state.intervals = []
        st.bar_chart(df.iloc[1:-1])  # To exclude first Two and last interval from Chart
        st.line_chart(df.iloc[1:-1])  # To exclude first Two and last interval from Chart
        st.dataframe(df) # Of all the data without exclusion 
        st.table(df.iloc[1:-1].describe()) #To exclude first Two and last interval from Analysis
###############################################################################################
###############################################################################################
elif side == "Stage 3: Audio":
    st.header("Tap Interval Timer Stage 3")
    st.markdown("Step-wise instructions: 1. Record the thought which is looping inside your mind by pressing the record button. 2. Stop the recording and then play it. 3. While the record is playing Tap at the start of each Inspiration and Keep skipping each 5th Breath like that of stage 2. Press the Stop Button to end the session.")

    # Record audio from the user's microphone
    audio_file = st.audio_input("Record a voice message of the thought that is looping inside your mind")
    # If an audio file is recorded, display the playback
    if audio_file:
        st.audio(audio_file)

    if st.button("TAP", width='stretch'):
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
    if st.button("STOP", width='stretch'):
        st.session_state.last_tap_time = None
        st.session_state.intervals = []
        st.bar_chart(df.iloc[1:-1])  # To exclude first Two and last interval from Chart
        st.line_chart(df.iloc[1:-1])  # To exclude first Two and last interval from Chart
        st.dataframe(df) # Of all the data without exclusion 
        st.table(df.iloc[1:-1].describe()) #To exclude first Two and last interval from Analysis
###############################################################################################
###############################################################################################
elif side == "Stage 4: Visual":
    st.header("Tap Interval Timer Stage 4")
    st.markdown("Step-wise instructions: 1. Upload the image which is looping inside your mind 2. Watch the image, Point the curson on the Tap Button and then close your eyes. 3. Tap at the start of each Inspiration and Keep skipping each 5th Breath like that of stage 2. Press the Stop Button to end the session.")

    # Upload an image
    image = st.file_uploader("Upload an image which is causing emotional turmoil", type = ['jpg', 'jpeg', 'png'])
    if image:
        st.image(image = image)

    if st.button("TAP", width='stretch'):
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
    if st.button("STOP", width='stretch'):
        st.session_state.last_tap_time = None
        st.session_state.intervals = []
        st.bar_chart(df.iloc[1:-1])  # To exclude first Two and last interval from Chart
        st.line_chart(df.iloc[1:-1])  # To exclude first Two and last interval from Chart
        st.dataframe(df) # Of all the data without exclusion 
        st.table(df.iloc[1:-1].describe()) #To exclude first Two and last interval from Analysis
###############################################################################################
###############################################################################################
else:
    st.header("Tap Interval Timer Stage 5")
    st.markdown("Step-wise instructions: 1. Upload the image like Stage 4 2. Record the Audio as Stage 3 3. Tap at the start of each Inspiration and Keep skipping each 5th Breath like that of stage 2. Press the Stop Button to end the session.")

    # Upload an image
    image = st.file_uploader("Upload an image which is causing emotional turmoil", type = ['jpg', 'jpeg', 'png'])
    if image:
        st.image(image = image)

    # Record audio from the user's microphone
    audio_file = st.audio_input("Record a voice message of the thought that is looping inside your mind")
    # If an audio file is recorded, display the playback
    if audio_file:
        st.audio(audio_file)

    if st.button("TAP", width='stretch'):
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
    if st.button("STOP", width='stretch'):
        st.session_state.last_tap_time = None
        st.session_state.intervals = []
        st.bar_chart(df.iloc[1:-1])  # To exclude first Two and last interval from Chart
        st.line_chart(df.iloc[1:-1])  # To exclude first Two and last interval from Chart
        st.dataframe(df) # Of all the data without exclusion 
        st.table(df.iloc[1:-1].describe()) #To exclude first Two and last interval from Analysis
###############################################################################################
###############################################################################################