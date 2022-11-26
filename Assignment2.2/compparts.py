#Read a integerinput x,y. Convert into complex number and store it in z. Display the imaginary part of z and real part of z.

import cmath

x =int(input("Enter the real part of the complex number"))
y=int(input("enter the imaginary part of the complex number"))

z=complex(x,y)
print("The real part of z is",z.real())
print("The imaginary part of z is",z.imag())
