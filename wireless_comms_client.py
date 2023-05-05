import asyncio
from bleak import BleakScanner, BleakClient
from controller import Game

class Client:

    def __init__(self):
        self.UUID = "0000abf1-0000-1000-8000-00805f9b34fb"
        self.address = "0DEF6B3D-07EF-0305-9454-93D83ADF3CE2"
        

    async def read_all_bt(self):
        devices = await BleakScanner.discover()
        #BleakClient.connect()
        for d in devices:
            if d.name == "METR4810_Team8":
                print(d)
                print(d.details)
                print(d.address)
                print(d.metadata)
                
    async def connect_with_server(self):
        async with BleakClient(self.address) as client:
            is_connected = await client.is_connected()
            print(f"Connected: {is_connected}")
            

    async def write_to_server(self):
        async with BleakClient(self.address) as client:
            g = Game()
            string = "."
            while(g.running):
                g.run_game()
                await client.write_gatt_char(self.UUID,str(list(g.analog_keys.values()))[1:-1].replace(" ","").encode(), response=False) # Remove brackets on end, whitespace and send as bytes
                await client.read_gatt_char(self.UUID) #Need to read as well for some reason

def main():
    asyncio.run(Client().write_to_server())

if __name__ == "__main__":
      main()