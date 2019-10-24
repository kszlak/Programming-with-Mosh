command = ''
previous = ''
start = ("start")
stop = ("stop")
quit = ("quit")

while True:
    command = input( '> ' ).lower()
    if command == 'help':
        print ('''
start - to start the car
stop - to stop the car
quit - to exit ''')
    elif command == start:
        if previous == start:
            print ('Car is just started!')
        else:
            print ('Car started!')
        previous = start
    elif command == stop:
        if previous == stop:
            print ('Car is just stopped!')
        else:
            print ('Car stopped!')
        previous = stop
    elif command == quit:
        break
    else:
        print("I don't understand that..")
