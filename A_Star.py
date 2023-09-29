from copy import deepcopy
from GraphVis import PathGraph

class A_Star:
    
    def __init__(self,edge_with_cost,oracle,heu):

        self.edges = edge_with_cost
        self.graph_dict = {}
        self.Heuristics = heu
        self.visited = []
        self.check = 0
        self.oracle = oracle
        for i,j,k in self.edges:
            if i not in self.graph_dict:
                self.graph_dict[i] = [[k,j]]
            else:
                self.graph_dict[i].append([k,j])


    def algorithmA_Star(self,start,end,path = []):
        
        paths = []

        if self.check==1:                                            #If path is found then this exits the recurrsion and returns the path
            return paths
    
        if start in self.visited:
            return path
        else:
            self.visited.append(start)
            path = path + [start]

        if start == end:                                             #Similar to BMS, but stops once the goal node is found
            if (self.oracle[0] == self.calcCost(path)):                                             
                self.check = 1
                path.insert(0,self.calcCost(path))
                return path
            else:
                return []
        
                
        if start not in self.graph_dict:
            return []

        nodes_with_cost = deepcopy(self.graph_dict[start])

        for i in nodes_with_cost:
            i[0] += self.Heuristics[i[1]]

        nodes = sorted(nodes_with_cost)

        for node in nodes:
            
            if node[1] not in path:
                new_paths = self.algorithmA_Star(node[1],end,path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def calcCost(self,path):
        cost = 0
        for i in range(len(path)-1):
            key = path[i]
            value = path[i+1]

            for k in self.graph_dict[key]:
                if value in k:
                    cost += k[0]
        
        return cost
    
    def showPathsA_Star(self,start,end):

        paths = self.algorithmA_Star(start,end)

        p = PathGraph(self.edges)

        p.showPathGraph(paths[1:])
