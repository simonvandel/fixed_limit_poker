import asyncio
import threading
import json
from environment.observers.Observer import Observer
from environment.Constants import Action
from environment import Player
from environment.observers.OmnipotentObservation import OmnipotentObservation, OmnipotentObservationEncoder
import websockets
import time


class WebsocketsObserver(Observer):
    queue_to_send: asyncio.Queue = asyncio.Queue()
    active = False
    thread = None
    websocket = None

    def __init__(self, interval=0.1):
        print("Waiting untill a websockets connection on localhost:8765 occurs ...")

        self.interval = interval

        # Start this in another thread
        self.thread = threading.Thread(target=self.run_async_job, args=())
        self.thread.daemon = True                            # Daemonize thread
        self.thread.start()                                  # Start the execution
        self.wait_for_connection()

    def run_async_job(self):
        # Run async method in this new thread ...
        asyncio.run(self.start())

    async def start(self):
        async with websockets.serve(self.send_data, "localhost", 6789):
            await asyncio.Future()

    async def send_data(self, websocket, path):
        self.websocket = websocket
        self.active = True

        # Wait for client to send something
        await self.websocket.recv()

        # While the program is running, de-queue and send messages
        while self.active or not self.queue_to_send.empty():
            # If we have new messages, send them
            if not self.queue_to_send.empty():
                m = self.queue_to_send.get_nowait()
                # send message
                await self.websocket.send(m)
                # receive ack
                await self.websocket.recv()
            else:
                # Otherwise sleep to avoid burning CPU
                time.sleep(self.interval)

    def wait_for_connection(self):
        while not self.active:
            time.sleep(self.interval)

    def run_to_completion(self):
        self.active = False
        while not self.queue_to_send.empty():
            time.sleep(self.interval)

    def queue_observation(self, observation: OmnipotentObservation) -> None:
        json_string = json.dumps(observation, cls=OmnipotentObservationEncoder)
        self.queue_to_send.put_nowait(json_string)

    def LogNewGame(self, observation: OmnipotentObservation) -> None:
        self.queue_observation(observation)

    def LogNewRound(self, observation: OmnipotentObservation) -> None:
        self.queue_observation(observation)

    def LogPlayerAction(self, observation: OmnipotentObservation, player: Player, action: Action) -> None:
        self.queue_observation(observation)

    def LogGameOver(self, observation: OmnipotentObservation) -> None:
        self.queue_observation(observation)
