import re
import unicodedata

count = 0

players = []
# keys = ['name','total_goalkeeping','total_movement','total_skill','total_defending','total_mentality','total_power','total_attacking','value','wage','pot','ova']
keys = ['total_goalkeeping','total_movement','total_skill','total_defending','total_mentality','total_power','total_attacking','value']
keys_index = {}


for line in open('fifa16.players.csv'):

	if count == 0:
		vals = line.strip().split(",")
		for key in keys:
			index = 0
			for value in vals:
				if value == key:
					keys_index[key] = index
				index += 1

	else:
		player = {}

		line = re.sub('".*?"', '1', line)
		values = line.strip().split(",")

		for key, index in keys_index.iteritems():
			player[key] = values[index]

		players.append(player)
	count += 1

fw = open('data', 'w')
for player in players:
	csv = ""
	for key in keys:
		if key == 'value':
			val = player[key][4:]

			fl = 0
			mul = 1
			if val[len(val)-1] == 'K':
				mul = 1000
				fl = 1
			elif val[len(val)-1] == 'M':
				mul = 1000000
				fl = 1

			mulplicand = 1
			if fl == 1:
				mulplicand = float(val[:-1])
			else:
				mulplicand = float(val)

			total = mulplicand * mul
			player[key] = int(total)


		csv += str(player[key]) + ","
	csv = csv.strip(",")
	csv += "\n"
	fw.write(csv)
