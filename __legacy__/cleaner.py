def clean(text):
    import re
    #text=text.strip()
    return (re.sub('\[.*?\]', '', text)).strip()
   # return text