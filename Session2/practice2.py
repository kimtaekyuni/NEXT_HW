def hack():
    hack = input()  
    if hack == "password":
        count = 0
        for i in range(10):
            print('발사')
            print(10 - count)
            count += 1


hack()
