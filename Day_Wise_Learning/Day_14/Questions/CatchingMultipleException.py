
"""
    8️⃣ Catching multiple exceptions in one block

Write a program that catches both ValueError and TypeError in a single except block.
    """
def safe_add(a,b):
    try:
        print( a+b)

    except (TypeError,ValueError) as e:
        print(f"Error : {e}")
        

safe_add(2,"0")