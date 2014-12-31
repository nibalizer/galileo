boogerd2
========


Web application to expose snot operation RESTfully.
---------------------------------------------------


requires snotparser to be cloned as snotparser in this directory

github.com/prill/snotparser




Quickstart
==========



% curl -XPOST -d '{ "message": "Hello\n I am groot", "user": "nibz@cat.pdx.edu" }' http://localhost:5000/v1/ticket/269/update



API v1
======


Get text of ticket
GET /v1/ticket/<ticket number>


Get "raw" text of ticket, with headers and admin info
GET /v1/ticket/<ticket number>/raw


Get flags of ticket
GET /v1/ticket/<ticket number>/flags


Get the message id to reply to ticket with (In-Reply-To)
GET /v1/ticket/<ticket number>/reply_to


Get subject of ticket
GET /v1/ticket/<ticket number>/subject


Get the person who is assigned to the ticket
GET /v1/ticket/<ticket number>/assigned


Get a json blob of all available metadata
GET /v1/ticket/<ticket number>/metadata


Get all flags possible to flag
GET /v1/all_flags


Resolve a ticket silently
POST /v1/ticket/<ticket number>/resolve_silent





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





Testing
-------


You can run the limited tests by using ./boogerdtest.sh in the project dir.

