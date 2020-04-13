#This is an example of a while loop
# The start condition is set to false so
# testing can be done on the state of the
# variable.

user_input = ""
started = False
# Starting the while loop
while True:
    user_input = input(">").lower()
    if user_input == "start":
        if started:
            print("Car already running")
        else:
            started = True
            print("Car started...")
    elif user_input == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Car stopped")
    elif user_input == "help":
        print("""
Type "start" to start
Type "stop" to stop
Type "quit" to end       """)
    elif user_input == "quit":
        break
    else:
        print("You entered jibberish")
