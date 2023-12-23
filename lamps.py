import argparse
from smart_plug import SmartPlug
from constants import LAMP_IPS, VALID_LAMPS
import asyncio

# Set up command-line argument parsing
parser = argparse.ArgumentParser(description='Toggle smart plugs')
parser.add_argument('lamp', choices=VALID_LAMPS, help='Choose the smart plug to control')

args = parser.parse_args() # Parse command-line arguments

def get_lamp_ip(lamp_choice):
  return LAMP_IPS.get(lamp_choice, None)

async def toggle(lamp_ip):
  plug = SmartPlug(lamp_ip)
  await plug.update()

  if plug.is_on:
    await plug.turn_off()
  elif plug.is_off:
    await plug.turn_on()
  # print(f'Toggling smart plug at IP: {lamp_ip}')

# Get the lamp IP based on the selected command
lamp_ip = get_lamp_ip(args.lamp)

# Check if the lamp IP is valid
if lamp_ip is not None:
# Run the toggle function
  asyncio.run(toggle(lamp_ip))
else:
  print(f"Invalid lamp choice: {args.lamp}. Please choose from {', '.join(VALID_LAMPS)}")
