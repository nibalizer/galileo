snotrocket
==========

Snotrocket is an applicaiton to speed up search and read operations on snot.

It may expose its own rest api. It may depend on boogerd to use ES internals. It may have
command line options. None of that is decided.


requirements
============


Python requirements are established in requirements.txt
Additionally an elasticsearch cluster, or single node, must be listening on localhost. Currently running/tested on ES 1.4




Truth and data duplication
==========================


A core goal of project galileo is that the traditional snot database must be the source of truth. If snotrocket uses elasticsearch as a cache, we have all the problems that come with caching. This should be solved as soon as elasticsearch functionality is stubbed out.
