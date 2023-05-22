
from controller import Game
from wireless_comms_client import Client
import asyncio

def main():
    runGameWithoutClient = False # set to true for testing game
    c = Client()
    g = Game()
    if runGameWithoutClient:
        while g.running:
            g.run_game()
    else:
        while g.running:
            asyncio.run(c.write_to_server(g)) # Game loop is within write to server
if __name__ == "__main__":
      main()