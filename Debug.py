import datetime
class Debugger:
    """ファイルに出力します。"""
    def __init__(self,fileName):
        self.fileName = fileName
        self.buf = ""
    
    def flush(self):
        with open(self.fileName,"w",encoding="utf-8") as f:
            f.write(self.buf)
    
    def println(self,text,end="\n"):
        self.buf += "[{datetime}] {text}{end}".format(datetime=datetime.datetime.now(),text=text,end=end)