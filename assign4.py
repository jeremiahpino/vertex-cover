from math import degrees
import sys 
from collections import defaultdict
from itertools import chain, combinations

def powerset(iterable):
    # powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# class represents the graph
class Graph:

    # python constructor 
    def __init__(self, vertices):
        # number of vertices
        self.V = vertices 

        # dictionary to store graph
        self.graph = defaultdict(list)
        # dictionary to store degrees
        self.degree = defaultdict(int)
        # temp storage of degrees
        self.degreeNew = defaultdict(int)

    # function to add edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

        count1 = self.degree[u] + 1
        self.degree[u] = count1

        count2 = self.degree[v] + 1
        self.degree[v] = count2

    # save old degrees to new degrees
    def save(self):
        self.degreeNew = self.degree.copy()

    # print old degrees
    def printD(self):
        for key, value in self.degree.items():
            print(key ,":", value)

    # print new degrees
    def printDn(self):
        for key, value in self.degreeNew.items():
            print(key ,":", value)

    # print graph
    def printG(self):
        print("Graph:")
        for key, value in self.graph.items():
            print(key ,":", value)
    
    # print vertices
    def printV(self):
        print("Vertices:")
        for x in range(self.V):
            print(x)

    # 2 approximation function
    def twoapprox(self):

        # intialize all unvisited vertices to false
        visited = [False]*(self.V)

        # edge = (u,v)
        # consider all edges 
        for u in range(self.V):

            # if u is not visited
            if not visited[u]:

                # for vertices adjacent to u, pick first that is not yet visited
                for v in self.graph[u]:

                    # if v is not visited 
                    if not visited[v]:

                        # set visited to true for u
                        visited[v] = True
                        # set visited to true for v
                        visited[u] = True
                        # break from inner loop
                        break
        
        # create list and append visited values
        twolist = []
        for j in range(self.V):
            if visited[j]:
                twolist.append(j)

        return twolist


    # logn approximation function
    def logapprox(self):

        # list of vertices to return
        loglist = []

        # mark all vertices as NOT visited
        visited = [False] * (self.V)

        # intialize counter to 0
        counter = 0

        # iterate through all vertices
        for x in range(self.V):

            # find max degree
            maxdegree = max(self.degree, key=self.degree.get)
            #print(maxdegree)
            # delete max degree 
            del self.degree[maxdegree]

            # if maxdegree is not visited 
            if not visited[maxdegree]:

                # append max degree to list
                loglist.append(maxdegree)

                # mark max degree as visited
                visited[maxdegree] = True

                # iterate through all vertices
                for u in range(self.V):
                    #print("u", u)
                
                    # check parents of vertex u
                    for p in self.graph.keys():
                        #print("parent", p)

                        # if p and is a parent of max degree (EX: 1: 2,3,4)
                        if (u) in self.graph[p]:

                            # check if p is visited
                            if visited[p] == True:
                                
                                #print("parent visited", p)
                                # increment counter if vertex is visited
                                counter = counter + 1

                    # check children of vertex u 
                    for child in self.graph[u]:
                        #print("child", child)

                        # check if child is visited
                        if visited[child] == True:
                            #print("child visited", child)

                            # increment counter if vertex is visited
                            counter = counter + 1

                    #print("counter",counter)

                    #print("degree of u:", self.degree[u])
                    # degree of u equals counter
                    if(self.degree[u] == counter):
                        visited[u] = True

                    # reset counter
                    counter = 0

                    # all vertices have been visited (RETURN list)
                    if sum(visited) == len(visited):
                        return loglist


    # brute force function
    def bruteforce(self, wholeSet):
        
        # list of vertices
        blist = []

        # mark all vertices as NOT visited
        visited = [False] * (self.V)

        # intialize counter to 0
        counter = 0

        # interate through subset of whole set
        for subset in wholeSet:

           #print("SUBSET:", subset)

            # for every subset intialize points to false
           visited = [False] * (self.V)
           
           # iterate through entire subset
           for value in subset:

                #print("value", value)

                # if value is not visited 
                if not visited[value]:

                    # append value to list
                    #blist.append(value)
                    #print("blist", blist)

                    # mark value as visited
                    visited[value] = True

                    # iterate through the subset
                    for u in range(self.V):
                        #print("u", u)
                    
                        # check parents of vertex u
                        for p in self.graph.keys():

                            # if p and is a parent of current vertex u (EX: 1: 2,3,4)
                            if (u) in self.graph[p]:
                                #print("parent", p)

                                # check if p is visited
                                if visited[p] == True:
                                    
                                    #print("parent visited:", p)
                                    # increment counter if vertex is visited
                                    counter = counter + 1

                        # check children of vertex u 
                        for child in self.graph[u]:
                            #print("child", child)

                            # check if child is visited
                            if visited[child] == True:
                                #print("child visited:", child)

                                # increment counter if vertex is visited
                                counter = counter + 1

                        #print("counter",counter)

                        # degree of u equals counter
                        #print("degree of u:", self.degreeNew[u])
                        if(self.degreeNew[u] == counter):
                            visited[u] = True

                        # reset counter
                        counter = 0

                        #print(visited)

                        # all vertices have been visited (RETURN list)
                        if sum(visited) == len(visited):
                            for value in subset:
                                blist.append(value)
                            #print("all true",visited)
                            return blist



def main():
    # get text file argument
    infile = sys.argv[1]

    # create an empty edgeList
    edgeList = []

    # open file for reading and iterate through file add lines to edgeList
    with open(infile, "r") as filobj:
        for line in filobj:
            edgeList.append(line.rstrip().split(" "))

    # create empty list fo vertices
    listv = []

    # iterate through edgeList and add vertices
    for i in range(len(edgeList)):
        num1 = edgeList[i][0]
        num2 = edgeList[i][1]
        num1 = int(num1)
        num2 = int(num2)
        listv.append(num1)
        listv.append(num2)

    # create set to delete duplicate vertices
    vset = set(listv)

    # number of vertices is length of set 
    numvertices = len(vset)

    #print(numvertices)

    #print(vset)

    entireSet = list(powerset(vset))

    # for sub in entireSet:
    #     print("subset", sub)
    #     for value in sub:
    #         print("value(s)",value)

    # initialize number of vertices in graph 
    g = Graph(numvertices)

    # iterate through edgeList and add edges
    for i in range(len(edgeList)):
        num1 = edgeList[i][0]
        num2 = edgeList[i][1]
        num1 = int(num1)
        num2 = int(num2)
        g.addEdge(num1, num2)

    #print(edgeList)

    #flatList = [x for sublist in edgeList for x in sublist]   

    #g.printG()
    #g.printV()   

    loglist = []
    twolist = []
    blist = []

    #print("original")
    #g.printD()

    # save old degrees to new degrees
    g.save()

    loglist = g.logapprox()
    twolist = g.twoapprox()
    #print("after 2approx")
    #g.printD()
    #g.printDn()
    blist = g.bruteforce(entireSet)

    print("log-Approximation:", end= " ")
    print(*loglist, sep=" ")
    print("2-Approximation:", end= " ")
    print(*twolist, sep=" ")
    print("Exact Solution:", end= " ")
    print(*blist, sep=" ")

if __name__ == "__main__":
    main()