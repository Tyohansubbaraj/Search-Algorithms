from columnar import columnar

class BMS:

    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        
        for i,j,_ in self.edges:
            if i not in self.graph_dict:
                self.graph_dict[i] = [j]
            else:
                self.graph_dict[i].append(j)



    def algorithmBMS(self,start,end,path = []):
        paths = []
        
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []
        
        sorted_nodes = sorted(self.graph_dict[start])                #BMS uses Lexicographical Sorting/Minimum Value to visit next node


        for node in sorted_nodes:
            if node not in path:                                     #Preventing the program from going back to the visited node
                new_paths = self.algorithmBMS(node,end,path)

                for p in new_paths:
                    paths.append(p)
        
        return paths

    def showPathBMS(self,start,end):

        paths = self.algorithmBMS(start,end)

        headers = ['Paths']
        data = [[i] for i in paths]
        table = columnar(headers=headers,data=data)
        print("Paths derived by British Museum Search Algorithm: ")
        print(table)

