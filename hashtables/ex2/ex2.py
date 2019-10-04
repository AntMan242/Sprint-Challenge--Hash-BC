#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,

                        hash_table_retrieve,)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    prevDes = None
    for t in tickets:

        if t.source is None: #The ticket for the first flight has a destination of None
            hash_table_insert(route[0], t.destination)
            prevDes = t.destination
        elif t.source == prevDes:
            hash_table_insert(route, t.destination)
            prevDes = t.destination

    return route