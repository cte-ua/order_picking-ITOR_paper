import math

from docplex.cp.model import CpoModel
from docplex.cp.model import *

def CPOptimizer_model(O, S, Q, L, h, r, q, d, n, f):  
    
    solver = os.path.splitext(os.path.basename(__file__))[0]    
    model = CpoModel(name = solver)
    
    d_max = math.ceil(max(d.loc[s] for s in S))    
    n_max = math.ceil(max(n.loc[l] for l in L))
    h_max = math.ceil(max(2 * h.loc[l] for l in L))
    l_max = len(L)
    hh = [2 * h.loc[l] for l in L]
    
    z = {k: model.integer_var(0, h_max, 'z_' + str(k)) for k in O}  # (min, max, name)
    i = {s: model.integer_var(0, l_max, 'i_' + str(s)) for s in S}
    i_max = {k: model.integer_var(0, l_max, 'imax_' + str(k)) for k in O}      
    x = {(l, s): model.integer_var(0, n_max, 'x_' + str(l) + str(s)) for l in L for s in S}
    
    for k in O:        
       model.add(i_max[k] == max([i[s] for s in S if Q[s].loc[k] == 1]))       
    
    for k in O:
        model.add(z[k] == model.element(hh, i_max[k]))
   
    counter_L = 0
    for s in S:
        counter_L = 0
        for l in L:
            model.add(model.if_then(i[s] == counter_L, x[l,s] >= 1))
            model.add(model.if_then(x[l,s] >= 1, i[s] == counter_L))
            counter_L += 1            

    for l in L:
         model.add(sum(x[l,s] for s in S) <= n.loc[l])
    
    f_s = {}
    denominator = {}
    for s in S:
        f_s[s] = model.integer_var(0,d_max, 'fs_'+ str(s))        
        denominator[s] = model.integer_var(1, n_max, 'ds_'+ str(s))
        model.add(denominator[s] == sum(x[l,s] for l in L))         
        model.add(f_s[s] == model.ceil(model.float_div(d.loc[s], denominator[s]*q.loc[s]))) 
        
    
    model.minimize(sum(z[k] for k in O) + sum (2 * r * f_s[s] for s in S))

    return model
    
  
  