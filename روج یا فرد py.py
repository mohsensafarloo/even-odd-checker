def zoj_fard (number): 
    if number/2==0:
        return f"zoj"
    else:
        return f"fard"

adad=10
k=zoj_fard(adad)
print(f"your number is :\n{k}")
