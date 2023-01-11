import streamlit as st
import datetime


# make any grid with a function
def make_grid(cols, rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid


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

places_state = {
    # make 25 elements of dict false, and 5 true
    1: False, 2: True, 3: False, 4: False, 5: False, 6: False, 7: True, 8: False, 9: False, 10: True,
    11: False, 12: False, 13: True, 14: False, 15: False, 16: False, 17: False, 18: False, 19: False, 20: False,
    21: False, 22: False, 23: False, 24: False, 25: False, 26: True, 27: False, 28: False, 29: True, 30: True,
}

booking_type = st.radio(
    "Что хотите забронировать?",
    ('Компьютер', 'Консоль', 'Бильярд'))

if booking_type == 'Компьютер':
    place_selector = make_grid(6, 5)
    place_number = 0

    for i in range(6):
        for j in range(5):
            place_number += 1

            if places_state[place_number]:
                place_selector[i][j].button(f"{place_number}", disabled=True, help="Это место уже забронировано")
            else:
                place_selector[i][j].button(f"{place_number}",
                                            on_click=handle_user_selection,
                                            args=(f"Компьютер №{place_number}",),
                                            help="Чтобы выбрать место - нажмите на него")

elif booking_type == 'Консоль':
    place_selector = make_grid(cols=2, rows=1)
    place_selector[0][0].button("Красные геймпады", on_click=handle_user_selection, args=("Красные геймпады",))
    place_selector[1][0].button("Черные геймпады", on_click=handle_user_selection, args=("Черные геймпады",))

else:
    place_selector = make_grid(cols=3, rows=1)
    place_selector[0][0].button("Русский бильярд", on_click=handle_user_selection, args=("Русский бильярд",))
    place_selector[1][0].button("Дагистанский бильярд", on_click=handle_user_selection, args=("Дагистанский бильярд",))
    place_selector[2][0].button("Нурминский бильярд", on_click=handle_user_selection, args=("Нурминский бильярд",))


# Exit button
# st.button('Забронировать', key='stop', on_click=handle_user_selection)
