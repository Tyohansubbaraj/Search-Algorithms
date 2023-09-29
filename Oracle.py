from columnar import columnar
from copy import deepcopy

class Oracle:

    def __init__(self,edge_with_cost):

        self.edges = edge_with_cost
        self.graph_dict = {}
        for i,j,k in self.edges:
                if i not in self.graph_dict:
                    self.graph_dict[i] = [[k,j]]
                else:
                    self.graph_dict[i].append([k,j])
    
    def algorithmOracle(self,start,end,path = []):
        
        paths = []
        
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []
        
        nodes = sorted(self.graph_dict[start])

        for node in nodes:
            
            if node[1] not in path:
                new_paths = self.algorithmOracle(node[1],end,path)
                for p in new_paths:
                    paths.append(p)

        return paths
        
    def showPathsOracle(self,start,end):

        paths = self.algorithmOracle(start,end)

        costPath = []

        for i in paths:
            cost = 0
            for j in range(len(i)-1):
                key = i[j]
                value = i[j+1]

                for k in self.graph_dict[key]:
                    if value in k:
                        cost += k[0]
            costPath.append(cost)

        temp = list(zip(costPath,paths))

        temp = sorted(temp)

        print("Paths ranked from best to worst based on cost: ")
        headers = ['Paths','Cost']
        data = [[i[1],i[0]] for i in temp]

        table = columnar(headers=headers,data=data)

        oracle = [temp[0][0]] + temp[0][1]

        print(table)

        return oracle

    def getOracle(self,start,end):

        paths = self.algorithmOracle(start,end)

        costPath = []

        for i in paths:
            cost = 0
            for j in range(len(i)-1):
                key = i[j]
                value = i[j+1]

                for k in self.graph_dict[key]:
                    if value in k:
                        cost += k[0]
            costPath.append(cost)

        temp = list(zip(costPath,paths))
        temp = sorted(temp)
        oracle = [temp[0][0]] + temp[0][1]
        return oracle