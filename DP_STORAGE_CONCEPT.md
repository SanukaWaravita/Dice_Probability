# Dynamic Programming: Storage and Reuse Concept

## The Core Idea

Dynamic Programming (DP) is all about **storing results** from previous iterations so we can **reuse** them later instead of recalculating the same things over and over.

Think of it like taking notes during a math test: instead of solving "2 + 3" every time you need it, you calculate it once, write down "5", and refer back to that answer whenever needed.

---

## The Problem Without Storage (Naive Approach)

If we tried to calculate "How many ways can 10 dice sum to 32?" without storing results, we'd need to check **every possible combination**:

```
Die 1: 1, Die 2: 1, Die 3: 1, ..., Die 10: 6  → Sum = ?
Die 1: 1, Die 2: 1, Die 3: 1, ..., Die 10: 5  → Sum = ?
Die 1: 1, Die 2: 1, Die 3: 1, ..., Die 10: 4  → Sum = ?
...
```

That's **6^10 = 60,466,176** combinations to check! 😱

---

## The Solution With Storage (Dynamic Programming)

Instead, we **build up** our answer step by step, storing intermediate results:

### Step 1: Store Results for 1 Die

**Question:** With 1 die, how many ways can we get each sum?

**Calculate and Store:**
```
Sum 1: 1 way  (roll 1)      → prev_dp[1] = 1
Sum 2: 1 way  (roll 2)      → prev_dp[2] = 1
Sum 3: 1 way  (roll 3)      → prev_dp[3] = 1
Sum 4: 1 way  (roll 4)      → prev_dp[4] = 1
Sum 5: 1 way  (roll 5)      → prev_dp[5] = 1
Sum 6: 1 way  (roll 6)      → prev_dp[6] = 1
```

**Storage:**
```
prev_dp = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, ...]
```

💡 **We just solved "1 die" for ALL possible sums!**

---

### Step 2: Reuse Stored Results for 2 Dice

**Question:** With 2 dice, how many ways can we get sum 7?

**Instead of listing all combinations, we REUSE our stored answers:**

```
To get sum 7 with 2 dice:
  - Roll a 1, then need 6 from remaining dice → prev_dp[6] = 1 way
  - Roll a 2, then need 5 from remaining dice → prev_dp[5] = 1 way
  - Roll a 3, then need 4 from remaining dice → prev_dp[4] = 1 way
  - Roll a 4, then need 3 from remaining dice → prev_dp[3] = 1 way
  - Roll a 5, then need 2 from remaining dice → prev_dp[2] = 1 way
  - Roll a 6, then need 1 from remaining dice → prev_dp[1] = 1 way

Total ways = 1 + 1 + 1 + 1 + 1 + 1 = 6 ways
```

**The Magic:** We didn't recalculate "ways to get 6 with 1 die" - we **looked it up** in `prev_dp[6]`!

**Store this result:**
```
current_dp[7] = 6
```

---

### Step 3: Continue Building Up

For 3 dice, sum 10:
```
To get sum 10 with 3 dice:
  - Roll a 1, need 9 from 2 dice → current_dp[9] from step 2
  - Roll a 2, need 8 from 2 dice → current_dp[8] from step 2
  - Roll a 3, need 7 from 2 dice → current_dp[7] from step 2 = 6
  - Roll a 4, need 6 from 2 dice → current_dp[6] from step 2
  - Roll a 5, need 5 from 2 dice → current_dp[5] from step 2
  - Roll a 6, need 4 from 2 dice → current_dp[4] from step 2
```

Again, we **reuse** the answers we stored in step 2!

---

## The Storage Pattern in Our Code

```python
prev_dp = [0] * (max_sum + 1)  # Storage for "previous number of dice"
prev_dp[0] = 1

for die_num in range(1, num_dice + 1):
    current_dp = [0] * (max_sum + 1)  # Storage for "current number of dice"
    
    for total in range(die_num, max_sum + 1):
        for face in range(1, 7):
            # REUSE stored result from previous iteration!
            current_dp[total] += prev_dp[total - face]
    
    prev_dp = current_dp  # STORE current results for next iteration
```

### What Gets Stored and Reused

| Iteration | What We Store | What We Reuse (from previous iteration) |
|-----------|---------------|----------------------------------------|
| Die 1 | Ways to get each sum with 1 die | Ways with 0 dice (just the initial state) |
| Die 2 | Ways to get each sum with 2 dice | Ways with 1 die (from Die 1 iteration) |
| Die 3 | Ways to get each sum with 3 dice | Ways with 2 dice (from Die 2 iteration) |
| ... | ... | ... |
| Die 10 | Ways to get each sum with 10 dice | Ways with 9 dice (from Die 9 iteration) |

---

## Why This Avoids Repetition

### Without Storage (Repetitive):
```
Calculate: 3 dice, sum 10
  ├─ Need: 2 dice, sum 9
  │   ├─ Need: 1 die, sum 8 ❌ (impossible, but we'd still check)
  │   └─ Need: 1 die, sum 7 ❌
  ├─ Need: 2 dice, sum 8
  │   ├─ Need: 1 die, sum 7 ❌ (checked again!)
  │   └─ Need: 1 die, sum 6 ✓ (checked again!)
  └─ Need: 2 dice, sum 7
      ├─ Need: 1 die, sum 6 ✓ (checked AGAIN!)
      └─ Need: 1 die, sum 5 ✓ (checked AGAIN!)
```

We keep recalculating "1 die, sum 6" over and over!

### With Storage (Efficient):
```
Calculate ONCE and STORE:
  1 die, sum 6 = 1 way

Then REUSE that answer:
  current_dp[7] = prev_dp[6]  ← Lookup! (instant)
  current_dp[8] = prev_dp[6]  ← Lookup! (instant)
  current_dp[9] = prev_dp[6]  ← Lookup! (instant)
```

---

## The Power of Storage

### Calculations Without Storage:
- **10 dice:** Check ~60 million combinations
- **Time:** Several minutes (or crash!)

### Calculations With Storage (DP):
- **10 dice:** 10 iterations × 60 sums × 6 faces = ~3,600 operations
- **Time:** Instant! ⚡

---

## Key Takeaway

**Dynamic Programming = Smart Storage**

1. **Break problem into smaller subproblems** (1 die, 2 dice, 3 dice...)
2. **Solve each subproblem ONCE and STORE the answer** (`prev_dp`, `current_dp`)
3. **REUSE stored answers** instead of recalculating (`current_dp[total] += prev_dp[total - face]`)
4. **Build up to final answer** (each iteration uses results from previous)

The array `prev_dp` is our "notebook" where we write down answers. Instead of solving the same math problem repeatedly, we just flip back to our notes and read the answer we already calculated!

This is why it's called **Dynamic** (building up solutions) **Programming** (storing values in a table/array for reuse).
