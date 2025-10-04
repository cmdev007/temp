import streamlit as st
from datetime import datetime, timedelta
import time
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Ritika's Birthday Countdown 🎉",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Background */
    .main {
        background: linear-gradient(135deg, #FF6B9D 0%, #C06C84 25%, #6C5B7B 50%, #355C7D 100%);
        animation: gradientShift 15s ease infinite;
        background-size: 400% 400%;
    }
    .stApp {
        background: linear-gradient(135deg, #FF6B9D 0%, #C06C84 25%, #6C5B7B 50%, #355C7D 100%);
        animation: gradientShift 15s ease infinite;
        background-size: 400% 400%;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Floating particles */
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
    }

    /* Title styling */
    .title-font {
        font-size: 72px !important;
        font-weight: 900;
        color: #FFFFFF;
        text-align: center;
        text-shadow: 4px 4px 8px rgba(0,0,0,0.4);
        margin-bottom: 10px;
        font-family: 'Arial Black', sans-serif;
        letter-spacing: 2px;
        animation: titleGlow 2s ease-in-out infinite;
    }

    @keyframes titleGlow {
        0%, 100% { text-shadow: 4px 4px 8px rgba(0,0,0,0.4), 0 0 20px rgba(255,255,255,0.3); }
        50% { text-shadow: 4px 4px 8px rgba(0,0,0,0.4), 0 0 40px rgba(255,255,255,0.6); }
    }

    /* Countdown container */
    .countdown-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: 40px 0;
        flex-wrap: wrap;
    }

    .countdown-box {
        background: rgba(255, 255, 255, 0.15);
        border-radius: 25px;
        padding: 35px 25px;
        margin: 10px;
        backdrop-filter: blur(15px);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37),
                    inset 0 0 20px rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(255, 255, 255, 0.18);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        min-width: 150px;
    }

    .countdown-box:hover {
        transform: translateY(-10px) scale(1.05);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.5),
                    inset 0 0 30px rgba(255, 255, 255, 0.2);
    }

    .countdown-number {
        font-size: 80px;
        font-weight: 900;
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        font-family: 'Arial Black', sans-serif;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        margin: 0;
        line-height: 1;
    }

    .countdown-label {
        font-size: 26px;
        color: #FFFFFF;
        text-align: center;
        font-weight: 600;
        margin-top: 10px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Birthday message */
    .birthday-message {
        font-size: 56px;
        background: linear-gradient(135deg, #FFD700 0%, #FF69B4 50%, #FFD700 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        font-weight: 900;
        animation: rainbow 3s ease-in-out infinite, bounce 1s ease-in-out infinite;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin: 30px 0;
    }

    @keyframes rainbow {
        0%, 100% { filter: hue-rotate(0deg); }
        50% { filter: hue-rotate(30deg); }
    }

    @keyframes bounce {
        0%, 100% { transform: scale(1) translateY(0); }
        50% { transform: scale(1.1) translateY(-10px); }
    }

    .age-text {
        font-size: 38px;
        color: #FFFFFF;
        text-align: center;
        margin: 30px 0;
        font-weight: 700;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.3);
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        display: inline-block;
        width: 100%;
    }

    /* Wishes section */
    .wishes-container {
        background: rgba(255, 255, 255, 0.12);
        border-radius: 25px;
        padding: 40px;
        margin: 40px auto;
        max-width: 800px;
        backdrop-filter: blur(15px);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 2px solid rgba(255, 255, 255, 0.18);
    }

    .wishes-text {
        font-size: 28px;
        color: #FFFFFF;
        text-align: center;
        line-height: 1.6;
        font-weight: 500;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }

    /* Decorative elements */
    .sparkle {
        display: inline-block;
        animation: sparkle 1.5s ease-in-out infinite;
    }

    @keyframes sparkle {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(1.2); }
    }
    </style>
""", unsafe_allow_html=True)

# Add decorative header with pandas
st.markdown('<p class="title-font"><span class="sparkle">✨</span> 🐼 Ritika\'s Birthday Countdown 🐼 <span class="sparkle">✨</span></p>', unsafe_allow_html=True)

# Birth date
birth_date = datetime(1999, 10, 11)

# Calculate next birthday
today = datetime.now()
current_year = today.year

# Determine next birthday
next_birthday = datetime(current_year, 10, 11)
if today > next_birthday:
    next_birthday = datetime(current_year + 1, 10, 11)

# Calculate age
age = next_birthday.year - birth_date.year

# Calculate time remaining
time_remaining = next_birthday - today

# Check if it's birthday today
if time_remaining.days == 0 and time_remaining.seconds < 86400:
    st.balloons()
    st.markdown('<p class="birthday-message">🐼 HAPPY BIRTHDAY RITIKA! 🐼</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="birthday-message">Welcome to {age}! 🐼🎂🎈🎁</p>', unsafe_allow_html=True)

    # Celebration animation
    for _ in range(3):
        st.balloons()
        time.sleep(0.5)
else:
    # Display countdown
    days = time_remaining.days
    hours = time_remaining.seconds // 3600
    minutes = (time_remaining.seconds % 3600) // 60
    seconds = time_remaining.seconds % 60

    st.markdown(f'<p class="age-text">🐼 Turning Sweet {age} on October 11, {next_birthday.year} 🐼</p>', unsafe_allow_html=True)

    # Add spacing
    st.markdown("<br>", unsafe_allow_html=True)

    # Create columns for countdown
    col1, col2, col3, col4 = st.columns(4, gap="large")

    with col1:
        st.markdown(f'''
            <div class="countdown-box">
                <p class="countdown-number">{days:02d}</p>
                <p class="countdown-label">Days</p>
            </div>
        ''', unsafe_allow_html=True)

    with col2:
        st.markdown(f'''
            <div class="countdown-box">
                <p class="countdown-number">{hours:02d}</p>
                <p class="countdown-label">Hours</p>
            </div>
        ''', unsafe_allow_html=True)

    with col3:
        st.markdown(f'''
            <div class="countdown-box">
                <p class="countdown-number">{minutes:02d}</p>
                <p class="countdown-label">Minutes</p>
            </div>
        ''', unsafe_allow_html=True)

    with col4:
        st.markdown(f'''
            <div class="countdown-box">
                <p class="countdown-number">{seconds:02d}</p>
                <p class="countdown-label">Seconds</p>
            </div>
        ''', unsafe_allow_html=True)

# Add spacing
st.markdown("<br><br>", unsafe_allow_html=True)

# Birthday wishes section with pandas
st.markdown("""
    <div class="wishes-container">
        <p class="wishes-text">
            <span class="sparkle">🐼</span> Get ready for an amazing celebration! <span class="sparkle">🐼</span>
        </p>
        <p class="wishes-text" style="margin-top: 20px;">
            🎁 May this year bring you endless joy, incredible success, and beautiful memories! 🎁
        </p>
        <p class="wishes-text" style="margin-top: 20px; font-size: 32px;">
            🐼 Let's make it unforgettable! 🐼
        </p>
    </div>
""", unsafe_allow_html=True)

# Add pandas dataframe with birthday milestones
st.markdown("<br>", unsafe_allow_html=True)

# Create milestone data
milestones_data = {
    '🎯 Milestone': ['Birth Year', 'Sweet 16', 'Legal Adult', 'Quarter Century', 'Current Age'],
    '📅 Year': [1999, 2015, 2017, 2024, next_birthday.year],
    '🎂 Age': [0, 16, 18, 25, age],
    '✨ Special': ['Born! 👶', 'Sweet Sixteen 💖', 'Adult Life Begins 🎓', 'Quarter Century 🌟', 'This Birthday! 🎉']
}

df_milestones = pd.DataFrame(milestones_data)

st.markdown('<h2 style="text-align: center; color: white; font-size: 42px; margin-top: 40px;">🐼 Ritika\'s Birthday Milestones 🐼</h2>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Style the dataframe
st.dataframe(
    df_milestones,
    use_container_width=True,
    hide_index=True,
    column_config={
        '🎯 Milestone': st.column_config.TextColumn(width='medium'),
        '📅 Year': st.column_config.NumberColumn(width='small', format='%d'),
        '🎂 Age': st.column_config.NumberColumn(width='small'),
        '✨ Special': st.column_config.TextColumn(width='medium')
    }
)

# Add countdown statistics using pandas
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; color: white; font-size: 42px; margin-top: 20px;">🐼 Countdown Statistics 🐼</h2>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Calculate various time units
total_seconds = time_remaining.total_seconds()
stats_data = {
    '⏰ Time Unit': ['Total Seconds', 'Total Minutes', 'Total Hours', 'Total Days', 'Weeks Left'],
    '🔢 Count': [
        int(total_seconds),
        int(total_seconds / 60),
        int(total_seconds / 3600),
        time_remaining.days,
        round(time_remaining.days / 7, 1)
    ]
}

df_stats = pd.DataFrame(stats_data)

# Display stats in columns
col_stat1, col_stat2 = st.columns(2)

with col_stat1:
    st.dataframe(
        df_stats,
        use_container_width=True,
        hide_index=True,
        column_config={
            '⏰ Time Unit': st.column_config.TextColumn(width='medium'),
            '🔢 Count': st.column_config.NumberColumn(width='medium', format='%d')
        }
    )

with col_stat2:
    # Create a chart showing countdown progress
    chart_data = pd.DataFrame({
        'Unit': ['Days', 'Hours', 'Minutes', 'Seconds'],
        'Value': [days, hours, minutes, seconds]
    })
    st.bar_chart(chart_data.set_index('Unit'), color='#FFD700')

# Auto-refresh every second
time.sleep(1)
st.rerun()
