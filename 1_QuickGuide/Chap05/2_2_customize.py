class VOW(object):
    def __init__(self,text):
        self.text = text
    def __enter__(self):
        self.text = "enter: " + self.text
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        self.text = "exit"

with VOW("test") as myvow:
    print(myvow.text)
    
print(myvow.text)