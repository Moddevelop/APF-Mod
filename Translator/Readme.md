# Translator Engine 

**__esto funciona de la siguiente manera __**

translator engine se creo, porque en las carpetas 📁 "VuStrings"
habia unos binarios que no se extraían así que pense en algo ingenioso.

--cree un extractor para los textos de traducción:--
* es.bin
* en.bin
* fr.bin
* ru.bin

# USO

lo primero que debe hacer es crear una carpeta llamada 

`
 input
`
ahi es donde guardara su:

` es.bin ` `en.bin` `fr.bin` ` deb.bin` `ru.bin`

# ejecusion del código 

* luego de guardar su archivo de texto en binario ahi
* ejecutas este comando en la terminal:

""bash

python bin2json.py

""

* entonces ahi se creara una carpeta llamada `extracted`
* en esa carpeta encontraras archivos ` json ` que son editables y fácil de leer

$ luego de que editen el archivo `json` con nuevos links y textos ahora iria reconstruir 
el binario:

""bash

python build.py

""
 
*este reconstruye el binario y lo guarda dn una carpeta llamada `ouput`.
y después toca remplazar los binarios originales del juego por las modificadas.

