import pg_data
import minestat
from time import sleep

connection = pg_data.get_connection()
pg_data.setup(connection)
server = minestat.MineStat("109.123.245.24", 25565)

while True:
    server.json_query()
    cursor = connection.cursor()
    print(f"Latency: {server.latency} ms")
    result = cursor.execute("""INSERT INTO status 
        (server_online, players, latency)
        VALUES (%s, %s, %s)
        RETURNING id""", [
        str(1 if server.online else 0),
        str(server.current_players if server.current_players != None else 0),
        str(server.latency)
        ]).fetchone()

    status_id: int = result[0]
    print(f"Status ID: {status_id}")
    
    if server.player_list != None:
        cursor.executemany("""INSERT INTO user_online
        (status_id, player_name)
        VALUES (%s, %s)""",
        [(status_id,x) for x in server.player_list])
    
    sleep(5)