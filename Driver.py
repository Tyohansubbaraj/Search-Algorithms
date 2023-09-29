from BMS import BMS
from DFS import DFS
from BFS import BFS
from HillClimbing import HillClimbing
from Oracle import Oracle
from BranchAndBound import BranchAndBound
from BranchAndBoundWithExtendedList import BranchAndBoundWithExtendedList
from OracleWithCostAndHeuristics import OracleWithCostAndHeuristics
from BranchAndBoundWithCostAndHeuristics import BranchAndBoundWithCostAndHueristics
from A_Star import A_Star
from GraphVis import CreateGraph,DisplayGraph

def main():
    
    # g=CreateGraph()
    # g.addNodes()
    # edge_list = g.addEdges()

    # d = DisplayGraph(edge_list)
    # d.showGraph()
    edge_list = [('S', 'A', 3), ('S', 'B', 4), ('A', 'B', 2), ('B', 'A', 2), ('A', 'D', 4), ('D', 'F', 2), ('F', 'G', 1), ('B', 'C', 5), ('C', 'E', 6)]


    while True:

        text = """SEARCH ALGORITHMS
1.  British Museum Search
2.  Depth First Search
3.  Breadth First Search
4.  Hill Climbing
5.  Oracle
6.  Branch And Bound
7.  Branch And Bound With Extended List
8.  Orace With Cost And Heurisitics
9.  Branch And Bound With Cost And Heurisitics
10. A Star
11. Exit
CHOICE: """
        
        choice = int(input(text))

        start = input("Enter Start Node: ")
        end = input("Enter Goal Node: ")

        if choice == 1:

            gBMS = BMS(edge_list)
            gBMS.showPathBMS(start,end)
        
        elif choice == 2:

            gDFS = DFS(edge_list)
            gDFS.showPathDFS(start,end)
        
        elif choice == 3:

            gBFS = BFS(edge_list)
            gBFS.showPathBFS(start,end)

        elif choice == 4:

            gHC = HillClimbing(edge_list)
            gHC.showPathHillClimbing(start,end)
        
        elif choice == 5:

            gOR = Oracle(edge_list)
            gOR.showPathsOracle(start,end)
        
        elif choice == 6:

            gOR = Oracle(edge_list)
            oracle = gOR.getOracle(start,end)
            gBnB = BranchAndBound(edge_list,oracle)
            gBnB.showPathsBranchAndBound(start,end)
        
        elif choice == 7:
            gOR = Oracle(edge_list)
            oracle = gOR.getOracle(start,end)
            gBnBwEL = BranchAndBoundWithExtendedList(edge_list,oracle)
            gBnBwEL.showPathsBranchAndBoundWithExtendedList(start,end)

        elif choice == 8:

            gORCH = OracleWithCostAndHeuristics(edge_list)
            gORCH.showPathsOracle(start,end)
        
        elif choice == 9:

            gORCH = OracleWithCostAndHeuristics(edge_list)
            oracle , heurisitcs = gORCH.getOracle(start,end)
            gBnBCH = BranchAndBoundWithCostAndHueristics(edge_list,oracle,heurisitcs)
            gBnBCH.showPathBranchAndBoundWithCostAndHueristics(start,end)
        
        elif choice == 10:

            gORCH = OracleWithCostAndHeuristics(edge_list)
            oracle , heurisitcs = gORCH.getOracle(start,end)
            gAStar = A_Star(edge_list,oracle,heurisitcs)
            gAStar.showPathsA_Star(start,end)
        
        elif choice == 11:
            print("Exiting")
            break
    
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
    