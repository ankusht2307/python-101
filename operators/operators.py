"""
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""


# Arithmetic Operators

"""
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
"""
#  +
print(2 + 3)

# -
print(3 -2)

# *
print(2 * 3)

# / 
print( 4 / 2)

# %
print(5 % 2)

# **
print(2**3)

# //
print(5 // 2)

# Assignment Operators

"""
Operator	Example	        Same As	
    =	    x = 5	        x = 5	

    +=	    x += 3	        x = x + 3	

    -=	    x -= 3	        x = x - 3	

    *=	    x *= 3	        x = x * 3	

    /=	    x /= 3	        x = x / 3	

    %=	    x %= 3	        x = x % 3	

    //=	    x //= 3	        x = x // 3	

    **=	x   **= 3	        x = x ** 3	

    &=	    x &= 3	        x = x & 3	

    |=	    x |= 3	        x = x | 3	

    ^=	    x ^= 3	        x = x ^ 3	

    >>=	x   >>= 3	        x = x >> 3	

    <<=	x   <<= 3	        x = x << 3	

    :=	    print(x := 3)	x = 3
                            print(x)
"""

# Comparison Operators

"""
==	Equal	Ex: x == y	
!=	Not equal	Ex: x != y	
>	Greater than	Ex: x > y	
<	Less than	Ex: x < y	
>=	Greater than or equal to	Ex: x >= y	
<=	Less than or equal to	Ex: x <= y
"""

# Logical Operators
"""
and 	Returns True if both statements are true	Ex: x < 5 and  x < 10	
or	Returns True if one of the statements is true	Ex: x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	
"""

# Identity Operators
"""
is 	Returns True if both variables are the same object	Ex: x is y	
is not	Returns True if both variables are not the same object	Ex: x is not y
"""

# Membership Operators
"""
in 	Returns True if a sequence with the specified value is present in the object	Ex: x in y	
not in	Returns True if a sequence with the specified value is not present in the object	Ex: x not in y
"""

# Bitwise Operators
"""
& 	AND	Sets each bit to 1 if both bits are 1	Ex: x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	Ex: x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	Ex: x ^ y	
~	NOT	Inverts all the bits	Ex: ~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	Ex: x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""