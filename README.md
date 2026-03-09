# INTRO TO AI - 1st Lab

This repository contains Python implementations of three introductory AI topics:

- A* Search
- A-Priori Algorithm
- Differential Evolution (1 evolution inspired algorithm)

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

<img width="1788" height="1294" alt="aStar_Example1" src="https://github.com/user-attachments/assets/561e01d8-5e5a-4208-8136-9a39781946e3" />

- `a_Star_2.py`
	- Description: Finds the best route from `Sinamar 2 St` to `ICT Building`.
	- Sample output:

<img width="2136" height="1370" alt="aStar_Example2" src="https://github.com/user-attachments/assets/fc054254-b8f7-404a-8ef8-3b67154ce880" />

### A-Priori Algorithm

- `a-priori_ex1.py`
	- Description: Mines frequent tag patterns from image-tag transactions.
	- Sample output:

<img width="912" height="1160" alt="A-Priori Example 1A" src="https://github.com/user-attachments/assets/494a78a1-ff5a-4c2c-9696-5c3bd6eef3a2" />
<img width="856" height="591" alt="A-Priori Example 1B" src="https://github.com/user-attachments/assets/5751f7cc-04bd-4c80-a666-20e1962140c1" />

- `a-priori_ex2.py`
	- Description: Discovers frequent itemsets and strong rules from shopping data.
	- Sample output:

<img width="831" height="1165" alt="A-Priori Example 2A" src="https://github.com/user-attachments/assets/38b66656-93f8-42b5-8164-93b7010f17eb" />
<img width="980" height="763" alt="A-Priori Example 2B" src="https://github.com/user-attachments/assets/5be46a2a-2ce4-41e7-a7bd-c031bb01b7c4" />

### Differential Evolution

- `diff-evol_ex1.py`
	- Description: Optimizes a class schedule toward preferred class times.
	- Sample output:

<img width="455" height="1109" alt="Differential Evolution Example 1" src="https://github.com/user-attachments/assets/9e3b49a5-4b81-4e87-be6d-920a7c29f7e1" />

- `diff-evol_ex2.py`
	- Description: Selects the production plan that gives the highest profit.
	- Sample output:

<img width="700" height="1096" alt="Differential Evolution Example 2" src="https://github.com/user-attachments/assets/e715d86d-4e0a-48a6-8771-ddeeaef9cce2" />

## Notes
- A* scripts include graph visualization windows when run in an environment with GUI support.
- A-Priori examples include short conclusion lines that explain why selected patterns/rules were kept.
- Most examples in differential evolution print intermediate steps (initial population, evaluation, mutation, selection, and final result).
