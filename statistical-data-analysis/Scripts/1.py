"""This Program will connect to sql database and add respected json file to respected database"""

import mysql.connector as sql
import json


conn = sql.connect(host='localhost',database='STASTISTICAL_DATA_ANALYSIS',user='root',password='####')

if conn.is_connected():
	print("Connected to MySql Server")

cursor = conn.cursor()

with open ("/home/raman-pop/statistical-data-analysis/Nith_results/result/json/Cse_dual/batch_16_cgpi.json","r") as file:
	data = json.load(file)


for i, item in enumerate(data):

	Rank = item.get("Rank", None)
	RollNo = item.get("Rollno", None)
	Name = item.get("Name", None)
	Cgpa= item.get("Cgpa", None)
	Sgpa= item.get("Sgpa", None)
	Points = item.get("Points", None)

	cursor.execute("INSERT INTO Cse_dd_final_2019 (Rank_No, RollNo, Name, Cgpi, Sgpi, Points) VALUES (%s, %s, %s, %s, %s, %s)", (Rank, RollNo, Name, Cgpa, Sgpa, Points))

conn.commit()
conn.close()







