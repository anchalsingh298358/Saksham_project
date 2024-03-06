def open_file():
    try:
        file=open('xyz.txt','r')
        print(file.read())
        file.close()
    except Exception as e:
        print(e)
    finally:
        print('This is the end of the program!')
open_file()