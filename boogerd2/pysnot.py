# Snot Helper utilities

import getent
import subprocess

import snotparser.snotparser as sp


class TicketNotFoundException(Exception):
    pass


def validate_existence(ticket_number):
    """
    Function to wrap stat_ticket to validate
    if a ticket exists
    """
    if not stat_ticket(ticket_number):
        raise TicketNotFoundException(
            "Ticket {0} not found".format(ticket_number))


def stat_ticket(ticket_number):
    """
    Test for existence of a ticket
    The basis for validate_existence
    """
    subproc = subprocess.Popen(['testsnot', '-l', str(ticket_number)], stdout=subprocess.PIPE)
    response, err  = subproc.communicate()
    if response == "":
        return False
    else:
        return True


def get_ticket(ticket_number):
    subproc = subprocess.Popen(['testsnot', '-s', str(ticket_number)], stdout=subprocess.PIPE)
    tic = subproc.communicate()
    return tic


def get_flags(ticket_number):
    validate_existence(ticket_number)
    parsed_data = sp.parseTicket(ticket_number, 'testsnot')
    flags = parsed_data['flags']
    return flags


def get_assigned(ticket_number):
    validate_existence(ticket_number)
    parsed_data = sp.parseTicket(ticket_number, 'testsnot')
    try:
        owner = parsed_data['assigned_to']
    except KeyError:
        return None
    return owner


def list_all_flags():
    subproc = subprocess.Popen(['testsnot', '-hF'], stdout=subprocess.PIPE)
    flags = subproc.communicate()[0].split()[:-6]

    return flags


def assign_ticket(ticket_number, user):
    if user not in dict(getent.group('acat'))['members']:
        if user != 'nobody':
            return False

    if stat_ticket(ticket_number) != True:
        return False

    if get_assigned(ticket_number) == user:
        return True

    subproc = subprocess.Popen(['testsnot', '-R', str(user), str(ticket_number)], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    response = subproc.communicate('y\n')

    if get_assigned(ticket_number) in [user, None]:
        return True
    else:
        return False


if __name__ == "__main__":
    #print stat_ticket(252)
    #print get_assigned(11440)
    print assign_ticket('256', 'nobody')
    #print list_all_flags()




