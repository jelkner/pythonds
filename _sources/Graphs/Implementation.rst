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
connected, and the weight of each edge. This dictionary is called
``connected_to``. The listing below shows the code for the ``Vertex`` class. The
constructor simply initializes the ``id``, which will typically be a string,
and the ``connected_to`` dictionary. The ``add_neighbor`` method is used add a
connection from this vertex to another. The ``connections`` method returns
all of the vertices in the adjacency list, as represented by the
``connected_to`` instance variable. The ``weight`` method returns the weight
of the edge from this vertex to the vertex passed as a parameter.

.. _lst_vertex:

**Listing 1**

::

    class Vertex:
        def __init__(self, key):
            self.id = key
            self.connected_to = {}

        def add_neighbor(self, nbr, weight=None):
            self.connected_to[nbr] = weight

        def __str__(self):
            return str(self.id) + ' connected_to: ' + \
                       str([x.id for x in self.connected_to])

        def connections(self):
            return self.connected_to.keys()

        def id(self):
            return self.id

        def weight(self, nbr):
            return self.connected_to[nbr]

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
            self.num_vertices = 0
            
        def add_vertex(self, key):
            self.num_vertices = self.num_vertices + 1
            new_vertex = Vertex(key)
            self.vert_list[key] = new_vertex
            return new_vertex
        
        def get_vertex(self, n):
            if n in self.vert_list:
                return self.vert_list[n]
            else:
                return None

        def __contains__(self, n):
            return n in self.vert_list
        
        def add_edge(self, f, t, cost=None):
            if f not in self.vert_list:
                nv = self.add_vertex(f)
            if t not in self.vert_list:
                nv = self.add_vertex(t)
            self.vert_list[f].add_neighbor(self.vert_list[t], cost)
        
        def get_vertices(self):
            return self.vert_list.keys()
            
        def __iter__(self):
            return iter(self.vert_list.values())

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
    ...    g.add_vertex(i)
    >>> g.vert_list
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
