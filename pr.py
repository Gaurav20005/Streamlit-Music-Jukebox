import streamlit as st
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Set the directory for the music files
MUSIC_FOLDER = "D:/Data Science"  # Update with your actual folder path

# Supported audio formats for playback
SUPPORTED_FORMATS = ('.mp3', '.wav', '.ogg')

# Check if the directory exists and show an error if not
if not os.path.exists(MUSIC_FOLDER):
    st.error("The specified music folder was not found. Please update the MUSIC_FOLDER variable to a valid path.")
else:
    os.chdir(MUSIC_FOLDER)

    # Function to load and play the selected track
    def start_playback(track):
        st.session_state["current_song"] = track
        st.session_state["play_status"] = "Playing"
        pygame.mixer.music.load(track)  # Load the selected track
        pygame.mixer.music.play()

    # Function to stop the track
    def halt_playback():
        st.session_state["play_status"] = "Stopped"
        pygame.mixer.music.stop()

    # Function to pause the track
    def pause_playback():
        st.session_state["play_status"] = "Paused"
        pygame.mixer.music.pause()

    # Function to resume the paused track
    def resume_playback():
        st.session_state["play_status"] = "Playing"
        pygame.mixer.music.unpause()

    # Initialize session state variables if not already present
    if "current_song" not in st.session_state:
        st.session_state["current_song"] = ""
    if "play_status" not in st.session_state:
        st.session_state["play_status"] = ""

    # Set the page title and header
    st.markdown("<h1 style='color: #3498db;'>Streamlit Music Jukebox</h1>", unsafe_allow_html=True)

    # Display the current song and status
    st.markdown(f"<h3>Currently Playing: <span style='color: #e74c3c;'>{st.session_state['current_song']}</span></h3>", unsafe_allow_html=True)
    st.text(f"Status: {st.session_state['play_status']}")

    # Load and filter the list of tracks based on valid formats
    available_tracks = [track for track in os.listdir(MUSIC_FOLDER) if track.endswith(SUPPORTED_FORMATS)]

    if available_tracks:
        # Dropdown menu for song selection
        chosen_song = st.selectbox("Pick a track to play", available_tracks)

        # Control buttons layout with colors and alignment
        play_col, pause_col, resume_col, stop_col = st.columns(4)

        if play_col.button("🎶 Play", key="play_button", help="Play the selected song"):
            start_playback(chosen_song)

        if pause_col.button("⏸ Pause", key="pause_button", help="Pause the song"):
            pause_playback()

        if resume_col.button("▶️ Resume", key="resume_button", help="Resume the paused song"):
            resume_playback()

        if stop_col.button("🛑 Stop", key="stop_button", help="Stop the song"):
            halt_playback()

    else:
        st.error("No playable audio tracks found in the specified folder.")
