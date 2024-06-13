def final_direction(start,ds):
    direction_angle={"W":180,"N":90,"E":0,"S":270}
    angle_direction={0:"W",90:"N",180:"E",270:"S"}
    position= direction_angle[start]
    for c in ds:
        if c=="L":
            position +=90
        elif c=="R":
            position -=90
    position=(position+360)%360
    position=angle_direction[position]
    print(position)



final_direction("N",["L","L","L"])
final_direction("N",["R","R","R","L"])
final_direction("N",["R","R","R"])
final_direction("N",["R","L"])


