import math

from docplex.cp.model import CpoModel
from docplex.cp.model import *


def CPOptimizer_model(O, S, Q, L, h, r, q, d, n, f):    

    # simplified model that uses few variables
    solver = os.path.splitext(os.path.basename(__file__))[0]    
    solver = solver.split('-', 1)[-1] if '-' in solver else solver
    model = CpoModel(name=solver)
    
    n_max = math.ceil(max(n.loc[l] for l in L))
    l_max = len(L)
    hh = [2 * h.loc[l] for l in L]
    
    i = {s: model.integer_var(0, l_max,  'i_' + str(s)) for s in S}
    x = {s: model.integer_var(1, n_max,  'x_' + str(s)) for s in S}

    for l in range(l_max):
         model.add( sum(x[s]*(i[s]==l) for s in S) <= n.loc[L[l]] )
    
    model.minimize(sum(model.element(hh,  max([i[s] for s in S if Q[s].loc[k] == 1])) for k in O) + sum (2 * r * model.ceil(model.float_div(d.loc[s], x[s]*q.loc[s])) for s in S) )

    return model, i, x
    
    