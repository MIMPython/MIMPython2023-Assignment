import math

def giaipt_bac2(a,b,c):
    ket_qua=()
    if a == 0:
        if b == 0:
            if c == 0:
                pass
                 
        else:
            ket_qua=(-c/b)
    else:
        delta=  b**2 -4 *a *c 
        if delta > 0:
            ket_qua= ((-b - math.sqrt(delta))/2*a),(-b + math.sqrt(delta)/2*a)
        elif delta < 0:
            pass
            
        else:
            ket_qua= ( -b/(2*a)) 

    return ket_qua 

print(giaipt_bac2(1,0,-2))
