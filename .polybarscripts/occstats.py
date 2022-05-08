import mcstatus
from time import sleep
import datetime
import sys

QUERY_TIME = 30

server = mcstatus.JavaServer("occanalytics.oc.tc")

prev_map = "INIT"
playtime = 0
start_players = 0

while True:

    status = server.status()
    motd = status.description

    active_map = motd.splitlines()[1][6:-4]

    if prev_map != active_map:
        prev_map = active_map
        start_players = status.players.online
        playtime = 0
    else:
        playtime += 1

    playtime_hr = datetime.timedelta(seconds=QUERY_TIME*playtime)

    plc = status.players.online - start_players
    if plc > 0:
        plcs = f"+{plc}"
    else:
        plcs = str(plc)

    print(f"MAP: {active_map} [{playtime_hr}] PLAYERS:{status.players.online} [{plcs}]")
    sys.stdout.flush()
    sleep(QUERY_TIME)
