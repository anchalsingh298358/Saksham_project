# to store the data permanently in files 
# file read and open
# data=open('abc.txt','r')   # read mode means to just view the contents of file (no changes)
# # print(data)  # object 
# # for i in data:
# #     print(i)

# print("------------------------------")
# # print(data.read(20))
# # print(data.readline(6))
# print(data.readlines())

# file_data=open('abc1.txt',mode='w')
# file_data.write('Hello file , lets add some content to file.')
# file_data.close()

# file=open('abc.txt','r+')
# file.write('This is first line of file.and lets change some data of file.')
# for i in file:
#     print(i)
# file.close()

# home work (mode=a) 

# file=open('abc.txt','a+')
# file.write('Good day to you')
# file.seek(0)
# print(file.read())
# file.close()

