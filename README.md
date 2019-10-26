# Tolerance-Calculator
Program to calculate linear plastic tolerances 
Nom del programa : Lineal tolerances calulator

Input : valor dimensió 
Nivell de qualitat : Coarse , médium , High 
Numero de cavitats : 1,2,4,6,8,16,32
Material : POMC;POMH ,PA66;PA6;PBT;PEHD;ABS;
Output : rang de tolerància 

Formula de càlcul :
Quality_level
Coarse = 0,0075
Medium=0,005
High=0,003
CavityNumber
Cav1=1
Cav2=1,03
Cav4=1,08
Cav6=1,10
Cav8=1,15
Cav16=1,2
Cav32=1.3
Material 
POMC=1
POMH=1
Pa6=1 
Tots els materials tenen efecte neutre sobre el càlcul de moment ( =1) 
Forma de càlcul 

ToleranceRange = Dimension*Quality_Level*CavityNumber*Material
Exemple :
Quality =coarse 
Nombre de cavitats = 8 
Material pom 
Dimensió 100mm 

100 * 0,0075 * 1,15 * 1=0,8625 de camp de total de tolerància o ±0,43  



Entorno visual  ( proposta ) :

 

Excepcions:
Ha de donar missatge error si entrem str en lloc de un valor numèric 
 
