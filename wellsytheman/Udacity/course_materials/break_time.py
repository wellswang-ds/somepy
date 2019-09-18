import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program srarted on " + time.ctime())
while(break_count<total_breaks):
    time.sleep(1*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=BVRnLUMeAoQ&list=PLmIAixrHzxnbZqAuPGHv4Vy5SosvlfxQv")
    break_count = break_count + 1
