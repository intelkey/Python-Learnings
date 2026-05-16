'''32. Password List Analyzer (A2 – list + validation)
    Weak passwords detecter.'''

passwords = [
    "123456",      
    "passwords",    
    "rahul123",    
    "Qwerty",      
    "hello",       
    "Mango!45Tree",  
    "Xy!9pQ#7zL",    
    "Sun$et2026",    
    "R@inB0w!Cloud"  
]

for pwd in passwords:
    # length check
    if len(pwd) < 8:
        print(pwd, "→ Weak (short)")
    else:
        # direct check without flags
        if any(ch.isupper() for ch in pwd) and \
           any(ch.islower() for ch in pwd) and \
           any(ch.isdigit() for ch in pwd) and \
           any(not ch.isalnum() for ch in pwd):
            print(pwd, "→ Strong")
        else:
            print(pwd, "→ Weak")
