from GraphVis import PathGraph

class HillClimbing:

    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        self.check = 0
        
        for i,j,_ in self.edges:
            if i not in self.graph_dict:
                self.graph_dict[i] = [j]
            else:
                self.graph_dict[i].append(j)
        
        self.Heuristics = {}

        for i,j,_ in edges:
            if i not in self.Heuristics:
                self.Heuristics[i]=0
            elif j not in self.Heuristics:
                self.Heuristics[j]=0
            else:
                continue
        
        self.getHeuristics()

    
    def getHeuristics(self):                                     #Getting Heuristic values from the user
        for i in self.Heuristics:
            self.Heuristics[i]=int(input(f'Enter the Heuristic value for {i}: '))

    def algorithmHillClimbing(self,start,end,path = []):
        
        paths = []
    
        if self.check==1:                                        #If path is found then this exits the recurrsion and returns the path
            return paths

            
        path = path + [start]


        if start == end:                                         #Stops the algorithm once goal is reached
            self.check = 1
            return path
        
        
        if start not in self.graph_dict:
            return []   

        sorted_nodes = sorted(self.graph_dict[start])
        Heuristics_nodes = [self.Heuristics[i] for i in sorted_nodes]

        temp = zip(Heuristics_nodes,sorted_nodes)                #Zipping lists to sort them based on Heuristic value
        temp = sorted(list(temp))
        sorted_nodes  = [i[1] for i in temp]                     #Taking only the sorted nodes from the zipped lists

        for node in sorted_nodes:
            if node not in path:
                new_paths = self.algorithmHillClimbing(node,end,path)
                for p in new_paths:
                    paths.append(p)

        return paths
    
    def showPathHillClimbing(self,start,end):

        paths = self.algorithmHillClimbing(start,end)

        p = PathGraph(self.edges)

        p.showPathGraph(paths)