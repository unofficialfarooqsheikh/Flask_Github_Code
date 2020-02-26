# from sql import SQL
# conn = SQL() 
# with conn:
#     csr = conn.cursor()
#     data = 'admin@admin.com'
#     try:
#         csr.execute("INSERT INTO dbo.users VALUES('admin@admin.com','Admin@123','Administrator',1)")
#         csr.commit()
#         print(csr)
#     except :
#         pass
    
# # conn = SQL() 
# # with conn:
# #     csr = conn.cursor()
# #     data = "*"
# #     csr.execute('SELECT * FROM dbo.users WHERE email = ?',email)
# #     data=csr.fetchone()
# # # user = user_email_mapping.get(id)
# # if user and safe_str_cmp(data[2], password):
# #         print(user)
# #         return user