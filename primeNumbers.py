def is_prime(number):
    if number <= 1:
        return "Insert number greater than 1."
    elif number in [2, 3, 5, 7]:
        return "Prime number"
    else:
      if(number%2 == 0 or number%3 == 0 or number%5 == 0 or number%7 == 0):
        return "Not a prime number"
      else:
        return "Prime number"
      
def test_is_prime():
    assert is_prime(13) == "Prime number"
    assert is_prime(2) == "Prime number"
    assert is_prime(3) == "Prime number"
    assert is_prime(1) == "Insert number greater than 1."
    assert is_prime(25) == "Not a prime number"
    assert is_prime(12) == "Not a prime number"
