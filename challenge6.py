import time
print("""
This game will test your ability to count.
Press the ENTER key once to start the timer.
Then press ENTER again when you think it has been 10 seconds.
The program will output how close you were to the 10 seconds.
      """)
input("Press ENTER to begin ")
starttime = time.time()
input("")
endtime = time.time()
close = (endtime-starttime) - 10
close = round(close,1)
print("You were off by ",close,"seconds")

