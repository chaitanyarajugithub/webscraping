def contactsixpass(a,contactpersonsixdetails,contactpersonsixname,contactpersonsixtitle,contactpersonsixemail,contactpersonsixmobile,contactpersonsixdirectline):
    name = a.text
    print(name.strip())
    contactpersonsixdetails.append(name.strip())
    print(getdata(a, 'Name:'))
    contactpersonsixname.append(getdata(a, 'Name:').lstrip())
    print(getdata(a, 'Title:'))
    contactpersonsixtitle.append(getdata(a, 'Title:'))
    print(getdata(a, 'Email'))
    contactpersonsixemail.append(getdata(a, 'Email'))
    print(getdata(a, 'Mobile'))
    contactpersonsixmobile.append(getdata(a, 'Mobile'))
    print(getdata(a, 'Direct Line'))
    contactpersonsixdirectline.append(getdata(a, 'Direct Line'))


def contactsixnull(a,contactpersonsixdetails,contactpersonsixname,contactpersonsixtitle,contactpersonsixemail,contactpersonsixmobile,contactpersonsixdirectline):
    contactpersonsixdetails.append("null")
    contactpersonsixname.append("null")
    contactpersonsixtitle.append("null")
    contactpersonsixemail.append("null")
    contactpersonsixmobile.append("null")
    contactpersonsixdirectline.append("null")