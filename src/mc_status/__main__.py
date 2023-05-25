import pg_data
import minestat
from time import sleep

connection = pg_data.get_connection()
pg_data.setup(connection)

while True:
    server = minestat.MineStat("109.123.245.24", 25565)
    cursor = connection.cursor()
    print(server.player_list)
    print(server.latency)
    cursor.execute("INSERT INTO status (server_online, players, latency) VALUES (%s, %s, %s)", [
        str(1 if server.online else 0),
        str(server.current_players if server.current_players != None else 0),
        str(server.latency)
        ])
    sleep(2)