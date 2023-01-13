import streamlit as st
from config_loader import ConfigLoader


def make_grid(cols, rows):
    """
    Function for creating a grid for elements.

    @param cols: number of columns
    @param rows: number of rows
    @return: list of lists with elements
    """
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid


class DeviceSelector:
    def __init__(self):
        self.config = ConfigLoader()

        # TODO: change mock to api data
        self.places_state = {
            1: False, 2: True, 3: False, 4: False, 5: False, 6: False, 7: True, 8: False, 9: False, 10: True,
            11: False, 12: False, 13: True, 14: False, 15: False, 16: False, 17: False, 18: False, 19: False, 20: False,
            21: False, 22: False, 23: False, 24: False, 25: False, 26: True, 27: False, 28: False, 29: True, 30: True,
        }

        selected_device = self.devices_selection()
        self.devices_view(selected_device)

    def devices_selection(self):
        devices = self.config.get_keys_specified('booking_services')
        booking_type = st.radio(
            "Что хотите забронировать?",
            # insert devices into tuple
            devices
        )
        return booking_type

    def devices_view(self, selected_device: str):
        """
        Function for displaying devices.

        @param selected_device: name of device
        """

        if selected_device is None:
            print("No device selected")
            return
        elif selected_device == 'pc':
            place_selector = make_grid(cols=6, rows=5)
            place_number = 0

            for i in range(6):
                for j in range(5):
                    place_number += 1

                    if self.places_state[place_number]:
                        place_selector[i][j].button(
                            f"{place_number}",
                            disabled=True,
                            help="Это место уже забронировано"
                        )
                    else:
                        place_selector[i][j].button(
                            f"{place_number}",
                            args=(f"Компьютер №{place_number}",),
                            help="Чтобы выбрать место - нажмите на него"
                        )

        elif selected_device == 'console':
            place_selector = make_grid(cols=2, rows=1)
            place_selector[0][0].button("Красные геймпады", args=("Красные геймпады",))
            place_selector[1][0].button("Черные геймпады", args=("Черные геймпады",))

        elif selected_device == 'billiard':
            place_selector = make_grid(cols=3, rows=1)
            place_selector[0][0].button("Русский бильярд", args=("Русский бильярд",))
            place_selector[1][0].button("Американский бильярд", args=("Американский бильярд",))
            place_selector[2][0].button("Нурминский бильярд", args=("Нурминский бильярд",))
