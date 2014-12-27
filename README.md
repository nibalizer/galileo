Galileo: a new snot project
===========================



Goals and Scope
---------------


The goal of the galileo project is to produce an alternate web application to snot. A Web Snot 2.0 if you will. This probably needs a better name. Plz2advise.

In an effort to reach this goal, serveral discrete components will be built. See 'subprojects'.

The primary requirement of this project is that it must be 100% compatible with the currently running snot. That means the snot database (flat files in /u/snot) are authoritative. Whenever possible, operations on this dataset will be done through traditional tooling. This means that both snot and galileo can run simultaneously.



Subprojects
-----------


Four parts:


1) boogerd2: application to expose snot operations through REST
   version 2 because kennobaka wrote version 1


2) snotrocket: an application to speed up read and search operations
    uses elasticsearch for cache


3) ???: presentation layer, how make wobsite


4) pysnot: a library exposing common snot operations as python functions




Tooling
-------


Right now most things are in python. But hopefully we can nail down the interfaces between the components and some of them can be written or rewritten in other languages.


Naming
------


Nothing special is meant by the name galileo, it was unique and random. Subproject tooling names will be as hillarious as possible.
