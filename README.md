# tier-list-generator

A command-line utility for generating tier lists

### How to use

Invoke `tiers.py` with the arguments you'd like to rank

```
$ ./tiers.py second first 2nd third
```

You will be asked to compare elements against each other

```
Which of these items is greater?
[1] first or [2] second or [0] equal: 1

Which of these items is greater?
[1] 2nd or [2] second or [0] equal: 0

Which of these items is greater?
[1] third or [2] 2nd or [0] equal: 2
```

`tiers.py` will compute a ranking based on your answers

```
1. first
2. second - 2nd
3. third
```
