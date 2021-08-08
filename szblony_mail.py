

def senders_address():
    print('senders address: ')
    sender = input()
    return sender

def recipients_address():
    print('recipients address:')
    recipient = input()
    return recipient

def typeofmail():
    typeof = ''
    reason = ''
    thank = ''
    person = ''
    letter = ''
    print('Choose option:\n1.Thanks\n2.Love letter\n3.Invitation\n4.Help')
    typeof = str(input())[0]
    if typeof == '1':
        print('Choose a reason:\n1.for help\n2.for dinner\n3.other')
        reason = str(input())[0]
        if reason == '1':
            thank = 'for your help'
        elif reason == '2':
            thank = 'for yesterdays dinner, it was very tasty'
        elif reason == '3':
            print('your reason:')
            thank = input()
    elif typeof == '2':
        print('Choose a person:\n1.your love\n2.your friend')
        person = str(input())[0]
        if person == '1':
            letter = 'my Darling! I love you and I miss you a lot'
        elif person == '2':
            letter = 'my friend! Do You want to be my love?'
    elif typeof == '3':
        print
    return typeof, thank, person, letter


def title_email():
    typeof, thank, person, letter = typeofmail()
    title = ''
    content = ''
    if typeof == '1':
        title = 'Thank You!'
        content = 'Thank You {}, you are very nice :)'.format(thank)
    elif typeof == '2':
        title = 'From me to You'
        content = 'Hello {}'.format(letter)
    elif typeof == '3':
        title = 'I invite You'
        content = 'Hello\nI {} invite you to {}'.format(sender, recipient)
    elif typeof == '4':
        title = 'Help!'
        content = 'Help, the terrorists are here!'
    return title, content, typeof

#senders_address()
#recipients_address()
#title_email()
#print('senders address:', sender)
#print('recipients address:', recipient)
#print('title:', title)
#print('content:', content)
