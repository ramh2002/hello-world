
# to calculate the distance
def distance(p1, p2):
    # calculate the distance
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

# create zero matrix for all the houses
def createZeroMatrix(n, m):
    return [['0' for i in range(m)] for j in range(n)]

# print the house distance from the pizza location
def mTightPrint(m):
    # iterate though each house
    for i in range(len(m)):
        line = ''
        for j in range(len(m[0])):
            line +=str(m[i][j])
        # final output which prints location of each house from pizza store
        print(line)

def PDMap(h, w, pizzaLoc):
    # initially all the houses are at zero locations (Mayor House)
    all_houses = createZeroMatrix(h,w)
    store_num = 0 # use to count the pizza stores

    #iterate each house location to find the distance between pizza store and house
    for i in range(h):
        for j in range(w):
            closer_dis = h*w
            closer = -1   # initialized to -1 because no house beyond Mayor house
            repeated = False # To check the nearest pizza locations common between the house

            for k in range(len(pizzaLoc)):
                dis = distance([i, j], pizzaLoc[k])   # calculate the distance of pizza location from the house
                # if the house distance is greater than the pizza loc distance then the closer distance is the pizza location
                if dis < closer_dis:
                    closer_dis = dis
                    closer = k
                    repeated = False
                #if current distance and closer distance are same means its a pizza house so its repeated which is substituted by X
                elif dis == closer_dis:
                    repeated = True

            # all the repeated locations are highlighted with X
            if repeated:
                all_houses[i][j] = 'X'
            # Non repeated pizza location from the current house location
            else:
                all_houses[i][j] = str(closer)
    # return all the house locations
    return all_houses


mTightPrint(PDMap(10, 10, [[2, 3], [4, 9], [7, 2]]))
mTightPrint(PDMap(50,80,[[20,10], [30,30],[40,20],[45,55],[10,55],[35,70],[35,60]]))
