from i3ipc.aio import Connection
from i3ipc import Event

import asyncio

async def main():
    def on_window(self, e):
        print(e)

    c = await Connection(auto_reconnect=True).connect()

    workspaces = await c.get_workspaces()

    c.on(Event.WINDOW, on_window)

    await c.main()

asyncio.get_event_loop().run_until_complete(main())