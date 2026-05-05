# walrus operator
# := introudcued in python3.8 allows you to assign values to variables as part of an expression. officially called assignment expression
if(n := len([1,2,3,4,5])) > 3:
  print(f"List is too long ({n} elements, expected <= 3)")

  # types definition
  from typing import List, Tuple, Dict, Union
  n: int = 5
  name: str = 'Shikha'

  def sum (a: int, b: int) -> int:
    print(a + b)
  
  sum(3,4)

  numbers: List = [1,2,3,4,5]

  person: Tuple[str, int] = ('Alice', 23)

  scores:Dict[str,int] = {"Alice":90,"Mradul":100}

  identifier: Union[int, str] = "ID123"