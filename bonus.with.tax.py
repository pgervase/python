#!/usr/bin/python
# this will prompt a user for a bonus target amount and a tax rate
# the idea is to figure out what the actual bonus would need to be 
# for the end person to get that precise amount given the tax rate
#
# For example, if I want to have the bonus be $100 and the tax rate
# is 25%, I would have to give more than just $125 since 25% of $125
# is 31.25. This means that I'd end up with only $93.75.
# If I doubled the amount, 25% or $200 is $50, leaving me with
# $150, which is more than the target. This tells me that the target
# is somewhere between $125(lower_bound) and $200(upper_bound)... but where?
# I can split the difference, $162.50, set that to current_guess, and 
# see if that is too high or too low. 

import sys

bonus = float(input('What is the bonus target? '))
taxrate = float(input('What is the tax rate in %, 25, 40, ... ? '))
#bonus = 100
#taxrate = 30

taxrate = taxrate / 100
#####
# Here i'll declare my upper estimate, lower estimate, and the current guess. 
# These will be used when I am trying to hone in on my answer
upper_bound = 0
lower_bound = 0
current_guess = 0
tax_on_current_guess = 0
final_after_tax = 0

######
# if the taxrate >= 50, then revolt!
if (taxrate < .5):
  pass
elif (taxrate == .5):
  finalanswer = (bonus * 2)
  print("to achieve your target bonux of %s with your tax rate of %s, you'd need the initial pay to be %s" % (bonus,taxrate,finalanswer))
  sys.exit(0)
elif (taxrate > .5):
  print("tax rate too high! revolt!")
  print("but seriously, why I'm not going to bother trying to figure out the tax rate / bonus for over 50%:")
  print("if the tax rate is 80%, you'd need 5x your bonus target.")
  print("if the tax rate is 90%, you'd need 10x.")
  print("if the tax rate were 95%, you'd need 20x.")
  print("if the tax rate were 97%, you'd need ~ 33.333....x")
  print("as the tax rate approaches 100%, the base needed reaches to infinity.")
  print("at some point, buffer overflow trying to come up with enough money to pay a super high tax")
  sys.exit(0)
else:
  print("tax rate too high! revolt!")
  sys.exit(0)
  
#####
# I can start by setting the lower_bound to (bonus + (bonus*taxrate)). This will be somewhat close to the answer, but always too low.
# The upper bonus at 2bonus will always be too high.
# If I'm this far, I know the tax rate is < 50%
lower_bound = (bonus + (bonus*taxrate))
upper_bound = (bonus * 2)
current_guess = lower_bound

#####
# the majority of the code will simply be looping
maxloops = 30   # for the final version, 30 loops will get extremely close with 20 probably roundable to the nearest cent.
i = 0
print("before going into the loop, current_guess is simply the lower_bound, %s" % (current_guess))
while(i < maxloops):
  tax_on_current_guess=(taxrate*current_guess)
  final_after_tax=current_guess-tax_on_current_guess
  print("------")
  #print("current_guess is %s, lower_bound is %s, and upper_bound is %s" % (current_guess,lower_bound,upper_bound))
  print("current_guess is %.2f, lower_bound is %.2f, and upper_bound is %.2f" % (current_guess,lower_bound,upper_bound))
  #print("tax on current guess is %s and so the final after tax for the current guess is %s" % (tax_on_current_guess,final_after_tax))
  print("tax on current guess is %.2f and so the final after tax for the current guess is %.2f" % (tax_on_current_guess,final_after_tax))
# I now know if my current guess is too high or too low. I'll adjust my current guess and either the lower or upper bounds
  if(final_after_tax<bonus):
#    print("current_guess is too low: %s and upper_bound is %s" % (current_guess, upper_bound))
    lower_bound=current_guess
    current_guess=(lower_bound+upper_bound)/2
#    print("current_guess updated to: %s and upper_bound is %s" % (current_guess, upper_bound))
  else:
#    print("current_guess is too high: %s and lower_bound is %s" % (current_guess, lower_bound))
    upper_bound=current_guess
    current_guess=(current_guess+lower_bound)/2
#    print("current_guess updated to %s and lower_bound is %s" % (current_guess, lower_bound))

  i = i + 1
  if(abs(final_after_tax-bonus)<0.009):
    #print("to receive in hand the amount of %s after a tax of %s%%, the correct initial amount is %s" % (bonus, (taxrate*100), current_guess))
    print("-----\n-----\nto receive in hand the amount of $%s after a tax of %s%%, the correct initial amount is $%.2f" % (bonus, (taxrate*100), current_guess))
    percentlarger = round(((current_guess-bonus)/bonus)*100, 2)
    #print("that is %s%% more than the target amount or $%s and an increase of %s%% over the initial tax rate of %s%%" % (percentlarger, bonus, str(percentlarger-taxrate), str(taxrate*100)))
    print("that is %s%% more than the target amount or $%s and an increase of %.2f%% over the initial tax rate of %s%%" % (percentlarger, bonus, (percentlarger-taxrate), str(taxrate*100)))
    sys.exit(0)
