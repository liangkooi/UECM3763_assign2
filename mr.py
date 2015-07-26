import pylab as p
import numpy as np

#Setup parameters

R0=3; alpha = 1; theta = 0.064; sigma = 0.27; t=1.0; n_path=1000;
n=n_partitions=1000; dt=t/n; 

# CREATE BROWNINAN MOTION PATHS

t = p.linspace (0,1,n+1)[:-1]
dB = p.randn(n_path,n+1)*p.sqrt(dt);
dB[:,0] = 0; # Set the first column for all row become zero
B=dB.cumsum(axis=1);

r=p.zeros_like(B); # Create a zero matrix having same size with B
r[:,0]=R0; # Set the first column of r as 3
col = 0;
for col in range (n):
    r[:,col+1]=r[:,col]+(theta-r[:,col])*dt + sigma*r[:,col]*dB[:,col+1]
    
    
pick_r=r[0:5:,:-1]  #Pick 5 realizations 
p.plot(t,pick_r.transpose()) #Plot the graph
# Label the title,y-axis and x-axis
p.title('5 realizations of the mean reversal process for 0<t<1 with $\\alpha$ = '+ str(alpha)+'\n $\\theta$ = '+str(theta)+' and $\\sigma$ ='+str(sigma))
p.xlabel('Time,$t$')
p.ylabel('R(t)')
p.show()

r_t1 = r[:,-1] # pick all your R(1)
expected_r1=np.mean(r_t1) # Find the expected value
print('The expected value of R(1),E(R(1)) =',expected_r1) # Show the result
# Count the number of value at R(1) that is exceeded 2
count = r_t1>2 
prob= sum (count)/n_path; # Calculate the probability R(1) greater than 2
print('Probability that R(1)>2, P(R(1)>2) =',prob) # Show the result


