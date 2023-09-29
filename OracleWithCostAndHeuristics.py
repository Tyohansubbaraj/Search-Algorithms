from columnar import columnar
from copy import deepcopy

class OracleWithCostAndHeuristics:
    
    def __init__(self,edge_with_cost):

        self.edges = edge_with_cost
        self.graph_dict = {}
        self.Heuristics = {}
        for i,j,k in self.edges:
            if i not in self.graph_dict:
                self.graph_dict[i] = [[k,j]]
            else:
                self.graph_dict[i].append([k,j])
        
        for i in edge_with_cost:
            for j in i[:2]:
                if j not in self.Heuristics:
                    self.Heuristics[j] = 0
        
        self.getHeuristics()
        
    def getHeuristics(self):                                         #Getting Heuristic values from the user
        for i in self.Heuristics:
            self.Heuristics[i]=int(input(f'Enter the Heuristic value for {i}: '))


    
    def algorithmOracleWithCostAndHeuristics(self,start,end,path = []):
        
        paths = []
        
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []
        
        nodes_with_cost = deepcopy(self.graph_dict[start])

        for i in nodes_with_cost:
            i[0] += self.Heuristics[i[1]]

        nodes = sorted(nodes_with_cost)

        for node in nodes:
            
            if node[1] not in path:
                new_paths = self.algorithmOracleWithCostAndHeuristics(node[1],end,path)
                for p in new_paths:
                    paths.append(p)

        return paths
    

    def showPathsOracle(self,start,end):

        paths = self.algorithmOracleWithCostAndHeuristics(start,end)

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

        paths = self.algorithmOracleWithCostAndHeuristics(start,end)

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
        return oracle,self.Heuristics