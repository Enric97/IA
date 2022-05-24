# Algoritmes de Tècniques d'Intel·ligència Artificial
### **_Tècniques d'Intel·ligència Artificial | TecnoCampus Mataró | Enginyeria Informàtica_**


## [Carpeta Greedy](Greedy) -> Algoritme Greedy

La carpeta inclou la implementació de l'algoritme Greedy en Python.


## [Carpeta P1](P1) -> Algoritme A* + Backtracking

La carpeta inclou l'enunciat de la Pràctica 1 de l'assignatura i la seva implementació en Python. Es basa en l'algoritme Greedy de la carpeta Greedy, amb modificacions per a fer ús d'heurístiques a l'estil d'A*, calculades a partir de tècniques recursives del caire de backtrackings.


### Exemple d'execució

![image](https://user-images.githubusercontent.com/60795194/170134975-960c8007-94db-4576-8538-713109b701ed.png)

![image](https://user-images.githubusercontent.com/60795194/170135019-df5d5d4d-ec7a-41c9-89b1-312f33569d45.png)

![image](https://user-images.githubusercontent.com/60795194/170135085-a7271943-c641-4919-8693-be80053f047a.png)

![image](https://user-images.githubusercontent.com/60795194/170135109-8477858c-f3e5-4bd5-8b9f-c7c9ddecc76b.png)


### Breu explicació del codi

![image](https://user-images.githubusercontent.com/60795194/170135257-a37b295d-1eff-409e-9cbb-7eea80208d16.png)
![image](https://user-images.githubusercontent.com/60795194/170135333-c000ca3b-a299-45da-b4ca-17bef1413c6a.png)
![image](https://user-images.githubusercontent.com/60795194/170135417-2e686bbe-508a-47e5-9f69-96d3494b8cb0.png)
![image](https://user-images.githubusercontent.com/60795194/170135430-1d2bf481-5de8-4b88-89a1-40cd91065e8b.png)
![image](https://user-images.githubusercontent.com/60795194/170135462-6e99383b-d29d-419e-872b-c1212419be2e.png)


*Apunts previs d'interpretació de l'enunciat*:

L'heurística és la suma del cost acumulat que necessitem per arribar a un destí.
Ens quedarem amb el que tingui una heurística menor.

La qüestió és que hem de crear un algoritme recursiu que sigui capaç d'analitzar tots els possibles camins que ens porten a un objectiu, però sense caure en bucle.

Proposta: Analitzar visited però dels childs, possiblement juntar-ho amb backtracking.

