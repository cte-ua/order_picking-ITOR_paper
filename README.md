# order_picking-ITOR_paper
Supplementary material for paper: "A constraint-programming approach for the storage space allocation problem in a distribution center" 


Instances folder: contains .xlsx files with data for all the instances (one instance per sheet). The files are:

   - Bins.xlsx: provides bins per location data b_l
   - Cap.xlsx: provides values of q_s (how many products s fit in one bin)
   - Locs.xlsx: provides values of h_l (distance to each location l)
   - Orders.xlsx: provides the list of orders generated

Code folder: contains .py files for all the models used in the experimental evaluation of the paper. Each file contains a single function with the form 
    def Optimizer_model(S, Q, L, h, r, q, d, n ...)
      ...
    return model 
the function produces the a model handler to be passed to either CPLEX or CP Optimizer (using model.solve())
The name of the file corresponds to the name of the model in the paper.

   -SCP.py
   -HYB.py
   ...

Experiment results folder: contains the results of all runs. For each run, the information is provided using the following structure:
    exp_main.txt
   - Instance ID: 
   - Solver: 
   - Solve status: 
   - Objective: 
   - Gap: 
   - BestBound: 
   - NumOfNodes: 
   - SolveTime: 
   - TimeBestSol: 
   - TimeInstance: 
   - TimeSolve: 
   - TimeTotal: 
   - End:
     
   exp_stats.txt
   - Instance ID:
   - NumOfVariables:
   - NumOfConstraints: 




 

 
