import streamlit as st
import time
from datetime import datetime, timezone, timedelta


def app():
    st.title("Clara's Countdown")

    # set the end date to February 24, 2023 at 6:30 PM in Hong Kong time
    end_date = datetime(2023, 2, 24, 18, 30, tzinfo=timezone(timedelta(hours=8)))
    st.write(f"Counting down to: {end_date}")

    remaining_time_text_seconds = st.empty()
    remaining_time_text_ms = st.empty()
    remaining_time_text_min = st.empty()

    while True:
        current_time = datetime.now(timezone.utc).astimezone(
            timezone(timedelta(hours=8))
        )
        remaining_time = end_date - current_time
        remaining_seconds = remaining_time.total_seconds()
        remaining_milliseconds = int(remaining_seconds * 1000)
        remaining_minutes = int(remaining_seconds // 60)
        # remaining_seconds = int(remaining_seconds % 60)

        if remaining_seconds <= 0:
            remaining_time_text_seconds.write("Time's up!")
            break

        remaining_time_text_seconds.write("Remaining time:", unsafe_allow_html=True)
        # st.text("")  # add some vertical space between lines
        remaining_time_text_min.write(
            f"{remaining_minutes} min", unsafe_allow_html=True
        )
        # st.text("")  # add some vertical space between lines
        remaining_time_text_seconds.write(
            f"{remaining_seconds} sec", unsafe_allow_html=True
        )
        remaining_time_text_ms.write(
            f"{remaining_milliseconds} ms", unsafe_allow_html=True
        )
        time.sleep(0.1)  # update the timer every 100 milliseconds


if __name__ == "__main__":
    app()
