Alicat Flow Meter Interface
============================

Detailed documentation of the AlicatFlow class and its methods.

.. autoclass:: pygas.AlicatFlow
   :members:
   :undoc-members:
   :show-inheritance:

   The ``AlicatFlow`` class represents an interface for controlling Alicat flow meters. It provides methods to start and stop data streaming, poll data, tare the device, query available gases, change gas types, lock and unlock the device display, read streaming data, set units, query static unit value, set baud rates, and change unit IDs.

   Initialization of the class:

   .. automethod:: __init__
       :no-index:

   Starting the data stream:

   .. automethod:: start_stream
       :no-index:

   Polling data from the device:

   .. automethod:: poll_data
       :no-index:

   Stopping the data stream:

   .. automethod:: stop_stream
       :no-index:

   Taring the device:

   .. automethod:: tare
       :no-index:

   Querying available gases:

   .. automethod:: available_gases
       :no-index:

   Changing the gas type:

   .. automethod:: change_gas
       :no-index:

   Locking the device display:

   .. automethod:: lock_display
       :no-index:

   Unlocking the device display:

   .. automethod:: unlock_display
       :no-index:

   Reading the streaming data:

   .. automethod:: read_stream
       :no-index:

   Setting the units:

   .. automethod:: set_units
       :no-index:

   Querying static unit value:

   .. automethod:: query_unit_val_static
       :no-index:

   Setting the baud rate:

   .. automethod:: baud_rate
       :no-index:

   Changing the unit ID:

   .. automethod:: change_unit_id
       :no-index:


