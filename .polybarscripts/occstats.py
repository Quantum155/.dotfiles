import mcstatus
from time import sleep
import datetime
import sys

QUERY_TIME = 30  # Time between pinging the server in seconds

server = mcstatus.JavaServer("play.oc.tc")

prev_map = "INIT"
playtime = 0
start_players = 0  # Track how many players are online when a map starts
disconnect_time = 0  # In case of network error, track time

while True:

    try:
        status = server.status()  # query the server
    except:  # Failed to ping the server
        prev_map = "DISCONNECTED"
        disconnect_time += 1
        disconnect_time_hr = datetime.timedelta(seconds=QUERY_TIME*disconnect_time)
        print(f"(OCC) Disconnected [{disconnect_time_hr}]")
        sys.stdout.flush()
        sleep(QUERY_TIME)
        continue

    disconnect_time = 0
    motd = status.description

    active_map = motd.splitlines()[1][6:-4]  # Get the active maps title from the server motd
    # TODO Detect when an event is active

    if prev_map != active_map:
        prev_map = active_map
        start_players = status.players.online
        playtime = 0
    else:
        playtime += 1

    playtime_hr = datetime.timedelta(seconds=QUERY_TIME*playtime)  # Convert playtime to a human readable format

    plc = status.players.online - start_players  # Player change since the game started
    if plc > 0:  # Create a string from the int with
        plcs = f"+{plc}"
    else:
        plcs = str(plc)

    print(f"MAP: {active_map} [{playtime_hr}] PLAYERS: {status.players.online} [{plcs}]")
    sys.stdout.flush()  # Flushing stdout required for polybar
    sleep(QUERY_TIME)
