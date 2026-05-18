import datetime

def logni(meno, text):
    cas = datetime.datetime.now()
    
    with open("log.txt", "a") as f:
        f.write(f"{cas} - user:{meno} - {text}\n")