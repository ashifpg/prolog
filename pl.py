Checking prime number:

divisible(X,Y):-
N is Y*Y,
N =< X,
X mod Y =:= 0.

divisible(X,Y):-
Y < X,
Y1 is Y+1,
divisible(X,Y1).

isprime(X):-
Y is 2, X > 1, \+divisible(X,Y).
Run Command:isprime(----)

#factorial
fact(0,1).
fact(N,F):-
(

 N>0 ->
 (
  N1 is N-1,
  fact(N1,F1),
  F is N*F1
 )
;
write('N sould be greater than 0')
).
Run Command fact(5,R).

Another:
fact(0,1).
fact(X,Y):-
X1 is X-1,
fact(X1,Z),
Y is X*Z.

Input:  fact(3,X).

#DFS in Python
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : [],
}
visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-First Search")
dfs(visited, graph, '5')

#BFS in Python
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
visited = []
queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(visited, graph, '5')

#family relation
female(morzina).
female(maleka).
female(saleka).
female(jorina).

male(jamal).
male(kamal).
male(motin).
male(baten).

parent(morzina,kamal).
parent(motin,kamal).
parent(motin,maleka).
parent(kamal,jorina).
parent(maleka,kamal).
parent(saleka,jamal).
parent(motin,baten).
parent(baten,jamal).

%rules
mother(X,Y):-
parent(X,Y),
female(X).

father(X,Y):-
parent(X,Y),
male(X).

sister(X,Y):-
parent(Z,X),
parent(Z,Y),
female(X),
X\==Y.

brother(X,Y):-
parent(Z,X),
parent(Z,Y),
male(X),
X\==Y.

grandparent(X,Y):-
parent(X,Z),
parent(Z,Y).

grandmother(X,Z):-
mother(X,Y),
parent(Y,Z).

grandfather(X,Z):-
father(X,Y),
parent(Y,Z).

wife(X,Y):-
parent(X,Z),
parent(Y,Z),
female(X),
male(Y).

husband(X,Y):-
parent(X,Z),
parent(Y,Z),
male(X),
female(Y).

uncle(X,Z):-
brother(X,Y),
parent(Y,Z).

aunt(X,Z):-
sister(X,Y),
parent(Y,Z).

#sum

sum(X,Y):-
 S is X+Y,
 write(S).

#prime number set
%prime number
prime(2):- 
	write(2).
prime(X):- 
	prime(X, 2).

prime(X, Y):- 
	X =:= Y, 
	write(' '), 
	write(X).
prime(X, Y):- 
	Z is X mod Y, 
	Z \== 0, 
	X \== Y, 
	prime(X,Y+1).
prime(X, Y):- 
	Z is X mod Y, 
	Z =:= 0, 
	X \== Y.
   
input_prime(N):- 
	input_prime(N, 2).
input_prime(N, X):- 
	N =:= X, prime(X).
input_prime(N, X):-
	N > X, prime(X), 
	W is X + 1, 
	input_prime(N, W).
command:input_prime(---)
