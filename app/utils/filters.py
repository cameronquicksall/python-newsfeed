# In this preceding code, the format_date() function expects to recieve a datetime object and then uses the strftime() method to convert it to a string.
# The `%m/%d/%y`  fomat will result in 'month/date/year'
def format_date(date):
    return date.strftime('%m/%d/%y')

def format_url(url):
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

def format_plural(amount, word):
    if amount != 1:
        return word + 's'

    return word

from datetime import datetime