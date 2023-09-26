def initial_velocity():
 import math
 system = input("Use meters or feet? ")
 system = system.lower()
 if system == ("meters"):
   G = int(9.81)
   X = int(input("How far did the object fly (in meters)? "))
   GX = G * X
   O = int(input("What was the launch angle (in degrees)? "))
   R = O * 0.0175
   sin = math.sin(2 * R)
   square = GX / sin
   velocity = str(round(square ** (1/2), 3))
   distance = str(X)
   O = str(O)
   return ("The object had an initial velocity of " + velocity + " meters per second when launched " + distance + " meters at a launch angle of " + O + " degrees.")
 elif system == ("feet"):
  G = int(32)
  X = int(input("How far did the object fly (in feet)? "))
  GX = G * X
  O = int(input("What was the launch angle (in degrees)? "))
  R = O * 0.0175
  sin = math.sin(2 * R)
  square = GX / sin
  velocity = str(round(square ** (1/2), 3))
  distance = str(X)
  O = str(O)
  return ("The object had an initial velocity of " + velocity + " feet per second when launched " + distance + " feet at a launch angle of " + O + " degrees.")
 else:
  print ("You must have a typo, try again.")
  return (initial_velocity())
print (initial_velocity())