# Weight plates calculator

This small script calculates all the possible weight combinations given a set of plates

## Usage

Run the script using

```python
python main.py plate1 plate2 ... plateN
```

there is also a help menu

```python
python main.py -h
```

Example:
```python
python main.py 2.5 1 3
```

Output:
```shell
Plates provided: [3.0, 2.5, 1.0]

All possible weights
  1.0: (1.0,)
  2.5: (2.5,)
  3.0: (3.0,)
  3.5: (2.5, 1.0)
  4.0: (3.0, 1.0)
  5.5: (3.0, 2.5)
  6.5: (3.0, 2.5, 1.0)
```