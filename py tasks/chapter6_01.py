text = "X-DSPAM-Confidence:    0.8475"
cut_text=None
prev_val=""
new_val=0
spc_pos=text.find(" ")
cut_text=spc_pos
for Text in text:    
    #print(Text)
    
    if(Text==" "):
        prev_val=spc_pos+1
        new_val=new_val+1
        #print(new_val)
        continue
print(float(text[cut_text+new_val:]))
