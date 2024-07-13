'''

import numpy as np 
num=np.array([2,3,4,9,3,7,8])
print(np.sort(num))

room=np.random.choice(['A','B'])
print(room)

states=np.array(["Clean","Dirty"])
stat=np.random.choice(states)
print(stat)
'''
#Dictionary
# room_states={
#     'A':'Clean',
#     'B':'Dirty'
    
# }

# print(room_states)


import numpy as np 
rooms=np.array(['A','B'])
states=np.array(['Clean','Dirty'])

def chooseRoom():
    return np.random.choice(rooms)

def chooseState():
    return np.random.choice(rooms)

def cleanRooms():
    room_states = {}
    for room in rooms:
        room_states[room] = chooseState()
    return room_states

room_states = cleanRooms()
print(room_states)

vacuumPosition = chooseRoom()
print('Current Position:', vacuumPosition)

cost=0
if room_states[vacuumPosition] == 'Dirty':
    print(f'{vacuumPosition} is dirty.')
    print(f'Cleaning{vacuumPosition} ')
    
    room_states[vacuumPosition]='Clean'
    print(f'{vacuumPosition} is cleaned')
    cost+=1
else:
    print(f'{vacuumPosition} is clean')
    print('No operation')
    



