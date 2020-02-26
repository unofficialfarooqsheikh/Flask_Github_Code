# import pyodbc 

# class SQL:
#     def __init__(self):
#         self.conn = None

#     def __enter__(self):
#         self.conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-IRHNO1M\SQLEXPRESS; DATABASE=Test DataBase; Trusted_Connection = yes')
#         self.cursor = self.conn.cursor

#     def __exit__(self, *args):
#         if self.conn:
#             self.conn.close()
#             self.conn = None

# def SqlDatatoJson(rows,columns):
# 	columnsout = [ ]
# 	for x in columns:
# 		for y in x: 
# 			columnsout.append(y)
# 	# print('all records',rows)
# 	# print('Columns',columnsout)
# 	dictionary={}
# 	output= [ ]
# 	for row in rows:
# 		for y in range(len(columnsout)):
# 			# print(columnsout[y],str(row[y]))
# 			dictionary.update({   
# 				columnsout[y]:str(row[y])})
# 		output.append(dictionary.copy())
# 	# print("here Output",output)
# 	return output