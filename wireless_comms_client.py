import asyncio
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
            
    async def write_to_server(self):
        async with BleakClient(self.address) as client:
            g = Game()
            while(g.running):
                g.run_game()
                await client.write_gatt_char(self.UUID,g.encodable_analog_values.encode(), response=False) # Remove brackets on end, whitespace and send as bytes
                await client.read_gatt_char(self.UUID) #Need to read as well for some reason

def main():
    c = Client()
    #asyncio.run(c.read_all_bt())
    asyncio.run(c.write_to_server())
    # g = Game()
    # while(g.running):
    #     g.run_game()

if __name__ == "__main__":
      main()