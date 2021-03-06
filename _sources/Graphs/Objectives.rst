..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner
    This work is licensed under the Creative Commons
    Attribution-NonCommercial-ShareAlike 4.0 International License. To view a
    copy of this license, visit
    http://creativecommons.org/licenses/by-nc-sa/4.0/.


Objectives
----------

-  To learn what a graph is and how it is used.

-  To implement the **graph** abstract data type using multiple internal
   representations.

-  To see how graphs can be used to solve a wide variety of problems

In this chapter we will study graphs. Graphs are a more general structure than
the trees we studied in the last chapter; in fact you can think of a tree as a
special kind of graph. Graphs can be used to represent many interesting things
about our world, including systems of roads, airline flights from city to city,
how the Internet is connected, or even the sequence of classes you must take to
complete a major in computer science. We will see in this chapter that once we
have a good representation for a problem, we can use some standard graph
algorithms to solve what otherwise might seem to be a very difficult problem.

While it is relatively easy for humans to look at a road map and understand the
relationships between different places, a computer has no such knowledge.
However, we can also think of a road map as a graph.  When we do so we can have
our computer do interesting things for us. If you have ever used one of the
Internet map sites, you know that a computer can find the shortest, quickest,
or easiest path from one place to another.

As a student of computer science you may wonder about the computer science and
mathematics courses you can take at your college. A graph is good way to
represent the interdependencies among courses.  :ref:`Figure 1 <fig1>` shows
such a graph. This one represents most of the available CS and math courses at
Northern Virginia Community College and the order in which they must be taken.

.. _fig1:

.. figure:: Figures/CS-Prereqs.png
    :align: center

    Figure 1: Available Computer Science and Mathematics Courses

