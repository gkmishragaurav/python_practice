#Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei),
# find the minimum number of conference rooms required.

def meeting_room(a):
    a.sort(key=lambda item: item[0])
    print(a)
    room=[]
    for start, end in a:
        if not room:
            room.append([start, end])
        else:
            status=False
            for i, item in enumerate(room):
                item_start, item_end = item
                if start >= item_end:
                    temp = [item_start, end]
                    room[i] = temp
                    status=True
                    break
            if not status:
                room.append([start, end])
            print(room)
    return len(room)

# a = [[7,10],[2,4]] - 1
a = [[7, 10], [4, 19], [19, 26], [14, 16],[13, 18], [16, 21]] # --  3
# a =  [[1, 18], [18, 23], [15, 29], [4, 15], [2, 11], [5, 13]] # 4
# a = [[0, 30], [5, 10], [15, 20]]#2
print(meeting_room(a))


