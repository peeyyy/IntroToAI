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

<img width="768" height="1095" alt="A-Priori Example 1" src="https://github.com/user-attachments/assets/8ec2c108-61f9-4962-9f68-9a3f035e742c" />

- `a-priori_ex2.py`
	- Description: Discovers frequent itemsets and strong rules from shopping data.
	- Sample output:

<img width="731" height="1167" alt="A-Priori Example 2" src="https://github.com/user-attachments/assets/ce743c18-e202-43e7-82fd-9f8c857890e8" />

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
