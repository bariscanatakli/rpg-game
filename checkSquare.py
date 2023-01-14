# square1 = {"x1":500,"y1":500,"x2":600,"y2":500,"x3":500,"y3":600,"x4":600,"y4":600}

square1X = {"x1":500,"x2":600}
square1Y = {"y1":500,"y3":600}

# square2X = {"x1":550,"x2":650,"x3":550,"x4":650}
# square2Y = {"y1":550,"y2":550,"y3":650,"y4":650}

# for name,pos in square2X.items():
#     if pos < square1["x2"] and pos > square1["x1"]:
#         print("x düzlemi kesişiyor", name)

# for name,pos in square2Y.items():
#     if pos < square1["y3"] and pos > square1["y1"]:
#         print("y düzlemi kesişiyor", name) 

square2 = {"x1,y1":(600,600),"x2,y2":(600,600),"x3,y3":(600,600),"x4,y4":(600,600)}
    
for name,positions in square2.items():
    if positions[0] >= square1X["x1"] and positions[0] <= square1X["x2"]:
        if positions[1] >= square1Y["y1"] and positions[1] <= square1Y["y3"]:
            print(positions,": kesisen nokta:",name)