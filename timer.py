import time
print("Press enter Key to start")
print("Press ctrl+c to stop")
while True:
    try:
        input()
        start = time.time()
        print("started")
    except KeyboardInterrupt:
        print("Stopped")
        end = time.time()
        print("toatal time =",round(end -start ,2),"sec")
        break
