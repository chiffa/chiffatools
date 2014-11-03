A handy toolbox of various python functions, classes and wrappers:
=================================================================

General tools:
**************

 * ConfigParsers : tools for handy parsing of the .ini functions. Instead of costum data structure returns a dict
 * Dataviz: a set of somewhat more involved functions for data showing
        * violin plot
        * better 2-D density plot
        
 * Dictionary comparator: fuzzy dictionary comparator
 * Linalg routines: useful, but somewhat uncommon linear algebra operations
 * GDF exprot: converts a matrix representation of a graph to a GDF format, plus assigns properties to all the nodes. 
 * Xml Doctor: a tool that is usefull to inspect what is truly contained in an xml file: number of class instances, fields for each instance and classes of fields. The one here has been optimzied for Reactome BioPax Lvl3 analysis
 * Matrix 2D embedding: transform a distance matrix to a 2-D representation.
 * buffered methods : a set of methods for rapid dumping/undumping of objects that need to be injected into a class to make it buffered. usefull for rapid iterations on classes with long intermediary computation times.
 
Tools specific to bioinformatics:
*********************************
 
 * Uniprot/Go structure parsers : useful parsers for biology that parse aliases and relations to a dict format. 



author : chiffa@github.commatrix_2D_embedding.py
Some of the tools are courtesy of StackOverflow answers that are usually cited in the comments.

Most of metods rely heavily on numpy, scipy, and scikits-learn