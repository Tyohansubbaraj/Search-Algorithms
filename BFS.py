from GraphVis import PathGraph

class BFS:

    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        
        for i,j,_ in self.edges:
            if i not in self.graph_dict:
                self.graph_dict[i] = [j]
            else:
                self.graph_dict[i].append(j)


    def algorithmBFS(self,start,end):

        queue = []                                                   #BFS Uses queues to implement level-wise searching
        queue.append([start])

        while queue:
            
            temp = queue.pop(0)
            if temp[-1]==end:                                        #Last element in the list is used to check if we have reached the goal
                return temp
            
            if temp[-1] not in self.graph_dict:
                continue
            
            sorted_nodes = sorted(self.graph_dict[temp[-1]])         #Visiting the neighbors of the recently visited node

            for node in sorted_nodes:
                temp2 = list(temp)
                temp2.append(node)                                   #Adding the the neighbor to the path
                queue.append(temp2)                                  #Adding new path to the queue

    def showPathBFS(self,start,end):

        paths = self.algorithmBFS(start,end)

        p = PathGraph(self.edges)

        p.showPathGraph(paths)
