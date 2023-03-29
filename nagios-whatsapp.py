#!/usr/bin/env python3
import argparse

from twilio.rest import Client

account_sid = 'SUA_ID_TWILIO'
auth_token = 'SEU_TOKEN_TWILIO'
client = Client(account_sid, auth_token)

to_number = 'whatsapp:NUMERO_DESTINATARIO'
from_number = 'whatsapp:SEU_NUMERO_TWILIO'

def parse_args():
    parser = argparse.ArgumentParser(description='Nagios notification via WhatsApp')
    parser.add_argument('-o', '--object_type', nargs='?', required=True)
    parser.add_argument('--notificationtype', nargs='?')
    parser.add_argument('--hoststate', nargs='?')
    parser.add_argument('--hostname', nargs='?')
    parser.add_argument('--hostaddress', nargs='?')
    parser.add_argument('--servicestate', nargs='?')
    parser.add_argument('--servicedesc', nargs='?')
    parser.add_argument('--output', nargs='?')
    args = parser.parse_args()
    return args

def host_notification(args):
    state = ''
    if args.hoststate == 'UP':
        state = u'\U00002705 '
    elif args.hoststate == 'DOWN':
        state = u'\U0001F525 '
    elif args.hoststate == 'UNREACHABLE':
        state = u'\U00002753 '

    return "%s%s (%s): %s" % (
        state,
        args.hostname,
        args.hostaddress,
        args.output,
    )


def service_notification(args):
    state = ''
    if args.servicestate == 'OK':
        state = u'\U00002705 '
    elif args.servicestate == 'WARNING':
        state = u'\U000026A0 '
    elif args.servicestate == 'CRITICAL':
        state = u'\U0001F525 '
    elif args.servicestate == 'UNKNOWN':
        state = u'\U00002753 '

    return "%s%s/%s: %s" % (
        state,
        args.hostname,
        args.servicedesc,
        args.output,
    )

def main():
    args = parse_args()
    if args.object_type == 'host':
        message = host_notification(args)
    elif args.object_type == 'service':
        message = service_notification(args)
    client.messages.create(body=message, from_=from_number, to=to_number)

if __name__ == '__main__':
    main()