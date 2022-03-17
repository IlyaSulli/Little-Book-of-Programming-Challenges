import time
print("""
This game will test your ability to type out the alphabet
press ENTER to start the timer then type in the alphabet
then press ENTER when you have finished
      """)
input("Press ENTER to begin ")
starttime = time.time()
alphabet = input("Enter the alphabet: ")
endtime = time.time()
if alphabet == "abcdefghijklmnopqrstuvwxyz":
    timetaken = endtime-starttime
    timetaken = round(timetaken,1)
    print("It took you ",timetaken,"seconds to type out the alphabet")
else:
    print("You entered the alphabet incorrectly")

