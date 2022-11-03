def createEmail(forename, surname, provider, country):
    # Convert all to lower case
    forename = forename.lower()
    surname = surname.lower()

    # Get email country extension
    if country == 'UK':
        email_provider = 'co.uk'
    elif country == 'USA':
        email_provider = 'com'
    else:
        email_provider = 'eu'

    # Get email provider details
    if provider == 'Google':
        account = 'gmail'
    else:
        account = 'hotmail'

    # Get first char of forename
    start_email = forename[0]

    # Create email address
    email_address = start_email + '.' + surname + '@' + account + '.' + email_provider
    print(email_address)


createEmail('Jonathan', 'Smith', 'Google', 'UK')
createEmail('Gemma', 'Prest', 'Hotmail', 'Berlin')
createEmail('Zoe', 'Fryer', 'Google', 'USA')
