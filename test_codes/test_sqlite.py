# import sqlite3

# db = sqlite3.connect("data/stationstest.db")
# c = db.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS stationsteset(id INTEGER PRIMARY KEY AUTOINCREMENT, "place name" TEXT, "nearest station" TEXT, "wheelchair accessibility" TEXT)''')
# c.execute("INSERT INTO stationsteset ("place name", 'nearest station', 'wheelchair accessibility') VALUES (?, ?, ?)", ("Boston Commons", "Boyston st", "Accessible"))
# db.commit

import sqlite3

db = sqlite3.connect("data/stationstest.db")
c = db.cursor()
# c.execute('create table stationstest (place name, nearest station, wheelchair accessibility)')
# db.commit()
place_name = "Boston Comons"
station = "Bolyston"
wheelchair = "Accessible"
c.execute('insert into stationstest values (?,?,?)', (place_name, station, wheelchair))
# c.execute('''CREATE TABLE IF NOT EXISTS stationsteset
#         (id INTEGER PRIMARY KEY AUTOINCREMENT, "place name" TEXT, "nearest station" TEXT, "wheelchair accessibility" TEXT)''')
# c.execute('INSERT INTO stationsteset ("place name", "nearest station", "wheelchair accessibility") VALUES (?, ?, ?)', ("Boston Commons", "Boyston st", "Accessible"))
db.commit()
