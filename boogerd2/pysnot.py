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


def list_all_flags():
    subproc = subprocess.Popen(['testsnot', '-hF'], stdout=subprocess.PIPE)
    flags = subproc.communicate()[0].split()[:-6]

    return flags


if __name__ == "__main__":
    print list_all_flags()
