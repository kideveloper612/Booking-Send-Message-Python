from twill.commands import *
go('http://mysite.org')

fv("1", "email-email", "blabla.com")
fv("1", "password-clear", "testpass")

submit('0')