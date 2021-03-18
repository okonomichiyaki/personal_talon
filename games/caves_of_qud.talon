app.name: CoQ.exe
-
settings():
    key_wait = 16.0
    key_hold = 16.0

# general
(menu|close|cancel): key(escape)
(open|pick|talk|okay): key(space)
new game: key(n)
continue: key(c)
options: key(o)
save: key(s)
quit: key(q)
help: key(f1)

# in-game
overlay on: key(alt:down)
overlay off: key(alt:up)
abilities: key(a)
move: key(w)
character: key(x)
inventory: key(i)
equipment: key(e)
quests: key(q)
tinker: key(k)
powers: key(p)
wait: key(keypad_5)

trade: key(t)
add: key(keypad_plus)
remove: key(keypad_minus)
offer: key(o)

take it:
    key(space)
    key(g)

# directions
north: key(keypad_8)
south: key(keypad_2)
east: key(keypad_6)
west: key(keypad_4)
north east: key(keypad_9)
north west: key(keypad_7)
south east: key(keypad_3)
south west: key(keypad_1)
up: key(shift-,)
down: key(shift-.)

camp: key(shift-m)
rest until healed: key(`)

# kushrala
freeze: key(shift-r)
teleport: key(shift-t)
corrosive: key(shift-g)

# 
flame: key(shift-l)
mirror: key(shift-r)
temporal: key(shift-t)

# narawur
clairvoyance: key(shift-c)
(sting|ting): key(shift-g)
