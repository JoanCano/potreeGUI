En el siguiente post se pretende mostrar una potente herramienta open source con la cual es realmente sencillo visualizar y servir nubes de puntos desde nuestro navegador.

## ¿Qué es Potree?
A grandes rasgos, [Potree](www.potree.org) se trata de un software de código abierto basado en WebGL, capaz de renderizar grandes nubes de puntos.

En su [página web](www.potree.org) se pueden comprobar varios ejemplos de nubes de puntos obtenidas por fotogrametría o escáner.

Está diseñado para trabajar con nubes de puntos en formato LAS, por lo que en el caso de que queramos transformar una nube de puntos, por ejemplo obtenida por fotogrametría, ésta la tendremos que transformar previamente a LAS para poder transformar la nube de puntos al formato con el que trabaja Potree (octrees).

## Descarga del software
Para proceder a utilizar Potree, descargaremos su software desde [www.potree.org/download](http://www.potree.org/download.html).

En la página se encuentra PotreeConverter, que se trata del conversor de LAS a octrees y el software en sí (source code). Sin embargo, solo hará falta PotreeConverter.

## Cómo ejecutarlo
Antes de empezar, conviene instalar un servidor web que trabaje en local para poder visualizar la nube de puntos (Potree requiere ciertos permisos en navegadores) sin tener que subirla a un servidor como tal.

Como "simulador" de servidor web se utilizará [Xampp](https://www.apachefriends.org/de/index.html), el cual se instalará en ```C:\xampp```.

Una vez se tiene todo descomprimido e instalado, se procede a transformar la nube de puntos. Para ello, se abre el símbolo del sistema (cmd) escribiendo la siguiente línea de código.

```
./PotreeConverter.exe C:/pointcloud.las -o C:/xampp/htdocs/potree --generate-page pageName
```
Donde:
- ```./PotreeConverter.exe``` se trata del ejecutable que se ha descargado.
- ```C:/pointcloud.las``` es la nube de puntos que queremos transformar.
- ```C:/xampp/htdocs/potree``` es la ruta donde se va a guardar.
- ```pageName``` Es el nombre que le asignaremos al archivo de salida

*Queda claro que las rutas pueden variar según dónde hayamos colocado los archivos.*

Una vez se ejecute nos debe aparecer una ventana como la siguiente, la cual indica que el proceso se está realizando.

![CMD](https://github.com/JoanCano/joancano.io/blob/master/images/imgPotree/resultado.png)

Cuando se haya realizado el proceso, es muy importante que los archivos generados se encuentren dentro de ```C:\xampp\htdocs``` para poder visualizar la nube de puntos en el navegador:

De manera que solo quedará abrir y visualizar la nube de puntos desde una ruta similar a la siguiente:

[http://localhost/potree/pageName.html](http://localhost/potree/pageName.html)

## Una pequeña contribución
Abrir la consola puede paracer algo tedioso, por lo que se ha creado el siguiente [ejecutable](https://github.com/JoanCano/potreeGUI/blob/master/PotreeConverter.exe) para evitar tener que escribir en la consola de Windows.

Al ejecutar potreGUI nos aparecen las siguientes ventanas:
1. Nos pregunta que nombre le damos al archivo
2. El archivo LAS que queremos transformar
3. El directorio donde queremos guardarlo (C:\xampp\htdocs)

![nombre](https://github.com/JoanCano/joancano.io/blob/master/images/imgPotree/1.PNG)

![2](https://github.com/JoanCano/joancano.io/blob/master/images/imgPotree/2.png)

![3](https://github.com/JoanCano/joancano.io/blob/master/images/imgPotree/3.png)

## Ejemplo práctico con una nube de puntos LiDAR del PNOA

Para mostrar el resultado que puede obtenerse con una nube de puntos LAS, se han utilizado 6 hojas LiDAR-PNOA que a su vez han sido unidas en CloudCompare.

Aquí tenéis el resultado. Suerte!

![CMD](https://github.com/JoanCano/joancano.io/blob/master/images/imgPotree/resultado2.PNG)
