boogerd2
========


Web application to expose snot operation RESTfully.
---------------------------------------------------


requires snotparser to be cloned as snotparser in this directory

github.com/prill/snotparser




API v1
======


Get text of ticket
GET /v1/ticket/<ticket number>


Get flags of ticket
GET /v1/ticket/<ticket number>/flags


Get all flags possible to flag
GET /v1/all_flags





Operations:
===========



Show Ticket
* snot -s(r) <ticket number>


Assign ticket
* snot -R <username> <ticketnumber>


List Flags
* snot -hF



Flag Ticket
* snot -F <flag> <ticketnumber>
* not really functional because snot command line cannot assign multiple flags




