## Merge Sort
----------------
1. Merge sorting steps of [16,21,11,8,12,22]
    - [16,21,11] - [8,12,22]
    - [16,21] - [11] - [8,12] - [22]
    - [16] - [21] - [11] - [8] - [12] - [22]
    - [16,21] - [8] - [11] - [12,22]
    - [8,16,21] - [11,12,22]
    - [8,11,12,16,21,22]
----------
2. Big-O Notation
    n + n/2 + ... = n(1 + 1/2 + ...) = nlogn → O(nlogn)
