
import snotparser.snotparser as sp

#ticket_number = 100000
for ticket_number in range(204000, 204581):
    parsed_data = sp.parseTicket(ticket_number)
    if parsed_data is not None:

        print ticket_number, parsed_data['status'], parsed_data['priority']


parsed_data = sp.parseTicket(100023)
print parsed_data


