import math as m
x = float(input("Enter the number "))
print("modf = ",m.modf(x))  # modf(x) Returns the fractional and integer parts of x
print("trunc = ",m.trunc(x)) # trunc(x)Returns the truncated integer value of x
print("exp = ",m.exp(x)) # exp(x) Returns e**x
print("expm1 = ",m.expm1(x)) # expm1(x) Returns e**x - 1
print("log = ",m.log(x)) # log(x[, base]) Returns the logarithm of x to the base (defaults to e)
print("log1p = ",m.log1p(x)) # log1p(x) Returns the natural logarithm of 1+x
print("log2 = ",m.log2(x)) # log2(x) Returns the base-2 logarithm of x
print("log10 = ",m.log10(x)) # log10(x) Returns the base-10 logarithm of x
print("pow() = ", m.pow(x,2)) # pow(x, y) Returns x raised to the power y
print("sqrt = ",m.sqrt(x)) # sqrt(x) Returns the square root of x
