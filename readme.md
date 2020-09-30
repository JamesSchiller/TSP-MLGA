# TSP-MLGA

![graph](https://github.com/JamesSchiller/TSP-MLGA/blob/master/Untitled.png)

## Summary

```
Each gene on the chromsome is either a 0, 1, 2, or 3, which corresponds to a strategy. 

Strategies:

0 - lowest_weight
1 - random_weight
2 - first_weight
3 - highest_weight

organisms
[2, 2, 0, 1, 1, 1, 2, 1, 3, 1, 3, 3, 2]
[3, 3, 1, 0, 3, 1, 0, 3, 3, 1, 0, 1, 2]
[1, 3, 1, 3, 0, 0, 1, 1, 0, 3, 0, 0, 3]
[3, 1, 3, 2, 3, 3, 0, 0, 2, 3, 3, 2, 0]
[0, 3, 1, 3, 3, 3, 0, 1, 2, 2, 0, 2, 1]
[3, 2, 2, 3, 0, 2, 1, 3, 2, 1, 3, 1, 0]
[0, 2, 0, 3, 0, 0, 0, 2, 1, 2, 0, 3, 1]
[0, 1, 3, 3, 1, 0, 0, 0, 1, 2, 0, 2, 3]
[3, 2, 1, 0, 0, 2, 1, 3, 3, 0, 0, 1, 2]
[1, 1, 3, 1, 1, 0, 2, 1, 1, 3, 0, 3, 2]
[2, 2, 2, 2, 2, 2, 0, 1, 1, 2, 3, 1, 0]
[1, 0, 1, 2, 2, 0, 3, 0, 1, 0, 1, 3, 2]
[3, 2, 0, 0, 0, 3, 0, 3, 2, 1, 2, 3, 3]
[1, 3, 2, 3, 2, 3, 2, 3, 0, 3, 1, 2, 3]
[2, 0, 3, 1, 0, 0, 0, 0, 2, 1, 1, 1, 0]
[1, 0, 0, 0, 1, 1, 2, 2, 3, 2, 0, 1, 3]
[1, 0, 0, 2, 0, 0, 3, 3, 2, 0, 0, 3, 2]
[1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2]
[0, 0, 1, 2, 0, 1, 3, 2, 1, 2, 3, 1, 2]
[3, 0, 1, 3, 2, 1, 3, 0, 1, 0, 2, 2, 0]
.......................................
.......................................
.........................., 1, 2, 0, 0]
[0, 1, 1, 3, 0, 0, 1, 1, 0, 3, 0, 0, 1]
[3, 0, 0, 0, 2, 0, 2, 1, 1, 0, 3, 2, 0]
[3, 0, 3, 1, 3, 1, 2, 0, 1, 1, 3, 0, 0]

Each new generation replaces each old organism by a new child organism.  
Cumulative Distribution Function (CDF) is used for the selection of two parents to mate and create
a new child organism. 

A high number of nodes and a low total weight is good. 
For ex, 
say we had a chromosome with 14 nodes visited with a total weight of 40
and we had a chromosome with 14 nodes visited with a total weight of 70
since higher number of nodes visited and lower weight is better,
it is a tie for number of nodes. But the lower weight is actually better, 
so we have to make lower weights have a higher probability in our CDF. 
We convert the total weight portion to a decimal and subract it from the number of nodes visited, 
so in this way, 40 is higher than 70. 
weight of 40 would be converted to 40 / 100 = .40
score would be
14 - .40 = 13.60
weight of 70 would be converted to 70 / 100 = .70
score would be
14 - .70 = 13.30
If you had another chromsome with 13 nodes visited with a total weight of 30, 
weight of 30 would be converted to 30 / 100 = .30
13 - .30 = 12.70
By always subtracting a decimal, scores with higher nodes visited is always still higher 
cause your always subtracting from nodes visited. 
14 - x will always be higher than 13 - y. 
```

## Run Instructions
```
source venv/bin/activate
python main.py
```

## Example Output
```
best organism
-----------------
organism: [2, 2, 2, 0, 2, 0, 0, 0, 1, 1, 3, 3, 3, 1]
visited: ['a', 'b', 'd', 'c', 'h', 'j', 'i', 'f', 'e', 'g']
node_score: 10
weight_score: 29
```