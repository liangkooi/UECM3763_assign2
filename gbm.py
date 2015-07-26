import pylab as p
import numpy as np

# SETUP PARAMETERS

# Values of Mu and sigma is given 
mu=0.1;  
sigma=0.26; 

S0=39; # Initial price 
n_path=1000; # Total number of simulations
n= n_partitions = 1000; # Number of partitions in the interval 

#Theoretical expectation and variance of S(3)
print(' \nTheoretical Expectation and variance of S(3) :')
t_e = S0 * p.exp(mu*3)
t_v = (S0**2)*(p.exp(2*mu*3))*(p.exp(sigma*sigma*3)-1)
print('Expectation value of S(3) = ',t_e)
print('Variance of S(3) = ',t_v)

# CREATE BROWNIAN MOTION PATHS

# Generate a row vector of 1001 evenly spaced points between time 0 and 3
t = p.linspace (0,3,n+1); # Spacing between the points is 0.003
dB = p.randn(n_path,n+1) / p.sqrt(n/3);
dB[:,0] = 0; # Set the first column of dB as zero
B=dB.cumsum(axis=1);# Sum over rows for each of the column

# Calculate stock prices
nu = mu - sigma*sigma/2;
S =p.zeros_like(B);
S[:,0] = S0 # Set the first column as the initial price = 39
S[:,1:] = S0*p.exp(nu*t[1:]+sigma*B[:,1:]);

#Plot the 5 realizations
S_plot= S[0:5] # Pick the first 5 rows
p.plot(t,S_plot.transpose()); # plot the graph
# Set the title
p.title('Geometric Brownian Motion (GBM) with $\mu$ =' + str(mu) + 'and $\sigma$ =' +str(sigma))
# Label the x axis
p.xlabel('Time,$t$');
# Label the y axis
p.ylabel('Stock prices,$USD$');
#Show the graph
p.show();

# Calculate expected value of S(3)
end_price = p.array(S[:,-1]); # price of time 3 for each row
expected_price = np.mean(end_price); # find the expected price by finding the mean
print('\nExpectation and variance based on simulation :')
print('Expected value of S(3) = ',expected_price); # print the expected value of S(3)
variance_S3 = np.var(end_price); # find the variance of the S(3)
print('Variance of S(3) = ',variance_S3);# Print the variance value

# Calculate probability of price more than 39
exceed_number = end_price > 39; # Calculate the number of S(3) that are exceed 39
count = sum (exceed_number) # Total number of S(3) that exceed 39
print('\nCalculation for probability and expectation:') #Header
print('Number of stock price that exceed 39 = ',count); # Print the result
probability= count/n_path # Calculate the probability of S(3) exceed 39
print('P[S(3)>39] = ',probability); # Print the probability result

# Calculate the expectation of E(S(3)|S(3)>39)

value_exceeded = exceed_number * end_price;
# Summation of all value that S(3) divided by total number of S(3) exceed 39
expectation_S3 = sum(value_exceeded)/count; 
print('Expectation,E(S(3)|S(3)>39) = ',expectation_S3);# Print the result








