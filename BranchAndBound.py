from GraphVis import PathGraph
from Oracle import Oracle

class BranchAndBound:

    def __init__(self,edge_with_cost,oracle):

        self.edges = edge_with_cost
        self.graph_dict = {}
        self.oracle = oracle
        self.check = 0
        self.ignore = []
        for i,j,k in self.edges:
            if i not in self.graph_dict:
                self.graph_dict[i] = [[k,j]]
            else:
                self.graph_dict[i].append([k,j])
    
    def algorithmBranchAndBound(self,start,end,path = []):

        paths = []

        if self.check==1:                                            #If path is found then this exits the recurrsion and returns the path
            return paths
    
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

        sorted_nodes = sorted(self.graph_dict[start])                #DFS uses Lexicographical Sorting/Minimum Value to visit next node

        for node in sorted_nodes:
            if node[1] not in path:

                new_paths = self.algorithmBranchAndBound(node[1],end,path)
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
    
    def showPathsBranchAndBound(self,start,end):

        paths = self.algorithmBranchAndBound(start,end)

        p = PathGraph(self.edges)

        p.showPathGraph(paths[1:])
