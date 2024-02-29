Alicat Pressure Transducer Interface
=====================================

Detailed documentation of the AlicatPressure class and its methods.

.. autoclass:: pygas.AlicatPressure
   :members:
   :undoc-members:
   :show-inheritance:

   The ``AlicatPressure`` class provides an interface for controlling Alicat Pressure Transducers. It includes functionality to start and stop streaming, perform taring, read streaming data, poll data, and set units.

   Initialization of the class:

   .. automethod:: __init__
        :no-index:

   Starting the data stream:

   .. automethod:: start_stream
        :no-index:

   Stopping the data stream:

   .. automethod:: stop_stream
        :no-index:

   Taring the device:

   .. automethod:: tare
        :no-index:

   Reading the streaming data:

   .. automethod:: read_stream
        :no-index:

   Polling data:

   .. automethod:: poll_data
        :no-index:

   Setting the units:

   .. automethod:: set_units
        :no-index:

