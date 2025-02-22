# Hierarchical Path Finder | An Efficient Common Ancestor Search in Tree Structures

This project involves the creation and traversal of a tree-like data structure that represents hierarchical relationships between entities. The primary goal is to efficiently find the common ancestor between two entities within the tree, using a depth-first search approach to locate nodes and calculate paths.

## Key Features

- **Tree Structure Representation**: The tree is composed of nodes where each node represents an entity (e.g., a species, item, or concept) and can have multiple child nodes. The root node serves as the starting point of the tree.

- **Node Navigation**: Each node in the tree has references to its parent and children, allowing for bidirectional traversal.

- **Path Finding**: The core functionality of this project is to find the common ancestor between two specified nodes. This is achieved by tracing both paths from the given nodes to the root and determining the first common ancestor.

- **Efficient Depth Search**: The system ensures optimal traversal by leveraging the depth of the nodes to minimize unnecessary operations and directly compare nodes at the same level in the hierarchy.

- **Hierarchical Data Handling**: The system allows for dynamic tree modification by adding new child nodes under a specified parent, simulating hierarchical relationships and their evolution over time.

## Purpose

The purpose of this project is to simulate and analyze hierarchical structures, such as family trees, organizational charts, or classification systems, where it is important to track relationships between entities and determine their connections or shared origins.

This project can be applied to a variety of domains, including biology (e.g., taxonomy or phylogenetic trees), data organization (e.g., file systems or organizational structures), or any other context where entities have parent-child relationships.

The main functionality of this project is to identify the path between two nodes by finding their common ancestor and efficiently outputting the hierarchical path from one node to the other.

