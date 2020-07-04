# -*- coding: utf-8 -*-

class syntax_highlighting_py:
    def __init__(self):
         self.dict={"class":"#4682B4","def":"#4682B4","return":"#4682B4","and":"#4682B4", "True":"#4682B4","False":"#4682B4","From":"#4682B4", "import":"#4682B4","if":"#4682B4", "else":"#4682B4","for":"#4682B4","elif":"#4682B4","try":"#4682B4","except":"#4682B4","class_name":"#008B8B","text_in_quotes":"#FF8C00","name_import_class":"#C71585"}


    def set_syntax(self,text):
        for key in self.dict:
            text=text.replace(key,"<font color=\"%s\">%s</font>"%(self.dict[key],key))
        return text    

