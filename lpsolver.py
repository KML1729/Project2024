from ortools.linear_solver import pywraplp
def main():
    
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    # Variables
    x1=solver.NumVar(0,solver.infinity(),'x1')
    x2=solver.NumVar(0,solver.infinity(),'x2')
    x3=solver.NumVar(0,solver.infinity(),'x3')
    x4=solver.NumVar(0,solver.infinity(),'x4')
    x5=solver.NumVar(0,solver.infinity(),'x5')
    total=1000000
    #Maximum investment Constraint 
    solver.Add(x1+x2+x3+x4+x5<=total)
    #Risk constraint
    solver.Add(1.08*x1+1.89*x2-1.12*x3-8.94*x4+2*x5>=0)
    #positivity of decision variables
    solver.Add(x1>=0)
    solver.Add(x2>=0)
    solver.Add(x3>=0)
    solver.Add(x4>=0)
    solver.Add(x5>=0)
    #Not more than 200,000 investment in any area
    solver.Add(x1<=0.2*total)
    solver.Add(x2<=0.2*total)
    solver.Add(x3<=0.2*total)
    solver.Add(x4<=0.2*total)
    solver.Add(x5<=0.2*total)
    #Not more than 25% investment in Stocks
    solver.Add(x1+x2<=0.25*(x1+x2+x3+x4+x5))
    #Atleast 15% investment in stockB
    solver.Add(x2>=0.15*(x1+x2+x3+x4+x5))
    #Objective function
    objective=solver.Objective()
    obj_coefficients= {x1: 6.75/100, x2: 0.42/100, x3: 0.42/100, x4: 1.54/100,x5: 7.03/100}
    for var,coeff in obj_coefficients.items():
        objective.SetCoefficient(var,coeff)

    objective.SetMaximization()    
    status=solver.Solve()
    if status==pywraplp.Solver.OPTIMAL:
        print("Solution")
        print(f"Total investment: {x1.solution_value()+x2.solution_value()+x3.solution_value()+x4.solution_value()+x5.solution_value()}")
        print(f"Objective:{objective.Value()}")
        print(f"x1: {x1.solution_value()}")
        print(f"x2: {x2.solution_value()}")
        print(f"x3: {x3.solution_value()}")
        print(f"x4: {x4.solution_value()}")
        print(f"x5: {x5.solution_value()}")
    else:
        print("No optimal value found")

if __name__=='__main__':
    main()
