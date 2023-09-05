# uppgift 3.3
import random
dice = random.randint(1, 6)

if dice == 1:
    print("""
Du slog en 1:a!
---------
|       |
|   X   |
|       |
---------
  """)
elif dice == 2:
    print("""
Du slog en 2:a!        
---------
|      X|
|       |
| X     |
---------
""")
        
elif dice == 3:
    print("""
Du slog en 3:a!        
---------
|      X|
|    X  |
| X     |
---------
""")
elif dice == 4:
    print("""
Du slog en 4:a!        
---------
|X     X|
|       |
|X     X|
---------
""")
elif dice == 5:
    print("""
Du slog en 5:a!        
---------
|X     X|
|   X   |
|X     X|
---------
""")
elif dice == 6:
    print("""
Du slog en 6:a!        
---------
|X     X|
|X     X|
|X     X|
---------
""")