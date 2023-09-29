from pyvis.network import Network



class CreateGraph:

    def __init__(self):
        self.g = Network(height="750px",width="1450px")
        self.edge_list = []
        
    def addNodes(self):
        
        n = int(input("Enter the number of nodes that are in the graph: "))

        for _ in range(n):
            self.g.add_node(input("Enter node name: "))
        
        
    def addEdges(self):
        
        n = int(input("Enter The Number Of Connections: "))

        for _ in range(n):

            first_node = input("Enter The First Node: ")
            second_node = input("Enter The Second Node: ")
            cost = int(input("Enter The Edge Cost: "))

            try:
                self.g.add_edge(first_node,second_node,label=str(cost))
                self.edge_list.append((first_node,second_node,cost))
                print("Connection Added")
                

            except:
                print("Invalid Connection")

        return self.edge_list

    def driver(self):
        self.g.show("Create.html",notebook=False)

class DisplayGraph:

    def __init__(self,edge_list):
        
        self.g = Network(height="750px",width="1450px")
        self.edge_list = [i[:2] for i in edge_list]
        self.cost_list = [str(i[-1]) for i in edge_list]
        self.nodes = ()
        for i in self.edge_list:
            if i[0] not in self.nodes:
                self.nodes= self.nodes+(i[0],)
            if i[1] not in self.nodes:
                self.nodes= self.nodes+(i[1],)

    def showGraph(self):

        for i in self.nodes:
            self.g.add_node(str(i))
        for i,j in zip(self.edge_list,self.cost_list):
            self.g.add_edge(i[0],i[1],label=j)
        self.g.show('Graph.html',notebook=False)

class PathGraph:

    def __init__(self,edge_list):
        
        self.g = Network(height="750px",width="1450px")
        self.edge_list_with_cost = edge_list
        self.edge_list = [i[:2] for i in edge_list]
        self.cost_list = [i[-1] for i in edge_list]
        self.nodes = ()
        for i in self.edge_list:
            if i[0] not in self.nodes:
                self.nodes= self.nodes+(i[0],)
            if i[1] not in self.nodes:
                self.nodes= self.nodes+(i[1],)
        

    def showPathGraph(self,path):

        edges = [(path[i],path[i+1]) for i in range(len(path)-1)]
        path_cost = [i[-1] for i in self.edge_list_with_cost if i[:2] in edges]
        non_path_nodes = [i for i in self.nodes if i not in path]
        non_path_edges_with_cost = [i for i in self.edge_list_with_cost if i[:2] not in edges]
        non_path_edges = [i[:2] for i in non_path_edges_with_cost]
        non_path_cost = [i[-1] for i in non_path_edges_with_cost]

        self.g.add_nodes(non_path_nodes,color=['#0000FF']*len(non_path_nodes))
        self.g.add_nodes(path,color=['#FFC0CB']*len(path))
        for i,j in zip(non_path_edges,non_path_cost):
            self.g.add_edge(i[0],i[1],label=str(j))
        for i,j in zip(edges,path_cost):
            self.g.add_edge(i[0],i[1],label=str(j))

        self.g.add_node('NON PATH NODE',color='#0000FF',x=-350,y=-450,fixed=True,physics=False)
        self.g.add_node('PATH NODE',color='#FFC0CB',x=-350,y=-550,fixed=True,physics=False)

        self.g.show('Path.html',notebook=False)