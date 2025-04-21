# Command
mypy --config-file mypy.ini test.py > test.txt

# Output

## With error
```
builtins.int.__add__
builtins.int.__add__
Literal[3]
Literal[4]
builtins.int.__add__
builtins.int.__add__
Literal[4]
Literal[3]
builtins.int.__add__
builtins.int.__add__
Literal[3]
Literal[4]
builtins.int.__add__
builtins.int.__add__
Literal[4]
Literal[3]
test_add.py:6: error: test  [misc]
Found 1 error in 1 file (checked 1 source file)
```

Does it multiple times, switches rhs and lhs


## Without error
```
builtins.int.__add__
builtins.int.__add__
Literal[3]
Literal[4]
Success: no issues found in 1 source file
```

Expected