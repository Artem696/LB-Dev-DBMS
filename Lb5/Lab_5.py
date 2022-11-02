import sys

class Graph:
    def __init__(self,n):
        self.count_nodes = n
        self.graph = {}
        self.short_path = {}
    def construct_graph(self,path):
        if len(self.graph)==0:
            self.graph[path[0]] = {}
            self.graph[path[0]][path[1]] = path[2]
        else:
            if path[0] not in self.graph.keys():
                self.graph[path[0]] = {}
                if len(path)>1:
                    self.graph[path[0]][path[1]] = path[2]
            else:
                self.graph[path[0]][path[1]] = path[2]
    def check(self,start_node,target_node):
        if start_node not in self.graph.keys():
            print(f"Вершины {start_node} не существует в графе")
            return False
        elif target_node not in self.graph.keys():
            print(f"Вершины {target_node} не существует в графе")
            return False
        else:
            return True
    def dijkstra_algorithm(self,start_node,target_node):
        if self.check(start_node,target_node):
            for node in self.graph.keys():
                self.short_path[node] = sys.maxsize
            self.short_path[start_node] = 0
            unvisited_nodes = []
            previous_nodes = {}
            for i in self.graph.keys():
                unvisited_nodes.append(i)
            unvisited_nodes[0] = start_node
            while unvisited_nodes:
                current_min = None
                for node in unvisited_nodes:
                    if current_min == None:
                        current_min = node
                    if self.short_path[node]<self.short_path[current_min]:
                        current_min = node
                neighbpurs = self.graph[current_min].keys()
                for neighbpur in neighbpurs:
                    temp_value = self.short_path[current_min] + self.graph[current_min][neighbpur]
                    if self.short_path[neighbpur]>temp_value:
                        self.short_path[neighbpur] = temp_value
                        previous_nodes[neighbpur] = current_min
                unvisited_nodes.remove(current_min)
            path = []
            node = target_node
            if node not in previous_nodes:
                print("Невозможно достичь указанной вершины, т.к. отсутсвует необходимый путь")
            else:
                path.append(target_node)
                while node != start_node:
                    path.append(previous_nodes[node])
                    node = previous_nodes[node]
                print("Короткий путь: " + " -> ".join(str(x) for x in reversed(path)))
                print(f"Длина пути: {self.short_path[target_node]}")


graph = Graph(10)
graph.construct_graph([1,3,7])
#graph.construct_graph([1,6,9])
graph.construct_graph([1,9,2])
graph.construct_graph([1,10,14])
graph.construct_graph([2,4,5])
graph.construct_graph([2,9,11])
graph.construct_graph([3,4,18])
graph.construct_graph([3,8,4])
graph.construct_graph([4,5,10])
#graph.construct_graph([4,6,8])
graph.construct_graph([5,8,15])
#graph.construct_graph([6,7,12])
graph.construct_graph([7,2,21])
graph.construct_graph([8,10,6])
graph.construct_graph([9])
graph.construct_graph([10])
graph.dijkstra_algorithm(1,7)
