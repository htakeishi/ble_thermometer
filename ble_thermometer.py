import asyncio
from bleak import BleakClient
# https://bleak.readthedocs.io/en/latest/api.html#module-bleak.backends.service

address = "B8:80:4F:58:B9:6C" # you can find a thermometer's back panel if UT-201BLE
UUID =    "00001809-0000-1000-8000-00805f9b34fb" # refer to GATT specification

async def run(address):
    client = BleakClient(address)
    try:
        await client.connect()
        if (client.is_connected):
            ret = await client.read_gatt_char(UUID)
            print("ret: {0}".format("".join(map(chr, ret))))
        else:
            raise Exception
    except Exception as e:
        print(e)
    finally:
        await client.disconnect()

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))