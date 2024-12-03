"""Unit tests for Pygassed Lbrary."""

from typing import Any

import pytest
import serial

from unittest.mock import MagicMock
from unittest.mock import patch

from pygassed.pygassed import AlicatFlow
from pygassed.pygassed import AlicatPressure


@pytest.fixture
def mock_serial() -> Any:
    with patch("pygassed.pygassed.serial.Serial") as mock_serial:
        yield mock_serial


@pytest.fixture
def alicat_flow(mock_serial: Any) -> Any:
    return AlicatFlow()


@pytest.fixture
def alicat_pressure(mock_serial: Any) -> AlicatPressure:
    return AlicatPressure()


# AlicatFlow Tests
def test_alicat_flow_init(mock_serial: Any) -> None:
    alicat = AlicatFlow(port="/dev/test", baudrate=9600)
    mock_serial.assert_called_once_with(
        "/dev/test",
        9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0,
    )


def test_alicat_flow_start_stream(alicat_flow: Any, mock_serial: Any) -> None:
    unit_id = "A1"
    alicat_flow.start_stream(unit_id)
    mock_serial.return_value.write.assert_called_once_with(f"{unit_id}@ @\r".encode())


def test_alicat_flow_poll_data(alicat_flow: Any, mock_serial: Any) -> None:
    unit_id = "A1"
    mock_serial.return_value.readline.side_effect = [
        b"", b"", b"", f"{unit_id} data\r".encode()
    ]
    result = alicat_flow.poll_data(unit_id)
    assert result == f"{unit_id} data\r"
    mock_serial.return_value.write.assert_called_once_with(f"{unit_id}\r".encode())


def test_alicat_flow_stop_stream(alicat_flow: Any, mock_serial: Any) -> None:
    unit_id = "A1"
    alicat_flow.stop_stream(unit_id)
    mock_serial.return_value.write.assert_called_once_with(f"@@ {unit_id}\r".encode())


def test_alicat_flow_tare(alicat_flow: Any, mock_serial: Any) -> None:
    unit_id = "A1"
    alicat_flow.tare(unit_id)
    mock_serial.return_value.write.assert_called_once_with(f"{unit_id}V\r".encode())


def test_alicat_flow_available_gases(alicat_flow: Any, mock_serial: Any) -> None:
    unit_id = "A1"
    mock_serial.return_value.readline.side_effect = [
        b"", b"", b"", f"{unit_id} gas data\r".encode()
    ]
    result = alicat_flow.available_gases(unit_id)
    assert result == f"{unit_id} gas data\r"
    mock_serial.return_value.write.assert_called_once_with(f"{unit_id}??G*\r".encode())


def test_alicat_flow_change_gas(alicat_flow: Any, mock_serial: Any) -> None:
    unit_id = "A1"
    gas_num = "123"
    mock_serial.return_value.readline.side_effect = [
        b"", b"", b"", f"{unit_id} gas changed\r".encode()
    ]
    result = alicat_flow.change_gas(unit_id, gas_num)
    assert result == f"{unit_id} gas changed\r"
    mock_serial.return_value.write.assert_called_once_with(
        f"{unit_id}G {gas_num}\r".encode()
    )


def test_alicat_flow_lock_display(alicat_flow: Any, mock_serial: Any) -> None:
    unit_id = "A1"
    alicat_flow.lock_display(unit_id)
    mock_serial.return_value.write.assert_called_once_with(f"{unit_id}L\r".encode())


def test_alicat_flow_unlock_display(alicat_flow: Any, mock_serial: Any) -> None:
    unit_id = "A1"
    alicat_flow.unlock_display(unit_id)
    mock_serial.return_value.write.assert_called_once_with(f"{unit_id}U\r".encode())


def test_alicat_flow_set_units(alicat_flow: Any, mock_serial: Any) -> None:
    unit_id = "A1"
    mock_serial.return_value.readline.side_effect = [
        b"", b"", b"", f"{unit_id} unit set\r".encode()
    ]
    result = alicat_flow.set_units(unit_id)
    assert result == f"{unit_id} unit set\r"
    mock_serial.return_value.write.assert_called_once_with(
        f"{unit_id}DCU 2 61 700 0\r".encode()
    )


def test_alicat_flow_read_stream(alicat_flow: Any, mock_serial: Any) -> None:
    # Simulate a stream of data being read
    mock_serial.return_value.readline.side_effect = [
        b"stream part 1",
        b"stream part 2\r",
        b"",
    ]
    with patch("builtins.print") as mock_print:
        alicat_flow.read_stream()
        mock_print.assert_any_call("stream part 1stream part 2\r")


# Tests for AlicatPressure
def test_alicat_pressure_init(mock_serial: Any) -> None:
    alicat = AlicatPressure(port="/dev/test", baudrate=9600)
    mock_serial.assert_called_once_with(
        "/dev/test",
        9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0,
    )


def test_alicat_pressure_start_stream(alicat_pressure: Any, mock_serial: Any) -> None:
    unit_id = "P1"
    alicat_pressure.start_stream(unit_id)
    mock_serial.return_value.write.assert_called_once_with(f"{unit_id}@=@\r".encode())


def test_alicat_pressure_stop_stream(alicat_pressure: Any, mock_serial: Any) -> None:
    unit_id = "P1"
    alicat_pressure.stop_stream(unit_id)
    mock_serial.return_value.write.assert_called_once_with(f"@@={unit_id}\r".encode())


def test_alicat_pressure_tare(alicat_pressure: Any, mock_serial: Any) -> None:
    unit_id = "P1"
    alicat_pressure.tare(unit_id)
    mock_serial.return_value.write.assert_called_once_with(f"{unit_id}PC\r".encode())


def test_alicat_pressure_poll_data(alicat_pressure: Any, mock_serial: Any) -> None:
    unit_id = "P1"
    mock_serial.return_value.readline.side_effect = [
        b"", b"", b"", f"{unit_id} pressure data\r".encode()
    ]
    result = alicat_pressure.poll_data(unit_id)
    assert result == f"{unit_id} pressure data\r"
    mock_serial.return_value.write.assert_called_once_with(f"{unit_id}\r".encode())


def test_alicat_pressure_set_units(alicat_pressure: Any, mock_serial: Any) -> None:
    unit_id = "P1"
    mock_serial.return_value.readline.side_effect = [
        b"", b"", b"", f"{unit_id} units set\r".encode()
    ]
    result = alicat_pressure.set_units(unit_id)
    assert result == f"{unit_id} units set\r"
    mock_serial.return_value.write.assert_called_once_with(
        f"{unit_id}DCU 2 61 700 0\r".encode()
    )


def test_alicat_pressure_read_stream(alicat_pressure: Any, mock_serial: Any) -> None:
    # Simulate a stream of data being read
    mock_serial.return_value.readline.side_effect = [
        b"data part 1",
        b"data part 2\r",
        b"",
    ]
    with patch("builtins.print") as mock_print:
        alicat_pressure.read_stream()
        mock_print.assert_any_call("data part 1data part 2\r")