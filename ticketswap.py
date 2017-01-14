import sys
import copy

charges = [0, 1, 1.9, 2.7, 3.4, 4.0, 4.5, 4.9, 5.2, 5.4, 5.5]

class Passenger(object):

    def __init__(self, name, entry, end, idVal):
        self.idVal = int(idVal)
        self.name = name
        self.entry = int(entry)
        self.end = int(end)
        self.current = int(entry)
        self.currentTicket = int(idVal)
        self.bill = int(0)


def run_ticket_sim(station, passengers, exited, total, total_1):
    loss = list()
    for p in passengers:
        fake_pas = copy.deepcopy(passengers)
        fake_sect = copy.deepcopy(p.intersect)
        facts = calc_max_loss(p.idVal, fake_sect, fake_pas)
    max = -1
    for i in loss:
        if(i > max):
            max = i
    #print "Max Loss: " + str(max)

        #for i in p.intersect:
        #    temp = p.entry
        #    p.entry = passengers[i-1].entry
        #     passengers[i-1].entry = temp

        #    total_2 = calculate_total(passengers)
            #print "Total_1 " + str(total_1)
            #print "Total_2 " + str(total_2)
            #print "Loss " + str(total_1 - total_2)
   #        if(total_1 - total_2 > 0):
   #            loss.append(total_1 - total_2)

#--------------------------------------------------------

            #if(total_1 <= total_2):
            #    print "More efficent"


r = list()

def calc_max_loss(p, intersect, passengers):
    for i in intersect:
        safe_sect = copy.deepcopy(intersect)
        safe_pas = copy.deepcopy(passengers)
        temp = safe_pas[p-1].entry
        safe_pas[p-1].entry = safe_pas[i-1].entry
        safe_pas[i-1].entry = temp
        safe_sect.remove(i)
        #print "Safe print " + str(calculate_total(safe_pas))
        r.append(str(calculate_total(safe_pas)))
        calc_max_loss(p, safe_sect, safe_pas)



            #print str(p.idVal) + " --> " + str(i)
            #x = copy.deepcopy(passengers)
            #print "Swap " + str(p.idVal) + " with " + str(i)
            #temp = p.entry
            #print "Before: " + str(p.entry) + " " + str(passengers[i-1].entry)
            #p.entry = passengers[i-1].entry
            #passengers[i-1].entry = temp
            #print "After: " + str(p.entry) + " " + str(passengers[i-1].entry)
            #print "Total " + str(calculate_total(passengers))
            #passengers = x


def swap_ticket(pas_1, pas_2):
    if(pas_1.entry < pas_2.entry):
        x = pas_1.end - pas_2.entry
        #print x
        pas_1.bill = charges[x]
        pas_2.bill = charges[pas_2.end - pas_1.entry]
        #print "Pas_1 " + str(pas_1.bill)
        #print "Pas_2 " + str(pas_2.bill)
    else:
        x = pas_2.end - pas_1.entry
        #print x
        pas_1.bill = charges[pas_1.end - pas_2.entry]
        pas_2.bill = charges[x]
        #print "Pas_1 " + str(pas_1.bill)
        #print "Pas_2 " + str(pas_2.bill)



def complete_intersection(passengers, maximum):
    stops_array = list()

    for p in passengers:
        low = p.entry
        high = p.end
        id_v = p.idVal

        stops = list()
        for i in range(low, high + 1):
            stops.append(i)
        stops_array.append(stops)

    intersections = list()
    for i in range(0, len(passengers)):
        matches = list()
        for j in range(0, len(passengers)):
            if(contains_same(stops_array[i], stops_array[j]) and passengers[i].idVal != passengers[j].idVal):
                matches.append(passengers[j].idVal)
        intersections.append(matches)

    for i in range(0, len(passengers)):
        passengers[i].intersect = intersections[i]

    return intersections


def contains_same(list_1, list_2):
    contains = False
    for i in range(0, len(list_1)):
        for j in range(0, len(list_2)):
            if(list_1[i] == list_2[j]):
                contains = True
    return contains

def calculate_total(passengers):
    total = 0

    for p in passengers:
        length = p.end - p.entry
        i = 0
        fee = 0
        initial = 1
        discount = float(.10)
        while(i < length and i < 10):
            fee += (1 - (i * discount))
            # str(fee)
            i += 1
        total += fee
        #print "-------"

    return total

f = open(str(sys.argv[1]), "r")
passengers = []
id_value = int(1)
for line in iter(f):
    if(line.strip()):
        values = line[10:line.index(")")].split(",")
        passengers.append(Passenger(values[0], values[1], values[2], id_value))
        id_value = id_value + 1

maximum = -1
for pas in passengers:
    if(maximum < pas.end):
        maximum = pas.end

#print "Max " + str(maximum)

total = calculate_total(passengers)
complete_intersection(passengers, maximum)

deque = list()
for p in passengers:
    deque.append(p.idVal)
    #print p.intersect

#print "Total without Swap " + str(total)

number = run_ticket_sim(int(1), passengers, len(passengers), int(0), total)
#print "Max Loss " + str(number)

max = -1
#print "Len r " + str(len(r))
for i in r:
    if(float(total) - float(i) > 0):
        if(float(total) - float(i) > max):
            max = (float(total) - float(i))
print "loss(" + str(max) + ")."

f.close()
