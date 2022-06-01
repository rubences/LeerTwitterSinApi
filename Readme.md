# Instalación de Twint
Lo primero de todo será instalar la librería Twint con pip y para ello no hay más que ejecutar el comando:

1
pip3 install twint
Además, si vas a ejecutar la búsqueda de tweets en un Jupyter Notebook, es muy posible que te aparezca es siguiente mensaje de error:

1
RuntimeError: This event loop is already running
Una solución común para este problema consiste en insertar las siguientes dos líneas en nuestro código:

import nest_asyncio
nest_asyncio.apply()
1
import nest_asyncio
2
nest_asyncio.apply()
 
# Configuración de Twint para extraer tweets sobre la Eurocopa
Para esta primera prueba vamos a recopilar y almacenar en un fichero JSON los últimos 10000 tweets que hablen sobre la Eurocopa. Primeramente, importamos la librería necesaria:

1
import twint
Es hora de configurar y aplicar los filtros deseados a nuestra búsqueda de tweets y para ello simplemente creamos un objeto Config, que nos proporciona Twint, al cúal le vamos asignado alguna de las siguientes configuraciones:

+ Search: podemos usar este ajuste para extraer unicamente los tweets que contengan cierta palabra.
+ Username: para extraer los tweets de un usuario (no incluye los retweets pero sí las respuestas).
+ Lang: idioma de los tweets. Twint no es infalible y es posible que os encontréis tweets en otros idiomas a pesar de haber utilizado este filtro. Sin embargo, podremos deshacernos facilmente de estos tweets de idiomas no deseados posteriormente.
+ Filter_retweets: para excluir los retweets de los resultados.
+ Limit: con este ajuste le indicamos el número máximo de tweets a recopilar.
+ Output: dirección del fichero donde queremos alamacenar los datos.
+ Since: para extraer los tweets que se han publicado desde la fecha que consideremos.
+ Until: para recopilar los tweets que se han publicado hasta la fecha que queramos.
+ Min_likes: número mínimo de likes que deben tener los tweets extraidos.
+ Min_replies: número mínimo de respuestas.
+ Min_retweets: número mínimo de retweets.
+ Pandas: usaremos este ajuste si queremos almacenar los resultados en un Dataframe de la libería Pandas.
Podéis ver la lista completa de opciones de configuración aquí.
https://github.com/twintproject/twint/wiki/Configuration

En el siguiente ejemplo práctico, podeís ver un ejemplo de como configurar Twint para recopilar y almacenar en un fichero JSON los último 10000 tweets de este año en español que contengan el término "eurocopa" y que tengan más de 5 likes, retweets y respuestas:

 

1
import twint
2
import nest_asyncio
3
nest_asyncio.apply()
4
​
5
c = twint.Config()
6
c.Search = "eurocopa"
7
c.Lang = "es"
8
c.Filter_retweets = True
9
c.Limit = 10000
10
c.Since = '2021-01-01'
11
c.Output = "./tweets.json"
12
c.Min_likes = 5
13
c.Min_replies = 5
14
c.Min_retweets = 5
Fácil. ¿verdad? Para poner en marcha el rastreo simplemente debemos ejecutar el siguiente comando:

1
twint.run.Search(c)
Una vez finalizado la recopilación de tweets, veremos los resultados en el fichero tweets.json. Entre la información extraída, tendremos el texto del mensaje, la fecha de publicación y el nombre del autor.

En el siguiente código tenéis un ejemplo de como recopilar y almacenar en un Dataframe de Pandas los tweets publicados por el perfil de Twitter de Elon Musk:

1
c = twint.Config()
2
c.Username = "elonmusk"
3
c.Lang = "en"
4
c.Filter_retweets = True
5
c.Limit = 10000
6
c.Pandas = True
Una vez finalizada la extracción, podemos acceder al Dataframe y asignarlo a una variable de la siguiente manera:

1
tweets = twint.storage.panda.Tweets_df