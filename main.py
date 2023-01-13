import streamlit as st
import datetime
from device_selector import DeviceSelector


# handle user selection
def handle_user_selection(selected_place: int):
    booking_end_time = datetime.timedelta(hours=booking_start_time.hour, minutes=booking_start_time.minute) \
                       + datetime.timedelta(hours=booking_time.hour, minutes=booking_time.minute)

    # print(f"{booking_start_time } \n{booking_time }\n{booking_end_time }")
    st.success(
        f"Вы забронировали {selected_place} на {date} с {booking_start_time} на {booking_end_time}",
        icon="✅"
    )


st.title("Бронирование")

# Input field for name
today = datetime.date.today()
date = st.date_input("Дата бронирования", datetime.date(today.year, today.month, today.day))

booking_start_time = st.time_input("Время начала бронирования", datetime.time(9, 0))

# Booking slider
min_booking_time = datetime.time(1, 0)
max_booking_time = datetime.time(2, 0)
step = datetime.timedelta(minutes=15)
booking_time = st.slider(
    "Сколько времени забронировать",
    min_value=min_booking_time,
    max_value=max_booking_time,
    step=step,
)

# Select device
device_selector = DeviceSelector()

st.button('Забронировать', key='stop', on_click=handle_user_selection)