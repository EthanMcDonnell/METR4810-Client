
from bleak import BleakScanner, BleakClient, BleakError
from controller import Game
import asyncio

class Client:

    def __init__(self):
        self.server_UUID = "0000abf1-0000-1000-8000-00805f9b34fb"
        # OLD ESP32s3 BOARD ADDRESS
        #self.server_address = "0DEF6B3D-07EF-0305-9454-93D83ADF3CE2"
        # NEW ESP32s3 BOARD ADDRESS
        self.server_address = "428732B4-B871-FE8F-56A4-F8DE0505BFF7"
        self.server_name = "METR4810_Team8"

    async def read_bt_data(self):
        """
        Prints device data that matches server name.
        """
        # Finds all devices which are creating BLE advertisements 
        devices = await BleakScanner.discover()
        for d in devices:
            if d.name == self.server_name:
                print(d)
                print(d.details)
                print(d.address)
            
    async def write_to_server(self, gameInstance:Game):
        """
        Connects client to server and sends 'Game' analog data.

        Args:
            gameInstance (Game): Instance of Game to run within connect loop
        """
        # Connects client with server
        try:
            async with BleakClient(self.server_address) as client:
                while(gameInstance.running):
                    # Need to run game here as don't want to send data before connected
                    gameInstance.run_game() 
                    if (gameInstance.analogValuesAssigned):
                        await client.write_gatt_char(self.server_UUID, gameInstance.encodable_analog_values.encode(), response=False) 
                        await client.read_gatt_char(self.server_UUID) # To get confirmation from server
        except BleakError:
            print("Disconnected")
            return