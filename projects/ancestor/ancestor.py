# from util import Stack, Queue

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        verts = self.vertices
        if verts.get(vertex) == None:
            verts[vertex] = set()

    def add_parents(self, v1, v2):
        verts = self.vertices
        if v1 not in verts:
            self.add_vertex(v1)
        if v2 not in verts:
            self.add_vertex(v2)
        if v1 in verts and v2 in verts:
            verts[v2].add(v1)

    def new_edge(self, vertex, visited):
        return [i for i in self.vertices.get(vertex) if i not in visited]

    def earliest_ancestor(self, child):
        verts = self.vertices

        queue = [[child]]
        visited = {child}
        ancestors = []

        for i in range(len(verts)):
            try:
                path = queue.pop(0)
                visit = path[-1]
                visited.add(visit)
                branch = set(self.new_edge(visit, visited))
                if len(branch) == 0:
                    ancestors.append(path)
                else:
                    for i in branch:
                        queue.append(path + [i])
            except IndexError:
                longest_lineage = max([len(i) for i in ancestors])
                earliest_ancestors = [i for i in ancestors if len(i) >= longest_lineage]
                earliest_ancestor = min([i[-1] for i in earliest_ancestors])
                break

        if earliest_ancestor == child:
            earliest_ancestor = -1


        print(earliest_ancestor)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph

    graph.add_parents(1, 3)
    graph.add_parents(2, 3)
    graph.add_parents(3, 6)
    graph.add_parents(5, 6)
    graph.add_parents(5, 7)
    graph.add_parents(4, 5)
    graph.add_parents(4, 8)
    graph.add_parents(8, 9)
    graph.add_parents(11, 8)
    graph.add_parents(10, 1)


    print(graph.vertices)
    graph.earliest_ancestor(6) # 10
    graph.earliest_ancestor(9) # 4
    graph.earliest_ancestor(11) # No parent, returns -1
  