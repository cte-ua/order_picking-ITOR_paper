#CPLEX-VG: this implements MIP CPLEX as in Velez Gallego conference paper, with one difference (one constraint is disaggregated here)

import os
from docplex.mp.model import Model

def CPLEX_model(O, S, Q, L, h, n, f):
    solver = os.path.splitext(os.path.basename(__file__))[0]
    model = Model(name=solver)

    QSDict = {k: [] for k in O}
    for k in O:
        for s in S:
            if Q[s].loc[k] == 1:
                QSDict[k].append(s)

    # variables    
    y = {(i, s, t): model.binary_var(name=f"y[{i},{s},{t}]") for i in L for s in S for t in range(1, 1 + (n.loc[i]))}
    z = {k: model.continuous_var(name=f"z[{k}]") for k in O} 

    # objective
    objective = model.sum(z[k] for k in O) + model.sum(f[t].loc[(i,s)] * y[(i, s, t)] for i in L for s in S for t in range(1,1+(n.loc[i])))
    model.minimize(objective)

    # constraints
    for s in S:
        model.add_constraint(model.sum(y[(i, s, t)] for i in L for t in range(1,1+(n.loc[i]))) == 1)
    for i in L:
        model.add_constraint(model.sum(y[(i, s, t)] * t for s in S for t in range(1,1+(n.loc[i]))) <= n.loc[i] )
    for k in O:
        for s in QSDict[k]: 
                model.add_constraint(z[k] >= model.sum(2 * h[i] * y[(i, s, t)] for i in L for t in range(1,1+(n.loc[i]))))
    return model, y 
    