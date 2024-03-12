# Moduli e pacchetti
In questa guida vengono introdotti i concetti base della gestione di progetti python,
ovvero la creazione di progetti con più file tramite l'organizzazione in moduli e pacchetti.

È possibile utilizzare un IDE (ad. es. PyCharm e VSCode) o anche un semplice editor di testo (come *blocco note*).


## Indice
1. [Moduli](#moduli)
    1. [Creare e importare un modulo](#creare-e-importare-un-modulo)
    2. [Namespace e symbol table](#namespace-e-symbol-table)
    3. [Diversi modi per importare](#diversi-modi-per-importare)
    4. [Import vs esecuzione](#import-vs-esecuzione)
2. [Pacchetti](#pacchetti)
    1. [Creazione di pacchetti](#creazione-di-pacchetti)
    2. [Importare pacchetti con \_\_init\_\_.py](#importare-pacchetti-con-__init__py)
    3. [Pacchetti parallleli](#pacchetti-paralleli)
3. [Dove Python cerca moduli e pacchetti](#dove-python-cerca-moduli-e-pacchetti)
    1. [Pycharm](#pycharm)
    2. [Terminale](#terminale)
4.  [Riferimenti](#riferimenti)


## Moduli
Se il progetto su cui si lavora contiene molto codice,
è scomodo avere tutto i un unico file. 
Dividere il progetto su file diversi, chiamati moduli, aggiunge una suddivisione
fisica alla suddivisione logica del codice.

La modularizzazione rende il sorgente più facile da mantenere e modificare (maintainability),
e permette di riutilizzare una parte del codice senza doverlo duplicare (reusability).
Inoltre si evitano collisioni non volute degli identificatori
(per esempio sovrascrivere variabile che si credeva di non aver ancora introdotto).

### Creare e importare un modulo
Creare un nuovo progetto (se si usa PyCharm) o una nuova cartella per contenere il codice che verrà creato in questo tutorial.

Creare il file *greetings.py*, contenente una funzione che, passato il nome dell'utente,
stampi un messaggio di saluto:

```python
def greet(name):
  print("Hello {}!".format(name))
```

Nella stessa cartella, creare il file *main_program.py*,
che importi il modulo e lo usi per salutare l'utente,
richiedendogli d'inserire il proprio nome:

```python
import greetings
name = input("Insert your name: ")
greetings.greet(name)
```
Come si può vedere la keyword *import* permette d'importare un modulo
in un diverso sorgente python.

Il progetto assumerà la seguente struttura:
```.
├── main_program.py
└── greetings.py
```

In PyCharm o VSCode, lanciare lo script *main_program.py* utilizzando il bottone play dell'interfaccia.

Se si usa il terminale, lanciare il seguente comando dalla cartella di progetto:
```bash
python main_program.py
```

Ma non è finita qui, *main_program* è esso stesso un modulo
e può essere eseguito da python, in modo equivalente,
rendendolo esplicito tramite il flag *-m*:

```bash
python -m main_program
```

### Namespace e Symbol table
Ogni modulo definisce un proprio *namespace* locale,
ovvero una collezione dei nomi simbolici che sono stati definiti
(nomi variabili, nomi funzioni, etc...) e le relative informazioni degli oggetti a cui questi simboli fanno riferimento.

I simboli appartenenti al namespace locale sono contenuti in una tabella dei simboli
locale (*symbol table*), ovvero visibile solo dal modulo stesso.

Aggiungere al file *greetings.py* la seguente linea di codice (al di fuori della funzione greet),
che stampa la tabella dei simboli locale del modulo.

```python
print('Symbol table of module "greetings" :\n {}'.format(dir()))
```

Eseguire il modulo *greetings* tramite IDE o tramite terminale:
```bash
python -m greetings
```
Diversi simboli sono automaticamente definiti dall'interprete
(*\_\_name\_\_*, *\_\_builtins\_\_*, ecc...),
ma anche il simbolo della funzione *greet*,
definita dal programmatore.

### Diversi modi per importare
Analizzando il codice in *main_program.py* si vede che
per accedere alla funzione greet bisogna chiamare
``greetings.greet(...)`` invece d'invocare direttamente
``greet(...)``. 

Questo perché ``import greetings``
aggiunge alla *symbol table* di *main_program*
solamente il simbolo *greeting* e non tutti i simboli del modulo importato.
Ciò è confermato se si aggiunge la seguente istruzione a *main_program*
e lo si esegue:

```python
print('Symbol table of module "main_program" :\n {}'.format(dir()))
```

È tuttavia possibile rinominare il simbolo quando lo si importa:
```python
import greetings as grt
...
grt.greet(name)
```
Oppure aggiungere direttamente uno o più simboli da un modulo:
```python
from greetings import greet #, simbolo2, simbolo3
...
greet(name)
```
O aggiungere direttamente tutti i simboli 
(da usare con cautela per evitare collisioni).
I simboli che iniziano per *"\_"* non vengono importati.

```python
from greetings import *
...
greet(name)
```

### Import vs esecuzione
Prestando attenzione all'output di *main_program.py*
vi sarete resi conto che lasciando la linea ```print(...)```
all'interno di *greetings.py*, questa viene eseguita
non solo quanto si esegue direttamente il modulo,
ma anche quando questo viene importato.

Cio avviene perché, quando il modulo è importato,
l'interprete esegue tutte le istruzioni presenti nel file,
come in una normale esecuzione.

Quello che l'interprete fa, però, è cambiare il valore associato
al simbolo *\_\_name\_\_*.
Questo viene settato a *"\_\_main\_\_"*
unicamente se il modulo è stato eseguito direttamente.
Con un semplice controllo, si può pertanto escludere del
codice dall'esecuzione quando il modulo viene importato.

Cambiare le seguenti linee in *greetings.py* 
e lanciare *main_program.py*
```python
if __name__ == "__main__":
    print('Symbol table of module "greetings" :\n {}'.format(dir()))
```
Ora la symbol table di *greetings* non viene più stampata
durante l'import, ma viene visualizzata se si lancia *greetings.py*.


## Pacchetti
Quando la grandezza del progetto cresce,
e conseguentemente anche il numero di moduli, 
è conveniente raggruppare quest'ultimi in pacchetti.
Un pacchetto è fondamentalmente una cartella che contiene più
moduli logicamente connessi.

### Creazione di pacchetti
Creare una cartella chiamata *salutations* in quella principale
e spostare il file *greetings.py* all'interno di essa.
Successivamente creare un altro file all'interno di *salutations*
chiamato *goodbye.py*.
La struttura del progetto sarà la seguente:

```
.
├── main_program.py
└── salutations
    ├── goodbye.py
    └── greetings.py
```


All'interno del file *goodbye.py* aggiungere una funzione che dica arrivederci l'utente:
```python
def byebye(name):
  print("Bye bye {}!".format(name))
```

Modificare il *main_program.py* per supportare il cambiamento:
```python
import salutations.greetings
import salutations.goodbye

print('Symbol table of module "main_program" :\n {}'.format(dir()))

name = input("Insert your name: ")
salutations.greetings.greet(name)
salutations.goodbye.byebye(name)
```

È anche possibile utilizzare la sintassi con *from* e *as*:
```python
from salutations.greetings import greet
from salutations.goodbye import byebye as bb
...
greet(name)
bb(name)
```

### Importare pacchetti con *\_\_init\_\_.py*
Modificare il *main_program.py*, nel seguente modo e verificare che **NON** funziona:
```python
import salutations
...
salutations.greetings.greet(name)
salutations.goodbye.byebye(name)
```
Comparando la symbol table con quella precedente (*import salutations.greetings*)
si vede che non ci sono differenze: in entrambe è definito il simbolo *salutations*.

Però, se si stampano le proprietà
(verranno definite meglio quando verranno introdotti gli oggetti) associate a *salutation*, si vede che nessun simbolo è definito:
```python
import salutations
print('Symbol table of module "salutations" :\n {}'.format(dir(salutations)))
```
Se invece si fanno gli import "estesi", i simboli dei moduli appaiono:
```python
import salutations.greetings
import salutations.goodbye
print('Symbol table of module "salutations" :\n {}'.format(dir(salutations)))
```
Questo accade perché *import salutation* definisce solo il simbolo,
ma non ha associato un modulo da eseguire che crei i suoi simboli,
cosa che invece accade importando un modulo. Esso viene eseguito
e i simboli delle variabili e funzioni creati.

È però possibile associare un modulo da eseguire quando si esegue l'import del package.
Questo può fare l'import dei moduli al suo interno. 
Creare un file chiamato *\_\_init\_\_.py* nella cartella *salutations*, contenente il seguente codice:

```python
import salutations.greetings, salutations.goodbye
```

Il progetto assumerà la seguente struttura:
```
.
├── main_program.py
└── salutations
    ├── goodbye.py
    ├── greetings.py
    └── __init__.py
```

Se ora si riesegue l'import di *salutations* i simboli vengono correttamente definiti.
```python
import salutations
print('Symbol table of module "salutations" :\n {}'.format(dir(salutations)))
```

È anche possibile modificare *\_\_init\_\_.py* nel seguente modo:
```python
from salutations.greetings import greet
from salutations.goodbye import byebye
__all__ = ['greet','byebye']
```
per permettere la seguente sintassi di import:

```python
from salutations import greet, byebye
...
greet(name)
byebye(name)
```

Il simbolo *\_\_all\_\_* permette di usare anche la seguente sintassi di import. 

```python
from salutations import *
...
greet(name)
byebye(name)
```
In questo modo lo sviluppatore del modulo può controllare
cosa l'utilizzatore importa quando decide d'importare "tutto".

### Pacchetti paralleli
Creare nella cartella principale un nuovo pacchetto chiamato *others*.
Nel pacchetto creare un modulo python chiamato *parallel.py* che importa il modulo *greetings.py*.

```python
import salutations.greetings as grt
grt.greet("John Doe")
```

La struttura del progetto sarà la seguente:
```
.
├── main_program.py
├── others
│   └── parallel.py
└── salutations
    ├── goodbye.py
    ├── greetings.py
    └── __init__.py
```

Lanciare lo script *others.py* tramite IDE
o tramite terminale posizionandosi nella cartella principale del progetto, al fine di testarne il funzionamento:

```python
python -m others.parallel
```


## Dove python cerca moduli e pacchetti
Quando si fa l'import l'interprete Python deve sapere dove cercare il pacchetti e moduli da importare.
Le directory in cui vengono cercati sono le seguenti:
- la directory da cui si trova lo script o quella da cui si avvia l'interprete
- la lista di directory definite nella variabile d'ambiente *PYTHONPATH* del sistema operativo
- una lista di directory stabilita quando python viene installato (dipende dall'installazione)

Per stampare l'intera lista di directory è possibile aggiungere a *main_program.py* le seguenti linee di codice.
```python
import sys
print(sys.path)  # print non è necessario dall'interprete
```
Eseguendolo verrà stampata la lista di directory in cui Python cerca i moduli e pacchetti.
Nella lista apparirà il percorso della cartella contenente il progetto.

Creare la cartella *libs* e spostare all'interno le cartelle *salutations* e *others*.
La struttura del progetto sarà la seguente:

```
.
├── libs
│   ├── others
│   │   └── parallel.py
│   └── salutations
│       ├── goodbye.py
│       ├── greetings.py
│       └── __init__.py
└── main_program.py
```

Se si esegue *main_program.py* gli import falliscono, in quanto i percorsi non sono più corretti.
Per non doverli cambiare, e continuare a usarli riferendoli alla cartella *lib*,
basta aggiungere il percorso della cartella *lib* al *sys.path*, prima di effettuare l'import di *salutations*:

```python
import sys
sys.path.append("percorso di libs")
...
from salutations import greet, byebye
```

### VSCode
VSCode, quando si usano i bottoni dell'interfaccia grafica uno script,
aggiunge solamente la directory in cui si trova lo script al *PYTHONPATH*.

Se si vuole modificare questo comportamento è possibile accedere alla sezione *Run and debug* nella barra laterale,
e selezionare *create a launch.json file*.
Quando richiesto selezionare *Python Debugger* e, successivamente, *Python File*.
Questo creerà il file ```launch.json``` nella cartella ```.vscode``` nella home del progetto.

Il ```launch.json``` permette di configurare le opzioni di esecuzione e debugging degli script Python.
Consultare la [documentazione](https://code.visualstudio.com/docs/editor/debugging#_launch-configurations) per sapere come modificarlo.
Modificare la configurazione di default come indicato sotto.

```json
{
   "name": "Python Debugger: Current File",
   "type": "debugpy",
   "request": "launch",
   "program": "${file}",
   "console": "integratedTerminal",
   "cwd": "${fileDirname}",
   "env": {"PYTHONPATH": "${workspaceFolder}${pathSeparator}lib"}
}
```

*cwd* indica la working directory da dove viene lanciato lo script,
mentre *env* permette di aggiungere variabili di ambiente, tra cui *PYTHYONPATH*.
L'esempio aggiunge a **PYTHYONPATH** il percorso del pacchetto ```lib```.
Lanciando lo *others.py* tramite il bottone play presente nella sezione *Run and debug**, lo script ora troverà il modulo *salutations*.

### PyCharm
PyCharm, quando si usano i bottoni dell'interfaccia grafica per lanciare gli script,
aggiunge di default la directory principale del progetto alla lista di directory in cui python cerca i pacchetti.

Se il codice utilizza import riferiti a una directory diversa, per esempio alla cartella dello specifico laboratorio,
è possibile aggiungerla alla lista di ricerca dell'interprete facendo tasto destro su di essa e selezionando
```Mark Directory as -> Sources Root```.

Inoltre PyCharm, di default, quando si fa tasto destro su un file e si seleziona *Run*,
lancia lo script utilizzando come *working directory* la cartella che lo contiene.
Per lanciare un modulo che **NON** si trova nel directory principale del progetto utilizzando la directory principale come *working directory*,
aprire il menù a tendina vicino al pulsante play e cliccare su *Edit configurations*.
Cliccare sulla configurazione di lancio dello script e cambiare la *working directory* inserendo il percorso della cartella principale.

### Terminale

Aggiungere come prime due linee di *parallel.py* il codice sopra riportato che stampa *sys.path*.
Lanciare poi i seguenti comandi dalla cartella *lib*:

```python
python others/parallel.py
python -m others.parallel
```

Nel primo caso python aggiunge alla lista di directory la cartella in cui si trova lo script *parallel.py*,
che non permette di trovare il package *salutations*.
Il secondo comando, invece, aggiunge alla lista la cartella da cui viene lanciato comando, ovvero *lib*.
In questo modo quando *parallel* viene eseguito,
l'interprete riesce a trovare il package *salutation* e i moduli in esso contenuti.


## Riferimenti
- [Moduli e Pacchetti](https://realpython.com/python-modules-packages/)









