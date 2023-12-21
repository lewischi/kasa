#!/usr/bin/env python
from subprocess import run
import re

BASE = 'kasa --host '
OFF = ' off'
ON = ' on'
STATE = ' state'

host = '192.168.4.38'
shellCmd = BASE + host + ' state'

testing = False
if testing == True:
  data = bytes('Device state: True', 'utf-8')

data = run(shellCmd, capture_output=True, shell=True)
output = data.stdout.splitlines()
errors = data.stderr.splitlines()
# combined = output + errors

pattern = re.compile(r"Device state:\s*(.*)")

# Combine and decode each line from byte to utf-8
decoded_line = [line.decode('utf-8') for line in output]
combined_string = '\n'.join(decoded_line)

match_found = False

for line in output: # Check each line of stdout
  line = line.decode('utf-8') # from byte to utf-8
  first_match = pattern.search(line) # Find the first match in the input data

  if first_match:
    matched_string = first_match.group(0).strip()
    if "True" in matched_string:
      shellCmd = BASE + host + OFF
      run(shellCmd, capture_output=True, shell=True)
      match_found = True
      break
    elif "False" in matched_string:
      shellCmd = BASE + host + ON
      run(shellCmd, capture_output=True, shell=True)
      match_found = True
      break

if not match_found:
  print("Pixar light not working.")
  for line in errors:
    decoded_errors = line.decode('utf-8')
    combined_string = '\n'.join(decoded_errors)
  print(combined_string)

