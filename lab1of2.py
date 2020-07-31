#Quiz: Slicing Lists
#The three most recent dates are the three last years. So using negative indexing with the last element having index of -1. The third last element is -3.
 

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 

eclipse_dates = eclipse_dates[-3:]
print(eclipse_dates)

