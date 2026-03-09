# INTRO TO AI - 1st Lab

This repository contains Python implementations of three introductory AI topics:

- A* Search
- A-Priori Algorithm
- Differential Evolution

Each topic has two examples with printed step-by-step output to make the workflow easy to follow.

## Folder Structure

- `A Star/`
	- `a_Star_1.py`: A* graph search on a small sample graph
	- `a_Star_2.py`: A* pathfinding example for USM campus navigation

- `A-Priori/`
	- `a-priori_ex1.py`: Image tag mining
	- `a-priori_ex2.py`: Market basket analysis

- `Differential Evolution Algorithm/`
	- `diff-evol_ex1.py`: Class scheduling optimization
	- `diff-evol_ex2.py`: Factory production optimization

## Sample Scripts and Output

### A* Search

- `a_Star_1.py`
	- Description: Finds the shortest path in a small weighted graph.
	- Sample output:

```text
SHORTEST PATH FOUND:
S -> A -> C -> Z
Total Cost = 5
```

- `a_Star_2.py`
	- Description: Finds the best route from `Sinamar 2 St` to `ICT Building`.
	- Sample output:

```text
SHORTEST PATH FOUND:
Sinamar 2 St -> Sunrise -> USM Main Gate -> CBDEM -> KEPLRC -> ICT Building
Total Cost = 10
```

### A-Priori Algorithm

- `a-priori_ex1.py`
	- Description: Mines frequent tag patterns from image-tag transactions.
	- Sample output:

```text
A-PRIORI ALGORITHM - IMAGE TAG MINING
STRONG ASSOCIATION RULES (Confidence >= 70%):
Meaning in this dataset: if an image has Ocean, it also has Beach and Sunshine.
```

- `a-priori_ex2.py`
	- Description: Discovers frequent itemsets and strong rules from shopping data.
	- Sample output:

```text
A-PRIORI ALGORITHM - MARKET BASKET ANALYSIS
STRONG ASSOCIATION RULES (Confidence >= 66%):
Meaning in this dataset: if a customer buys Bread and Milk, they also bought Butter.
```

### Differential Evolution

- `diff-evol_ex1.py`
	- Description: Optimizes a class schedule toward preferred class times.
	- Sample output:

```text
FINAL OPTIMAL SCHEDULE
Math = 9.0
Science = 11.0
Programming = 2.0
Final Fitness = 0.0
Why chosen: this schedule has the lowest possible fitness (0),
meaning it exactly matches the preferred times with no deviation.
```

- `diff-evol_ex2.py`
	- Description: Selects the production plan that gives the highest profit.
	- Sample output:

```text
STEP 6 : FINAL RESULT
Total Profit = 590
The algorithm selects P3 because it produces the highest profit.
```

## Notes

- Scripts are designed for learning and demonstration.
- Most examples print intermediate steps (initial population, evaluation, mutation, selection, and final result).
- Apriori examples include short conclusion lines that explain why selected patterns/rules were kept.
- A* scripts include graph visualization windows when run in an environment with GUI support.
