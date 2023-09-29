from GraphVis import PathGraph

class DFS:

    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        self.check = 0
        
        for i,j,_ in self.edges:
            if i not in self.graph_dict:
                self.graph_dict[i] = [j]
            else:
                self.graph_dict[i].append(j)

    def algorithmDFS(self,start,end,path = []):
        
        paths = []
        
        if self.check==1:                                            #If path is found then this exits the recurrsion and returns the path
            return paths

            
        path = path + [start]


        if start == end:                                             #Similar to BMS, but stops once the goal node is found
            self.check = 1
            return path
        
        
        if start not in self.graph_dict:
            return []

        sorted_nodes = sorted(self.graph_dict[start])                #DFS uses Lexicographical Sorting/Minimum Value to visit next node


        for node in sorted_nodes:
            if node not in path:
                new_paths = self.algorithmDFS(node,end,path)
                for p in new_paths:
                    paths.append(p)
        
        return paths

    def showPathDFS(self,start,end):

        paths = self.algorithmDFS(start,end)

        p = PathGraph(self.edges)

        p.showPathGraph(paths)