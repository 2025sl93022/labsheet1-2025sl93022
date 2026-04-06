def add(a, b):
	return a+b

def multiply(a, b):
	return a*b

def subtract(a, b):
	return a-b

def divide(a, b):
	if b==0:
		return None
	return a/b

if __name__ == "__main__":
    print("Running tests...")

    assert add(2, 3) == 5
    assert subtract(5, 3) == 2
    assert multiply(2, 3) == 6
    assert divide(6, 3) == 2

    print("All tests passed successfully!")

