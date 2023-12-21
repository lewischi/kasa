from smart_plug import SmartPlug
from constants import *
import asyncio

async def toggle():
  plug = SmartPlug(OFFICE_PIXAR_LAMP)
  await plug.update()

  if plug.is_on:
    await plug.turn_off()
  elif plug.is_off:
    await plug.turn_on()

asyncio.run(toggle())