# Algoritmes de Tècniques d'Intel·ligència Artificial
### **_Tècniques d'Intel·ligència Artificial | TecnoCampus Mataró | Enginyeria Informàtica_**


## [Carpeta Greedy](Greedy) -> Algoritme Greedy

La carpeta inclou la implementació de l'algoritme Greedy en Python.


## [Carpeta P1](P1) -> Algoritme A* + Backtracking

La carpeta inclou l'enunciat de la Pràctica 1 de l'assignatura i la seva implementació en Python. Es basa en l'algoritme Greedy de la carpeta Greedy, amb modificacions per a fer ús d'heurístiques a l'estil d'A*, calculades a partir de tècniques recursives del caire de backtrackings.


### Exemple d'execució

![image](https://user-images.githubusercontent.com/60795194/170134975-960c8007-94db-4576-8538-713109b701ed.png)

Primer es demanen les diferents comandes (si no corresponen amb cap nom de taula s'interpreten com a buides).

S'estudien tots els recorreguts possibles entre la Cuina i cadascun dels destins indicats i 'escull el millor a cada destí.
D'entre els millors recorreguts a cada destí, s'escull el que té un menor cost i es determina com a primer destí (en aquest cas A3, amb un cost de 1.5).

![image](https://user-images.githubusercontent.com/60795194/170135019-df5d5d4d-ec7a-41c9-89b1-312f33569d45.png)

Des d'A3, s'estudien els millors recorreguts a cadascun dels destins restants. S'escull el millor dels millors recorreguts, i el següent destí és E4, amb un cost de 2.

![image](https://user-images.githubusercontent.com/60795194/170135085-a7271943-c641-4919-8693-be80053f047a.png)

Des d'E4, s'estudien els millors recorreguts a cadascun dels destins restants. S'escull el millor dels millors recorreguts, i el següent destí és D1, amb un cost de 9.0.

Des de D1, s'estudien els millors recorreguts a cadascun dels destins restants, i s'escull l'únic que queda: a C3, amb un cost de 5.

![image](https://user-images.githubusercontent.com/60795194/170135109-8477858c-f3e5-4bd5-8b9f-c7c9ddecc76b.png)

Finalment, es torna a la Cuina. Se n'estudia el camí des del node actual, C3, amb un cost de 9.25.

Per acabar, s'indica tot el recorregut realitzat, i el seu cost final: 26.75.


### Breu explicació del codi

Primer, el programa compta amb diverses funcions (amb noms que s'han procurat de fer autoexplicatius, i comentaris addicionals):
![image](https://user-images.githubusercontent.com/60795194/170135257-a37b295d-1eff-409e-9cbb-7eea80208d16.png)
![image](https://user-images.githubusercontent.com/60795194/170135333-c000ca3b-a299-45da-b4ca-17bef1413c6a.png)
![image](https://user-images.githubusercontent.com/60795194/170135417-2e686bbe-508a-47e5-9f69-96d3494b8cb0.png)

Després, es creen manualment els nodes de les taules amb què compta el restaurant (en una implementació que requerís de més flexibilitat, es podria afegir un sistema de lectura de nodes des d'un fitxer extern, per exemple):
![image](https://user-images.githubusercontent.com/60795194/170135430-1d2bf481-5de8-4b88-89a1-40cd91065e8b.png)

Finalment, es crea una llista amb tots els nodes i es creen diverses variables globals necessàries:

![image](https://user-images.githubusercontent.com/60795194/170135462-6e99383b-d29d-419e-872b-c1212419be2e.png)

S'executa la funció que crea l'arbre de nodes, una per a obtenir tot el camí del robot cambrer amb quatre parades màximes, i s'imprimeix la informació del recorregut.


El bucle general més rellevant és el següent, que va obtenint camins mentre quedin destins a visitar:
![image](https://user-images.githubusercontent.com/60795194/170137986-9f407420-0141-41fc-b82e-aeccdfe3bc9d.png)

Entrant en detall, la selecció dels millors camins per a cada destí es tracta en el següent mètode:
![image](https://user-images.githubusercontent.com/60795194/170138129-92796ff1-1d37-4d6e-818e-ff0318d5a038.png)

Finalment, convé apuntar el mètode que executa la recursivitat de l'algorisme:
![image](https://user-images.githubusercontent.com/60795194/170138173-6f5ec47e-63c6-4302-8153-2460a9bc8c2b.png)



*Apunts previs d'interpretació de l'enunciat*:

L'heurística és la suma del cost acumulat que necessitem per arribar a un destí.
Ens quedarem amb el que tingui una heurística menor.

La qüestió és que hem de crear un algoritme recursiu que sigui capaç d'analitzar tots els possibles camins que ens porten a un objectiu, però sense caure en bucle.

Proposta: Analitzar visited però dels childs, possiblement juntar-ho amb backtracking.

