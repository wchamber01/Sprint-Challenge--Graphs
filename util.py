class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        From v1 to v2
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist in graph')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # Define the queue and initialize the starting vertex
        q = Queue()
        q.enqueue(starting_vertex)

        # Keep track of visited nodes
        visited = set()

        # Repeat until queue is empty
        while q.size() > 0:

            # Dequeue first vertex i.e: remove from queue
            vertex = q.dequeue()

            # Have we visited the vertex yet? If not then visit it.
            if vertex not in visited:
                print(vertex)

                # Add visited vertex to visited list
                visited.add(vertex)

                # Do this for all vertices in the queue
                for next_vert in self.get_neighbors(vertex):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Define the stack and initialize the starting vertex
        s = Stack()
        s.push(starting_vertex)

        # Keep track of visited nodes
        # visited = {starting_vertex}
        visited = set()

        # Repeat until stack is empty
        while s.size() > 0:

            # Pop first vertex - remove from stack
            vertex = s.pop()
            # print(vertex)

            # Have we visited the vertex yet? If not then visit it.
            if vertex not in visited:
                print(vertex)
                # Add visited to visited list
                visited.add(vertex)
                # Do this for all vertices in the stack
                for next_vert in self.vertices[vertex]:
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)

        if visited is None:
            visited = set()

        visited.add(starting_vertex)

        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        vertex = [starting_vertex]
        q.enqueue(vertex)

        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            path_end = path[-1]
            if path_end == destination_vertex:
                return path
            if path_end not in visited:
                visited.add(path_end)
                for neighbor in self.get_neighbors(path_end):
                    q.enqueue(path + [neighbor])
                    # visited.add(vertex)
                # return next_vert
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        path = [starting_vertex]
        s.push(path)
        visited = set()

        while s.size() > 0:
            vertex = s.pop()
            end = vertex[-1]
            if end == destination_vertex:
                return vertex
            if end not in visited:
                visited.add(end)
                for neighbor in self.vertices[end]:
                    s.push(vertex + [neighbor])
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        print(starting_vertex)

        if visited is None:
            visited = set()

        if path is None:
            path = []

        visited.add(starting_vertex)

        # Make a copy  of the list, adding on the new vertex (different than append)
        path = path + [starting_vertex]

        # Base case
        if starting_vertex == destination_vertex:
            return path

        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(
                    child_vert, destination_vertex, visited, path)

                if new_path:
                    return new_path

        return None
