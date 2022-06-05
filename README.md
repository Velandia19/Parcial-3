# Parcial-3
Creación de base de datos y aplicación a la agroindustria 
Resumen 
En este programa se crea una base de datos a partir de librerías y métodos desarrollados en Python, que permiten a un agricultor tener un modelaje simple en la evolución de una especie que afecta a sus cultivos, como lo es la mosca de fruta (Drosophila melanogaster),
dado que es una especie con características biológicas especiales, este programa también puede ser utilizado a la hora de estudios genéticos en la Drosophila melanogaster ya que su reproducción es rápida y el breve ciclo de vida (15-21 días) facilitan el uso del método crispr, también aproximadamente el 61 % de los genes de enfermedades humanas que se conocen tienen una contrapartida identificable en el genoma de las moscas de la fruta.
Desarrollo
A partir de la librería sqlite3 y la aplicación DB browser se crean 3 tablas las cuales tienen una relación entre sus datos, los nombres de las tablas son usuario1 que contiene la cantidad de moscas iniciales y el nombre de la planta de fruta que está afectando, la segunda tabla es usuario2 que también contiene el nombre de la especie y la cantidad de plantas de esta, la tercera tabla es many que aloja los tres datos obtenidos del usuario, y a partir de estas tres tablas se crean funciones con conexión a la base de datos que reciben parámetros para obtener diversas funcionalidades de consulta, visualización de  datos, desarrollo de operaciones, eliminar datos, y calcular un modelaje que representa la cantidad de moscas de la totalidad de sus cultivos de fruta luego de 5 y 10 días a partir de las cantidades iniciales.
Implementación 
Inicialmente un cultivo tiene 2 de moscas de fruta. En t=5 días se determina que el número de moscas es 60. Si la razón de crecimiento es proporcional al número de moscas P(t) presentes en el tiempo t se encuentra la función que modela este crecimiento
Donde p es la cantidad de moscas 
k es la razón de crecimiento proporcional a la cantidad de moscas 

La ecuación diferencial de primer orden es 
dp/dt=kp
Esta ecuación se puede resolver por el método de separación de variables por lo que: 
∫dp/p=∫k dt
ln⁡(p)=kt+c_1
Despejamos a p 
p=ce^kt
Esta es la función de modelaje, y a partir de las condiciones iniciales descritas anteriormente, se encuentra la razón de crecimiento. 
p(5)=60
60=2e^(k(5))
60/2=e^5k
ln⁡(60/2)=5k

k=ln⁡(30)/5≈0.68023
Por lo que el modelo implementado en Python es 
p=2e^(ln⁡(30)/5 t)

