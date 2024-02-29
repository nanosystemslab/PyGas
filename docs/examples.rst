Using AlicatFlow and AlicatPressure
------------------------------------

The `AlicatFlow` and `AlicatPressure` classes from the `pygas` library allow for interacting with Alicat flow meters and pressure transducers, respectively. Below is an example showcasing how to initialize these classes and use some of their key methods to perform common tasks.

First, we instantiate an `AlicatFlow` object and use it to stop streaming, change the gas type, and poll data based on user input:

.. code-block:: python

    from pygas import AlicatFlow, AlicatPressure

    # Initialize the AlicatFlow object
    alicat_flow = AlicatFlow()

    # Get the current unit ID from the user
    unit_id: str = input("Current unit_id: ")

    # Stop the data stream for the specified unit
    alicat_flow.stop_stream(unit_id)

    # Change the gas type based on user input
    gas_num: str = input("Gas num: ")
    alicat_flow.change_gas(unit_id, gas_num)

    # Poll data for the specified unit and print it
    data: Optional[str] = alicat_flow.poll_data(unit_id)
    print(data)

Similarly, for interacting with an Alicat pressure transducer, you can initialize an `AlicatPressure` object. Here's how you might use it to start a data stream and then read that stream:

.. code-block:: python

    # Initialize the AlicatPressure object
    alicat_pressure = AlicatPressure()

    # Start streaming data for a specified unit
    unit_id = input("Enter unit ID for pressure transducer: ")
    alicat_pressure.start_stream(unit_id)

    # Example function call to read the stream (implementation not shown)
    # alicat_pressure.read_stream()

Remember to replace `"Enter unit ID for pressure transducer: "` and other placeholder texts with actual values or logic as necessary for your application.

These examples demonstrate the versatility of the `pygas` library in managing flow and pressure measurements with Alicat devices.
