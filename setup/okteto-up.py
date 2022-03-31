import os
from sys import exit

token = os.environ.get("OKTETO_TOKEN")
if not token: exit("#"*25 + "\nSet OKTETO_TOKEN!!\n" + "#"*25)
  
def okteto_up():
  from logging import getLogger
  getLogger("OKTETO").warning("RESTARTING!!")
  return os.system(string.format(token))

string = """\
okteto context use https://cloud.okteto.com --token {}
rm -rf nekopack-test
git clone https://github.com/ashty-drone/nekopack-test.git
cd nekopack-test
okteto deploy
"""

while True:
  from datetime import datetime
  start_time = datetime.now()

  while True:
    curr_time = datetime.now()
    uptime = curr_time - start_time
    if uptime.seconds >= 180: break
  
  try: okteto_up()
  except: pass
