#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ticket_dic = {}

    for i in range(0, length):
        ticket_dic[tickets[i].source] = tickets[i].destination

    route = []
    source = "NONE"
    destination = ticket_dic[source]

    while destination is not "NONE":
        route.append(destination)
        source = destination
        destination = ticket_dic[source]

    route.append("NONE")
    return route
