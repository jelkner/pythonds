..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner
    This work is licensed under the Creative Commons
    Attribution-NonCommercial-ShareAlike 4.0 International License. To view a
    copy of this license, visit
    http://creativecommons.org/licenses/by-nc-sa/4.0/.


Implementation
~~~~~~~~~~~~~~

Using dictionaries, it is easy to implement the adjacency list in Python. In
our implementation of the Graph abstract data type we will create two classes
(see :ref:`Listing 1 <lst_vertex>` and :ref:`Listing 2 <lst_graph>`),
``Graph``, which holds the master list of vertices, and ``Vertex``, which will
represent each vertex in the graph.

Each ``Vertex`` uses a dictionary to keep track of the vertices to which it is
connected, and the weight of each edge. If weights are not needed, a set could
be used instead of a dictionary. In order to handle both cases, a dictionary
called ``neighbors`` is used, but it is given a default value of ``None``.

The listing below shows the code for the ``Vertex`` class. The initialization
method simply initializes the ``key``, which will typically be a string,
and the ``neighbors`` dictionary. The ``add_neighbor`` method is used add a
connection from this vertex to another. The ``connections`` method returns
all of the vertices in the adjacency list, as represented by the ``neighbors``
instance variable. The ``weight`` method returns the weight of the edge from
this vertex to the vertex passed as a parameter, or ``None`` if it is not set.

.. _lst_vertex:

**Listing 1**

::

    class Vertex:
        def __init__(self, key):
            self.key = key
            self.neighbors = {}

        def add_neighbor(self, neighbor, weight=None):
            self.neighbors[neighbor] = weight

        def __str__(self):
            return '{} neighbors: {}'.format(
                self.key,
                [x.key for x in self.neighbors]
            )

        def get_connections(self):
            return self.neighbors.keys()

        def get_weight(self, neighbor):
            return self.neighbors[neighbor]

The ``Graph`` class, shown in the next listing, contains a dictionary that maps
vertex names to vertex objects. In :ref:`Figure 4 <fig_adjlist>` this
dictionary object is represented by the shaded gray box. ``Graph`` also
provides methods for adding vertices to a graph and connecting one vertex to
another. The ``get_vertices`` method returns the names of all of the vertices in
the graph. In addition, we have implemented the ``__iter__`` method to make it
easy to iterate over all the vertex objects in a particular graph. Together,
the two methods allow you to iterate over the vertices in a graph by name, or
by the objects themselves.

.. _lst_graph:

**Listing 2**

::

    class Graph:
        def __init__(self):
            self.vert_list = {}

        def add_vertex(self, vertex):
            self.vertices = [vertex.key] = vertex 

        def get_vertex(self, key):
            if key in self.verticies[key]:
                return self.verticies[key]
            else:
                return None

        def __contains__(self, key):
            return key in self.verticies
        
        def add_edge(self, from_key, to_key, weight=None):
            if from_key not in self.verticies:
                self.add_vertex(Vertex(from_key))
            if to_key not in self.verticies:
                self.add_vertex(Vertex(to_key))
            self.verticies[from_key].add_neighbor(
                self.verticies[to_key],
                weight
            )
        
        def get_vertices(self):
            return self.verticies.keys()
            
        def __iter__(self):
            return iter(self.verticies.values())


Using the ``Graph`` and ``Vertex`` classes just defined, the following Python
session creates the graph in :ref:`Figure 2 <fig_dgsimple>`. First we create
six vertices numbered 0 through 5. Then we display the vertex dictionary.
Notice that for each key 0 through 5 we have created an instance of a
``Vertex``. Next, we add the edges that connect the vertices together. Finally,
a nested loop verifies that each edge in the graph is properly stored. You
should check the output of the edge list at the end of this session against
:ref:`Figure 2 <fig_dgsimple>`.

::

    >>> g = Graph()
    >>> for i in range(6):
    ...    g.add_vertex(Vertex(i))
    >>> g.verticies
    {0: <graphs.Vertex object at 0x7f8e3b60ff98>,
    1: <graphs.Vertex object at 0x7f8e3b633b70>,
    2: <graphs.Vertex object at 0x7f8e3b633e80>,
    3: <graphs.Vertex object at 0x7f8e3b633f60>,
    4: <graphs.Vertex object at 0x7f8e3b633f98>,
    5: <graphs.Vertex object at 0x7f8e3b633fd0>}
    >>> g.add_edge(0, 1, 5)
    >>> g.add_edge(0, 5, 2)
    >>> g.add_edge(1, 2, 4)
    >>> g.add_edge(2, 3, 9)
    >>> g.add_edge(3, 4, 7)
    >>> g.add_edge(3, 5, 3)
    >>> g.add_edge(4, 0, 1)
    >>> g.add_edge(5, 4, 8)
    >>> g.add_edge(5, 2, 1)
    >>> for v in g:
    ...    for w in v.connections(): 
    ...        print("({}, {})".format(v.id, w.id))
    ... 
    (0, 5)
    (0, 1)
    (1, 2)
    (2, 3)
    (3, 4)
    (3, 5)
    (4, 0)
    (5, 4)
    (5, 2)
