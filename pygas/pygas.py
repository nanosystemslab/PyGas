from typing import Optional

import serial


class AlicatFlow:
    """
    Represents an interface to control Alicat flow meters.
    """

    def __init__(self, port: str = "/dev/tty.usbserial-AU0585NK", baudrate: int = 19200) -> None:
        """
        Initializes the AlicatFlow object.

        Args:
            port (str): The serial port to communicate with the device.
            baudrate (int): The baud rate for serial communication.
        """
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(
            self.port,
            self.baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0,
        )

    def start_stream(self, unit_id: str) -> None:
        """
        Starts streaming data from the device.

        Args:
            unit_id (str): The ID of the unit.
        """
        try:
            self.ser.write(f"{unit_id}@ @\r".encode())
        except Exception as e:
            print(f"Error starting stream: {e}")

    def poll_data(self, unit_id: str) -> Optional[str]:
        """
        Polls data for the specified unit.

        Args:
            unit_id (str): The ID of the unit.

        Returns:
            Optional[str]: The response message from the device.
        """
        try:
            self.ser.write(f"{unit_id}\r".encode())
            msg: str = ""
            count: int = 0
            while msg == "":
                data: bytes = self.ser.readline()
                count += 1
                data_str = data.decode(errors="ignore")
                if f"{unit_id}" in data_str and "\r" in data_str:
                    msg = data_str
                    print(msg)
                if count == 10:
                    print("No response received within the expected timeframe.")
                    return None
            else:
                return msg
        except Exception as e:
            print(f"Error polling data: {e}")
            return None
        return None

    def stop_stream(self, unit_id: str) -> None:
        """
        Stops streaming data from the device.

        Args:
            unit_id (str): The ID of the unit.
        """
        try:
            self.ser.write(f"@@ {unit_id}\r".encode())
        except Exception as e:
            print(f"Error stopping stream: {e}")

    def tare(self, unit_id: str) -> None:
        """
        Performs taring on the device.

        Args:
            unit_id (str): The ID of the unit.
        """
        try:
            self.ser.write(f"{unit_id}V\r".encode())
        except Exception as e:
            print(f"Error taring: {e}")

    def available_gases(self, unit_id: str) -> Optional[str]:
        """
        Queries available gases from the device.

        Args:
            unit_id (str): The ID of the unit.

        Returns:
            Optional[str]: The queried data.
        """
        try:
            self.ser.write(f"{unit_id}??G*\r".encode())
            msg = ""
            count = 0
            while msg == "":
                data = self.ser.readline()
                count += 1
                data_str: str = data.decode(errors="ignore")

                if (f"{unit_id}" in data_str) and ("\r" in data_str):
                    msg = msg + data_str
                    return msg
                elif count == 5:
                    count = 0
                    self.ser.write(f"{unit_id}??G*\r".encode())
        except Exception as e:
            print(f"Error querying available gases: {e}")
            return None
        return None

    def change_gas(self, unit_id: str, gas_num: str) -> Optional[str]:
        """
        Changes the gas type for the specified unit.

        Args:
            unit_id (str): The ID of the unit.
            gas_num (str): The gas number to be set.

        Returns:
            Optional[str]: The response message from the device.
        """
        try:
            self.ser.write(f"{unit_id}G {gas_num}\r".encode())
            msg = ""
            count = 0
            while msg == "":
                data = self.ser.readline()
                count += 1
                data_str: str = data.decode(errors="ignore")  # Decode data to string
                if len(data_str) > 3:
                    msg = msg + data_str
                    return msg
                elif count == 5:
                    count = 0
                    self.ser.write(f"{unit_id}G {gas_num}\r".encode())
        except Exception as e:
            print(f"Error changing gas: {e}")
            return None
        return None

    def lock_display(self, unit_id: str) -> None:
        """
        Locks the display of the specified unit.

        Args:
            unit_id (str): The ID of the unit.
        """
        try:
            self.ser.write(f"{unit_id}L\r".encode())
        except Exception as e:
            print(f"Error locking display: {e}")

    def unlock_display(self, unit_id: str) -> None:
        """
        Unlocks the display of the specified unit.

        Args:
            unit_id (str): The ID of the unit.
        """
        try:
            self.ser.write(f"{unit_id}U\r".encode())
        except Exception as e:
            print(f"Error unlocking display: {e}")

    def read_stream(self) -> None:
        """
        Reads and prints the streaming data from the device.
        """
        try:
            msg = ""
            while 1:
                data = self.ser.readline()
                if len(data) > 0:
                    msg = msg + data.decode()
                    if "\r" in msg:
                        print(msg)
        except Exception as e:
            print(f"Error reading stream: {e}")

    def set_units(
        self, unit_id: str, static_value: str, unit_value: str, group: str = "1", override: str = "0"
    ) -> Optional[str]:
        """
        Sets the units for the specified unit.

        Args:
            unit_id (str): The ID of the unit.
            static_value (str): The static value to set.
            unit_value (str): The unit value to set.
            group (str, optional): The group value. Defaults to "1".
            override (str, optional): The override value. Defaults to "0".

        Returns:
            Optional[str]: The response message from the device.
        """
        try:
            self.ser.write(f"{unit_id}DCU {static_value} {group} {unit_value} {override}\r".encode())
            msg = ""
            count = 0
            while msg == "":
                data = self.ser.readline()
                count += 1
                data = data.decode(errors="ignore")
                if len(data) > 3:
                    msg = msg + data
                    return msg
                elif count == 5:
                    count = 0
                    self.ser.write(f"{unit_id}DCU {static_value} {group} {unit_value} {override}\r".encode())
        except Exception as e:
            print(f"Error setting units: {e}")
            return None
        return None

    def query_unit_val_static(self, unit_id: str) -> Optional[str]:
        """
        Queries the static unit value for the specified unit.

        Args:
            unit_id (str): The ID of the unit.

        Returns:
            Optional[str]: The response message from the device.
        """
        try:
            self.ser.write(f"{unit_id}DCU 69\r".encode())
            msg = ""
            count = 0
            while msg == "":
                data = self.ser.readline()
                count += 1
                data = data.decode(errors="ignore")
                print(data)
                if len(data) >= 10:
                    msg = msg + data
                    return msg
                elif count == 5:
                    count = 0
                    self.ser.write(f"{unit_id}DCU 5\r".encode())
        except Exception as e:
            print(f"Error querying static unit value: {e}")
            return None

    def baud_rate(self, unit_id: str) -> None:
        """
        Sets the baud rate for the specified unit.

        Args:
            unit_id (str): The ID of the unit.
        """
        try:
            self.ser.write(f"{unit_id}NCB {self.baudrate}\r".encode())
        except Exception as e:
            print(f"Error setting baud rate: {e}")

    def change_unit_id(self, unit_id: str, new_unit_id: str) -> None:
        """
        Changes the unit ID of the specified unit.

        Args:
            unit_id (str): The current ID of the unit.
            new_unit_id (str): The new ID to set for the unit.
        """
        try:
            self.ser.write(f"{unit_id}@ {new_unit_id}\r".encode())
        except Exception as e:
            print(f"Error changing unit ID: {e}")


class AlicatPressure:
    def __init__(self, port: str = "/dev/tty.usbserial-AU0585NK", baudrate: int = 19200) -> None:
        """
        Initializes an AlicatPressure object.

        Args:
            port (str, optional): The serial port to connect to. Defaults to "/dev/tty.usbserial-AU0585NK".
            baudrate (int, optional): The baud rate for the serial communication. Defaults to 19200.
        """
        self.port: str = port
        self.baudrate: int = baudrate
        self.psia: str = ""
        self.temp: str = ""
        self.volum_flow: str = ""
        self.mass_flow: str = ""
        self.gas: str = ""
        self.ser: serial.Serial = serial.Serial(
            self.port,
            self.baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0,
        )

    def start_stream(self, unit_id: str) -> None:
        """
        Starts streaming data for the specified unit.

        Args:
            unit_id (str): The ID of the unit.
        """
        self.ser.write(f"{unit_id}@=@\r".encode())

    def stop_stream(self, unit_id: str) -> None:
        """
        Stops streaming data for the specified unit.

        Args:
            unit_id (str): The ID of the unit.
        """
        self.ser.write(f"@@={unit_id}\r".encode())

    def tare(self, unit_id: str) -> None:
        """
        Tares the specified unit.

        Args:
            unit_id (str): The ID of the unit.
        """
        self.ser.write(f"{unit_id}PC\r".encode())

    def read_stream(self) -> None:
        """Reads the streaming data."""
        msg: str = ""
        while 1:
            data: bytes = self.ser.readline()
            if len(data) > 0:
                msg = msg + data.decode(errors="ignore")
                if "\r" in msg:
                    print(msg)

    def poll_data(self, unit_id: str) -> Optional[str]:
        """
        Polls data for the specified unit.

        Args:
            unit_id (str): The ID of the unit.

        Returns:
            Optional[str]: The response message from the device.
        """
        try:
            self.ser.write(f"{unit_id}\r".encode())
            msg: str = ""
            count: int = 0
            while msg == "":
                data: bytes = self.ser.readline()
                count += 1
                data_str = data.decode(errors="ignore")
                if f"{unit_id}" in data_str and "\r" in data_str:
                    msg = data_str
                    print(msg)
                if count == 10:
                    print("No response received within the expected timeframe.")
                    return None
            else:
                return msg
        except Exception as e:
            print(f"Error polling data: {e}")
            return None
        return None

    def set_units(self, unit_id: str) -> Optional[str]:
        """
        Sets the units for the specified unit.

        Args:
            unit_id (str): The ID of the unit.

        Returns:
            Optional[str]: The response message from the device.
        """
        try:
            self.ser.write(f"{unit_id}DCU 2 61 700 0\r".encode())
            msg: str = ""
            count: int = 0
            while msg == "":
                data: bytes = self.ser.readline()
                data = data.decode(errors="ignore")
                if (f"{unit_id}" in data) and ("\r" in data):
                    msg = msg + data
                    if "\r" in msg:
                        print(msg)
                elif count == 10:
                    self.ser.write(f"{unit_id}DCU 2 61 700 0\r".encode())
            else:
                return msg
        except Exception as e:
            print(f"Error setting units: {e}")
            return None
        return None


if __name__ == "__main__":
    alicat_flow = AlicatFlow()  # Corrected instantiation
    unit_id: str = input("Current unit_id: ")
    alicat_flow.stop_stream(unit_id)
    gas_num: str = input("Gas num: ")
    alicat_flow.change_gas(unit_id, gas_num)
    data: Optional[str] = alicat_flow.poll_data(unit_id)
    print(data)
