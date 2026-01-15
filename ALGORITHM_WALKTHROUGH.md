# Dynamic Programming Algorithm - Complete Walkthrough

This document traces through **every iteration** of the dice probability algorithm with a simplified example.

## Example Configuration
- **Number of dice**: 2
- **Target sum**: 7
- **Max possible sum**: 12 (2 × 6)

---

## Initial Setup

```python
max_sum = 2 * 6 = 12
prev_dp = [0] * 13  # indices 0-12 (length 13)
prev_dp[0] = 1      # One way to get sum 0 with zero dice
```

**Initial State:**
```
prev_dp = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
           ^
         idx 0
```

---

## Iteration: die_num = 1 (First Die)

**Outer Loop:** `die_num = 1`

**Initialize:**
```python
current_dp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

### Inner Loops (total from 1 to 12):

#### total = 1
- **face = 1**: `total - face = 0` → `current_dp[1] += prev_dp[0]` → `current_dp[1] = 0 + 1 = 1`
- **face = 2**: `total - face = -1` → skip (negative)
- **face = 3**: skip
- **face = 4**: skip
- **face = 5**: skip
- **face = 6**: skip

**After total=1:** `current_dp = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`

#### total = 2
- **face = 1**: `total - face = 1` → `current_dp[2] += prev_dp[1]` → `current_dp[2] = 0 + 0 = 0`
- **face = 2**: `total - face = 0` → `current_dp[2] += prev_dp[0]` → `current_dp[2] = 0 + 1 = 1`
- **face = 3**: skip
- **face = 4**: skip
- **face = 5**: skip
- **face = 6**: skip

**After total=2:** `current_dp = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`

#### total = 3
- **face = 1**: `total - face = 2` → `current_dp[3] += prev_dp[2]` → `current_dp[3] = 0 + 0 = 0`
- **face = 2**: `total - face = 1` → `current_dp[3] += prev_dp[1]` → `current_dp[3] = 0 + 0 = 0`
- **face = 3**: `total - face = 0` → `current_dp[3] += prev_dp[0]` → `current_dp[3] = 0 + 1 = 1`
- **face = 4**: skip
- **face = 5**: skip
- **face = 6**: skip

**After total=3:** `current_dp = [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]`

#### total = 4
- **face = 1**: `current_dp[4] += prev_dp[3]` → `0 + 0 = 0`
- **face = 2**: `current_dp[4] += prev_dp[2]` → `0 + 0 = 0`
- **face = 3**: `current_dp[4] += prev_dp[1]` → `0 + 0 = 0`
- **face = 4**: `current_dp[4] += prev_dp[0]` → `0 + 1 = 1`
- **face = 5**: skip
- **face = 6**: skip

**After total=4:** `current_dp = [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]`

#### total = 5
- **face = 1**: `current_dp[5] += prev_dp[4]` → `0 + 0 = 0`
- **face = 2**: `current_dp[5] += prev_dp[3]` → `0 + 0 = 0`
- **face = 3**: `current_dp[5] += prev_dp[2]` → `0 + 0 = 0`
- **face = 4**: `current_dp[5] += prev_dp[1]` → `0 + 0 = 0`
- **face = 5**: `current_dp[5] += prev_dp[0]` → `0 + 1 = 1`
- **face = 6**: skip

**After total=5:** `current_dp = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]`

#### total = 6
- **face = 1**: `current_dp[6] += prev_dp[5]` → `0 + 0 = 0`
- **face = 2**: `current_dp[6] += prev_dp[4]` → `0 + 0 = 0`
- **face = 3**: `current_dp[6] += prev_dp[3]` → `0 + 0 = 0`
- **face = 4**: `current_dp[6] += prev_dp[2]` → `0 + 0 = 0`
- **face = 5**: `current_dp[6] += prev_dp[1]` → `0 + 0 = 0`
- **face = 6**: `current_dp[6] += prev_dp[0]` → `0 + 1 = 1`

**After total=6:** `current_dp = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]`

#### total = 7 through 12
All remain 0 because `prev_dp` only has a value at index 0.

**Final current_dp after die_num=1:**
```
current_dp = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
```

**Meaning:** With 1 die, there's exactly **1 way** to get each sum from 1 to 6.

**Update:**
```python
prev_dp = current_dp
```

---

## Iteration: die_num = 2 (Second Die)

**Outer Loop:** `die_num = 2`

**Initialize:**
```python
current_dp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

**Starting prev_dp:**
```
prev_dp = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
```

### Inner Loops (total from 2 to 12):

#### total = 2
- **face = 1**: `current_dp[2] += prev_dp[1]` → `0 + 1 = 1`
- **face = 2**: `current_dp[2] += prev_dp[0]` → `1 + 0 = 1`
- **face = 3**: skip
- **face = 4**: skip
- **face = 5**: skip
- **face = 6**: skip

**After total=2:** `current_dp = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`

**Meaning:** Sum 2 with 2 dice → only (1,1) → 1 way

#### total = 3
- **face = 1**: `current_dp[3] += prev_dp[2]` → `0 + 1 = 1`
- **face = 2**: `current_dp[3] += prev_dp[1]` → `1 + 1 = 2`
- **face = 3**: `current_dp[3] += prev_dp[0]` → `2 + 0 = 2`
- **face = 4**: skip
- **face = 5**: skip
- **face = 6**: skip

**After total=3:** `current_dp = [0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]`

**Meaning:** Sum 3 with 2 dice → (1,2) and (2,1) → 2 ways

#### total = 4
- **face = 1**: `current_dp[4] += prev_dp[3]` → `0 + 1 = 1`
- **face = 2**: `current_dp[4] += prev_dp[2]` → `1 + 1 = 2`
- **face = 3**: `current_dp[4] += prev_dp[1]` → `2 + 1 = 3`
- **face = 4**: `current_dp[4] += prev_dp[0]` → `3 + 0 = 3`
- **face = 5**: skip
- **face = 6**: skip

**After total=4:** `current_dp = [0, 0, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0]`

**Meaning:** Sum 4 with 2 dice → (1,3), (2,2), (3,1) → 3 ways

#### total = 5
- **face = 1**: `current_dp[5] += prev_dp[4]` → `0 + 1 = 1`
- **face = 2**: `current_dp[5] += prev_dp[3]` → `1 + 1 = 2`
- **face = 3**: `current_dp[5] += prev_dp[2]` → `2 + 1 = 3`
- **face = 4**: `current_dp[5] += prev_dp[1]` → `3 + 1 = 4`
- **face = 5**: `current_dp[5] += prev_dp[0]` → `4 + 0 = 4`
- **face = 6**: skip

**After total=5:** `current_dp = [0, 0, 1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0]`

**Meaning:** Sum 5 with 2 dice → (1,4), (2,3), (3,2), (4,1) → 4 ways

#### total = 6
- **face = 1**: `current_dp[6] += prev_dp[5]` → `0 + 1 = 1`
- **face = 2**: `current_dp[6] += prev_dp[4]` → `1 + 1 = 2`
- **face = 3**: `current_dp[6] += prev_dp[3]` → `2 + 1 = 3`
- **face = 4**: `current_dp[6] += prev_dp[2]` → `3 + 1 = 4`
- **face = 5**: `current_dp[6] += prev_dp[1]` → `4 + 1 = 5`
- **face = 6**: `current_dp[6] += prev_dp[0]` → `5 + 0 = 5`

**After total=6:** `current_dp = [0, 0, 1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0]`

**Meaning:** Sum 6 with 2 dice → (1,5), (2,4), (3,3), (4,2), (5,1) → 5 ways

#### total = 7 (OUR TARGET!)
- **face = 1**: `current_dp[7] += prev_dp[6]` → `0 + 1 = 1`
- **face = 2**: `current_dp[7] += prev_dp[5]` → `1 + 1 = 2`
- **face = 3**: `current_dp[7] += prev_dp[4]` → `2 + 1 = 3`
- **face = 4**: `current_dp[7] += prev_dp[3]` → `3 + 1 = 4`
- **face = 5**: `current_dp[7] += prev_dp[2]` → `4 + 1 = 5`
- **face = 6**: `current_dp[7] += prev_dp[1]` → `5 + 1 = 6`

**After total=7:** `current_dp = [0, 0, 1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0]`

**Meaning:** Sum 7 with 2 dice → (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) → **6 ways** ✓

#### total = 8
- **face = 1**: `current_dp[8] += prev_dp[7]` → `0 + 0 = 0`
- **face = 2**: `current_dp[8] += prev_dp[6]` → `0 + 1 = 1`
- **face = 3**: `current_dp[8] += prev_dp[5]` → `1 + 1 = 2`
- **face = 4**: `current_dp[8] += prev_dp[4]` → `2 + 1 = 3`
- **face = 5**: `current_dp[8] += prev_dp[3]` → `3 + 1 = 4`
- **face = 6**: `current_dp[8] += prev_dp[2]` → `4 + 1 = 5`

**After total=8:** `current_dp = [0, 0, 1, 2, 3, 4, 5, 6, 5, 0, 0, 0, 0]`

**Meaning:** Sum 8 with 2 dice → (2,6), (3,5), (4,4), (5,3), (6,2) → 5 ways

#### total = 9
- **face = 1**: `current_dp[9] += prev_dp[8]` → `0 + 0 = 0`
- **face = 2**: `current_dp[9] += prev_dp[7]` → `0 + 0 = 0`
- **face = 3**: `current_dp[9] += prev_dp[6]` → `0 + 1 = 1`
- **face = 4**: `current_dp[9] += prev_dp[5]` → `1 + 1 = 2`
- **face = 5**: `current_dp[9] += prev_dp[4]` → `2 + 1 = 3`
- **face = 6**: `current_dp[9] += prev_dp[3]` → `3 + 1 = 4`

**After total=9:** `current_dp = [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 0, 0, 0]`

**Meaning:** Sum 9 with 2 dice → (3,6), (4,5), (5,4), (6,3) → 4 ways

#### total = 10
- **face = 1**: `current_dp[10] += prev_dp[9]` → `0 + 0 = 0`
- **face = 2**: `current_dp[10] += prev_dp[8]` → `0 + 0 = 0`
- **face = 3**: `current_dp[10] += prev_dp[7]` → `0 + 0 = 0`
- **face = 4**: `current_dp[10] += prev_dp[6]` → `0 + 1 = 1`
- **face = 5**: `current_dp[10] += prev_dp[5]` → `1 + 1 = 2`
- **face = 6**: `current_dp[10] += prev_dp[4]` → `2 + 1 = 3`

**After total=10:** `current_dp = [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 0, 0]`

**Meaning:** Sum 10 with 2 dice → (4,6), (5,5), (6,4) → 3 ways

#### total = 11
- **face = 1**: `current_dp[11] += prev_dp[10]` → `0 + 0 = 0`
- **face = 2**: `current_dp[11] += prev_dp[9]` → `0 + 0 = 0`
- **face = 3**: `current_dp[11] += prev_dp[8]` → `0 + 0 = 0`
- **face = 4**: `current_dp[11] += prev_dp[7]` → `0 + 0 = 0`
- **face = 5**: `current_dp[11] += prev_dp[6]` → `0 + 1 = 1`
- **face = 6**: `current_dp[11] += prev_dp[5]` → `1 + 1 = 2`

**After total=11:** `current_dp = [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 0]`

**Meaning:** Sum 11 with 2 dice → (5,6), (6,5) → 2 ways

#### total = 12
- **face = 1**: `current_dp[12] += prev_dp[11]` → `0 + 0 = 0`
- **face = 2**: `current_dp[12] += prev_dp[10]` → `0 + 0 = 0`
- **face = 3**: `current_dp[12] += prev_dp[9]` → `0 + 0 = 0`
- **face = 4**: `current_dp[12] += prev_dp[8]` → `0 + 0 = 0`
- **face = 5**: `current_dp[12] += prev_dp[7]` → `0 + 0 = 0`
- **face = 6**: `current_dp[12] += prev_dp[6]` → `0 + 1 = 1`

**After total=12:** `current_dp = [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]`

**Meaning:** Sum 12 with 2 dice → (6,6) → 1 way

**Final current_dp after die_num=2:**
```
current_dp = [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
              0  1  2  3  4  5  6  7  8  9 10 11 12  (indices)
```

---

## Final Calculation

```python
ways_to_target = current_dp[7] = 6
total_outcomes = 6^2 = 36
probability = 6/36 = 0.1666666667
percentage = 16.666667%
```

## Summary

With **2 dice** targeting a sum of **7**:
- ✅ There are **6 ways** to achieve this: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)
- ✅ Total possible outcomes: **36**
- ✅ Probability: **6/36 = 1/6 ≈ 16.67%**

The algorithm correctly computed this by building up from 1 die to 2 dice, tracking all possible ways to reach each sum at each stage!
