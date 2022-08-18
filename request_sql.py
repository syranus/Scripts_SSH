import sqlite3
import sys

conn = sqlite3.connect("C:\\Users\\j.mauduit\\Desktop\\captiveportalcnam_wifi_lry.db")
#conn = sqlite3.connect("/var/db/captiveportalcnam_wifi_lry.db")
c = conn.cursor()
c.execute("SELECT count(*) FROM captiveportal")
data = c.fetchall()

for i in data:
    val = int(i[0])
    print(val)
    if val == 0:
        print("Personne de connecté")
        sys.exit(1)
    else:
        print(f"OK - {val} Utilisateurs connectés")
        sys.exit(0)


conn.commit()
conn.close()