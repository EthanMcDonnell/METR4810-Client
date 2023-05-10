
from bleak import BleakScanner, BleakClient
from controller import Game

class Client:

    def __init__(self):
        self.UUID = "0000abf1-0000-1000-8000-00805f9b34fb"
        self.address = "0DEF6B3D-07EF-0305-9454-93D83ADF3CE2"
        self.name = "METR4810_Team8"

    async def read_all_bt(self):
        devices = await BleakScanner.discover()
        for d in devices:
            if d.name == self.name:
                print(d)
                print(d.details)
                print(d.address)
            
    async def write_to_server(self, gameInstance:Game):
        async with BleakClient(self.address) as client:
            while(gameInstance.running):
                # needs to be run here (within "BleakClient as client")
                gameInstance.run_game() 
                if (gameInstance.analogValuesAssigned):
                    print(gameInstance.encodable_analog_values)
                    # Remove brackets on end, whitespace and send to server as bytes
                    await client.write_gatt_char(self.UUID, gameInstance.encodable_analog_values.encode(), response=False) 
                    # Need to read as well for some reason ¯\_(ツ)_/¯, Gatt event on client side not event 2 unless it is called
                    await client.read_gatt_char(self.UUID) 
