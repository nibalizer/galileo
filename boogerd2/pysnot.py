# Snot Helper utilities

import datetime
from email.mime.text import MIMEText
import getent
import subprocess
import smtplib

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


def get_metadata(ticket_number):
    validate_existence(ticket_number)
    parsed_data = sp.parseTicket(ticket_number, 'testsnot')
    return parsed_data


def list_all_flags():
    subproc = subprocess.Popen(['testsnot', '-hF'], stdout=subprocess.PIPE)
    flags = subproc.communicate()[0].split()[:-6]

    return flags


def unassign_ticket(ticket_number):
    validate_existence(ticket_number)
    subproc = subprocess.Popen(['testsnot', '-R', 'nobody', str(ticket_number)], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    response = subproc.communicate('y\n')
    if get_assigned(ticket_number) is None:
        return True
    else:
        return False


def assign_ticket_with_validation(ticket_number, user):
    validate_existence(ticket_number)
    if user not in dict(getent.group('acat'))['members']:
        return False

    if get_assigned(ticket_number) == user:
        return True

    if assign_ticket(ticket_number, user):
        if get_assigned(ticket_number) == user:
            return True
        else:
            return False
    else:
        return False

def assign_ticket(ticket_number, user):

    subproc = subprocess.Popen(['testsnot', '-R', str(user), str(ticket_number)], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    response = subproc.communicate('y\n')

    if subproc.returncode == 0:
        return True
    else:
        return False


def resolve_ticket_silent(ticket_number):

    subproc = subprocess.Popen(['testsnot', '-c', str(ticket_number)], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    response = subproc.communicate('y\n')

    if subproc.returncode == 0:
        return True
    else:
        return False


def resolve_ticket(number, from_email, config, message=None):

    """
    Send an email to resolve a ticket"
    Stolen from underscore by Prill
    """
    # to = config['snot']['snotEmail']
    to = 'testtrouble@cat.pdx.edu'

    msg = MIMEText(message)
    msg['Subject'] = "Completing ticket #%d" % number
    msg['From']    = from_email
    msg['To']      = to
    msg.add_header("X-TTS", "%d COMP" % number)

    s = smtplib.SMTP('localhost')
    s.sendmail(from_email, [msg['To']], msg.as_string())
    s.quit()

    return True


if __name__ == "__main__":
    #print stat_ticket(252)
    #print get_assigned(11440)
    #print datetime.datetime.now()
    #print assign_ticket_with_validation('257', 'nibz')
    #print datetime.datetime.now()
    #print assign_ticket('257', 'nibz')
    #print datetime.datetime.now()
    #print resolve_ticket(262)
    #print list_all_flags()
    #print get_metadata(255)
    print resolve_ticket(266, 'blkperl@cat.pdx.edu', None)




