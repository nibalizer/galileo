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


def get_ticket_raw(ticket_number):
    subproc = subprocess.Popen(['testsnot', '-sr', str(ticket_number)], stdout=subprocess.PIPE)
    tic = subproc.communicate()


def get_history(ticket_number):
    validate_existence(ticket_number)
    hist = sp.getTicketHistory(ticket_number, 'testsnot')
    #TODO: push this chomping into snotparser
    #TODO: fix the snotparser implementation, it sux
    #TODO: use caching
    history = [i.strip() for i in hist]
    return history


def get_reply_to(ticket_number):
    subproc = subprocess.Popen(['testsnot', '-m', str(ticket_number)], stdout=subprocess.PIPE)
    reply_to_string, err  = subproc.communicate()
    return reply_to_string.split()[1]


def get_flags(ticket_number):
    validate_existence(ticket_number)
    parsed_data = sp.parseTicket(ticket_number, 'testsnot')
    flags = parsed_data['flags']
    return flags

def get_subject(ticket_number):
    validate_existence(ticket_number)
    parsed_data = sp.parseTicket(ticket_number, 'testsnot')
    subject = parsed_data['subject']
    return subject

def get_reply_subject(ticket_number):
    """
    Append Re: to subjet if it doesn't already exist
    """
    subject = get_subject(ticket_number)
    if subject.startswith("Re:"):
        pass
    else:
        subject = "Re: " + subject
    return subject


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


def fire_email(msg, from_email):
    """
    Fire an email with smtplib
    """
    s = smtplib.SMTP('localhost')
    s.sendmail(from_email, [msg['To']], msg.as_string())
    s.quit()


def resolve_ticket(number, from_email, config, message=None):

    """
    Send an email to resolve a ticket
    Stolen from underscore by Prill
    """
    # to = config['snot']['snotEmail']
    to = 'testtrouble@cat.pdx.edu'

    msg = MIMEText(message)
    msg['Subject'] = "Completing ticket #%d" % number
    msg['From']    = from_email
    msg['To']      = to
    msg.add_header("X-TTS", "%d COMP" % number)

    fire_email(msg, from_email)

    return True


def update_ticket(ticket_number,
        to,
        from_email='testtrouble@cat.pdx.edu',
        subject=None,
        message=None):

    #TODO this function is getting too big, break it up
    """
    Send an email to update a ticket
    """

    # If a subject is not passed in, set it to respond
    # to the old subject
    # If the old subject already starts with Re:, don't
    # add a Re:
    if subject is None:
        subject = get_reply_subject(ticket_number)

    # TODO paramaterize testtrouble for eventual migration
    # to real snot
    cc = 'testtrouble@cat.pdx.edu'

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From']    = from_email
    msg['To']      = cc + ',' + to
    # This is actually not a bug. It's the only way I could get it
    # to work. If someone can figure out a better way, please let
    # me know.
    msg['In-Reply-To'] = "In-Reply-To " + get_reply_to(ticket_number)

    fire_email(msg, from_email)

    # Email... doesn't really have success. So we can return True
    # here and shucks man, idunno.
    return True


if __name__ == "__main__":
    #print update_ticket(267, 'nibz@cat.pdx.edu,cmurphy@cat.pdx.edu', from_email='blkperl@cat.pdx.edu', message='test lasers')
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
    #print resolve_ticket(266, 'blkperl@cat.pdx.edu', None)
    print get_history(137)




