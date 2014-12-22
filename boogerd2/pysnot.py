# Snot Helper utilities
import subprocess
import snotparser.snotparser as sp


def get_ticket(ticket_number):
    subproc = subprocess.Popen(['testsnot', '-s', str(ticket_number)], stdout=subprocess.PIPE)
    tic = subproc.communicate()
    return tic


def get_flags(ticket_number):
    parsed_data = sp.parseTicket(ticket_number, 'testsnot')
    flags = parsed_data['flags']
    return flags


