nh, nm, ns = map(int, input().split(':'))
lh, lm, ls = map(int, input().split(':'))

first_time = (nh*3600) + (nm*60) + ns
last_time = (lh*3600) + (lm*60) + ls

if first_time < last_time:
    time = last_time - first_time
    a = time//3600
    b = time//60%60
    c = time%60
    
    print('%02d:%02d:%02d'%(a,b,c))

else:
    time = last_time - first_time + 3600*24
    a = time//3600
    b = time//60%60
    c = time%60
    
    print('%02d:%02d:%02d'%(a,b,c))
