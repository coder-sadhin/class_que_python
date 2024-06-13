class Magic():
    def replace(self,s,o,n):
        return s.replace(o,n)

    def str_length(self,s):
        return len(s)
    
    def trim(self,s):
        return s.strip(s)
    
magic= Magic()

s= magic.replace("AzErty", "E","e")
print(s)
s= magic.str_length("AzErty")
print(s)
s=magic.trim("  AzErty   ")
print(s)