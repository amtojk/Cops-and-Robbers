#### Algorithm for determining if a graph is cop-win in Python
#### By: Amtoj Kaur
#### This algorithm inspired by the code by Jeremie Turcotte, see https://github.com/tjeremie/Cops-and-robbers/blob/master/Cop%20number/Dismantlable_graphs.wl
#### This code uses the equivalence relation between cop-win and dismantlable graphs, see Theorem 1.1 in https://math.ryerson.ca/~pralat/papers/2012_cop-win.pdf
#### The code begins on line 11
#### Lines 11-28 are from https://python-course.eu/examples/graph2.py 




class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice):
        """ returns a list of all the edges of a vertice"""
        return self._graph_dict[vertice]
       
    def all_vertices(self):
        """ returns the vertices of a graph as a set """
        return set(self._graph_dict.keys())
   
   
    def find_subset(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to
            end_vertex in graph """
        graph = self._graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,
                                                     end_vertex,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths
       
    def neighbourhood(self, start_vertex, neighbourhood=[]):
        graph=self._graph_dict
        neighbourhood=list(start_vertex)
        for key in graph:
            if start_vertex==key:
                return list(graph[start_vertex])+neighbourhood
        print("No corresponding value found! Initiating return...")
        return None
    
    def del_vertex(self, k):
        for i in range(self.V):
            temp=self.graph[i]
            if i==k:
                while temp:
                    self.graph[i]=temp.next
                    temp=self.graph[i]
            # Delete the vertex 
            # using linked list concept        
            if temp:
                if temp.vertex == k:
                    self.graph[i]= temp.next
                    temp = None
            while temp:
                if temp.vertex == k:
                    break
                prev = temp
                temp = temp.next
  
            if temp == None:
                continue
  
            prev.next = temp.next
            temp = None   
       
g= { "a" : {"b","c"},
      "b" : {"a","c","d"},
      "c" : {"a", "b","d"},
      "d" : {"b","c"},
}


graph_dict = g
graph=Graph(g)

#Find neighbourhoods
verticeslist = graph.all_vertices()
verticeslist = list(verticeslist)
N = []

for vertice in range(len(verticeslist)):
    N.append(set(graph.neighbourhood(verticeslist[vertice])))

def flagging(neighbourhood_set, verticeslist):
    flagged = []
    subset = True #Condition to run code if subset is present. Tells function when it is unable to flag
    for n, elem in enumerate(neighbourhood_set): #Go through the set
        thiselem = elem
        for i in range(len(neighbourhood_set)): #compare elem with whole set
            if neighbourhood_set[i] != thiselem: #dont compare against itself
                x = elem.issubset(neighbourhood_set[i])
                if x == True:
                    #flagged.append(elem)
                    flagged.append(verticeslist[n])
                    neighbourhood_set.remove(neighbourhood_set[n])
                    for j in range(len(neighbourhood_set)):
                        if verticeslist[n] in neighbourhood_set[j]:
                            neighbourhood_set[j].remove(verticeslist[n])
                    verticeslist.remove(verticeslist[n])
                    return flagged, neighbourhood_set, verticeslist, subset      
    subset = False
    return flagged, neighbourhood_set, verticeslist, subset        


#Find neighbourhoods
verticeslist = graph.all_vertices()
verticeslist = list(verticeslist)
N = []

for vertice in range(len(verticeslist)):
    individuallist = set(graph.neighbourhood(verticeslist[vertice]))
    #individuallist.remove(verticeslist[vertice])
    N.append(individuallist)
   
#Running code
flaglist = []
flag, newlist, newverticeslist, subsetcheck = flagging(N, verticeslist)

while subsetcheck == True:
    flaglist.append(flag)
    flag, newlist, newverticeslist, subsetcheck = flagging(newlist, newverticeslist)

if len(newlist)<=3: #connected graph of length 3 or less is cop-win
    print('Yes, the graph is cop-win')
else:
    print('No, the graph is not cop-win')
