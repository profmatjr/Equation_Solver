import numpy as np
import math
import matplotlib.pyplot as plt

def eqn_Solver(f,df,x0,eps):#solves x=f(x) with df=df/dx, error<eps and x0 as initial guess
	#it uses the Newton's method
	table=[]
	table.append(['Iteration','Solution','Absolute error','Relative error'])
	it=0
	while(True):
		it+=1
		x_new=x0-(f(x0)/df(x0))
		Ab_error=math.fabs(x_new-x0)
		Rel_error=math.fabs(Ab_error/x0)
		table.append([it,f'{x_new:.6f}',f'{Ab_error:.7e}',f'{Rel_error:.7e}'])
		if(Rel_error<eps):
			break
		x0=x_new
		print('\n \t \n',it,x0)
	return table	
	
if ( __name__ == '__main__' ):
		
  def g(x):#Equation to iterate in the form x=g(x)
	  return math.cos(x)
  def dgdx(x):#derivative of g(x) above
	  return -math.sin(x)
	  
  x0 = np.pi/4 #initial guess
  Tol = 1.e-6 #approximation solution accurancy
  
  data=[]
  data=eqn_Solver(g,dgdx,x0,Tol)
  
  plt.figure()
  ax = plt.gca()
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
  plt.box(on=None)
  my_table = plt.table(cellText=data[1:], colLabels=data[0], colWidths=[0.1,0.2,0.35,0.35], loc='center')
  fig = plt.gcf()
  plt.savefig('Solution-table.pdf',bbox_inches='tight',dpi=150)#saves in .pdf
  plt.savefig('Solution-table.png',bbox_inches='tight',dpi=150)#saves in .png
  
  plt.show()#shows the table
 


