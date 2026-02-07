def square_root_bisection(number, tolerance=0.1, max_iterations=10):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    else:
        low = 0
        high = max(1, number)
        for i in range(max_iterations):
            mid = (low+high)/2
            if high - low <= tolerance:
                x = (low+high)/2
                print(f"The square root of {number} is approximately {x}")
                return x
            
            if mid*mid>number:
                high = mid
            else:
                low = mid 
        print(f"Failed to converge within {max_iterations} iterations")
        return None        
             

print(square_root_bisection(81, 1e-3, 50))
