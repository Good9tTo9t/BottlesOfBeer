import time
beers = 99

def song():
    global beers
    while beers > 0:
        print("%d瓶啤酒在牆上，%d瓶啤酒在牆上。拿走一瓶傳下去，"%(beers,beers))
        beers -= 1
        time.sleep(1)
    print("牆上沒有啤酒了，牆上沒有啤酒了。再去商店多買些，")
    time.sleep(1)
    beers = 99
    song()

song()


