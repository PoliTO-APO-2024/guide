# Testing
Introdurre errori nel proprio codice è molto semplice e non sempre la loro presenza è evidente.
Un programma potrebbe andare avanti per anni prima che la giusta combinazione di input possa causare un problema.
Se il software è impiegato in un ambiente *safety critical* 
(si pensi ad esempio al software di stabilizzazione di un areo, apparecchi per il supporto vitale, etc...),
la presenza di errori "invisibili" nel codice può avere effetti molto gravi.

In python questo è accentuato dal fatto che, rispetto a linguaggi compilati, molti controlli sulla correttezza del codice sono fatti a runtime (si pensi al type checking). Bisogna quindi aspettare che l'errore si verifichi per sapere che ci sia.


## Unit testing
L'Unit testing è un metodologia che consiste nel testare separatamente piccole porzioni di codice. In programmi a oggetti le unità sono solitamente metodi o funzioni.

L'unit testing viene comunemente eseguito in tre modalità diverse: white box, black box, grey box testing.
Nel primo caso chi scrive i test ha conoscenza completa del codice che va a testare, nel secondo caso, invece, non ne ha nessuna, ma interagisce unicamente tramite l'interfaccia che esso espone.
Nel terzo caso, si ha una conoscenza parziale del codice che si testa.


## Coverage
La coverage è la percentuale di codice che viene testata dai test eseguiti.
Sono presenti diverse metriche per calcolarle.
Alcune delle più comuni sono:
- instruction coverage: tutte le istruzioni sono state eseguite almeno un volta
- branch coverage: tutti i "rami" in cui si divide il codice (per esempio degli *if*) sono eseguiti almeno una volta
- condition coverage: ogni espressione booleana elementare è stata testata avendo come risultato sia vero che falso.

Avere 100% coverage, tuttavia, non è sufficiente per assicurarsi che il codice non contenga errori.
Si pensi ad esempio a tutte le possibile combinazioni di vero-falso che si possono avere data una serie di *if* in catena. Oppure edge cases particolari, tipo ritrovarsi con un divisore pari a zero o generare overflow.


## Python unittest
Python fornisce una libreria di default chiamata [unittest](https://docs.python.org/3/library/unittest.html) che, come dice il nome, permette di svolgere unit testing.
Questa libreria è stata sviluppata prendendo come riferimento la liberia [JUnit](https://junit.org/junit5/) del linguaggio Java.
Questo è rispecchiato dal fatto che metodi e funzioni seguono la notazione *lowerCamelCase* invece di quella *snake_case* indicata dalla guida di stile [PEP 8](https://peps.python.org/pep-0008/).

I test vengono raggruppati in classi che ereditano dalla classe unittest.Testcase.
Il raggruppamento si esegue solitamente per funzionalità da testare.
Ogni metodo della classe il cui nome inizia con la parola *test* è un diverso unit test.
È possibile definire dei metodi da lanciare prima e dopo ogni test, di modo che eseguano del codice di setup e pulizia comune a tutti i test.
Per farlo basta scrivere due metodo chiamati setUp() e tearDown().


## Eseguire test
In questo corso non viene richiesto di saper scrivere test, ma soltanto di saperli lanciare sul proprio codice.
Per farlo, creare una cartella che li contenga, solitamente chiamata tests (è importante che ci sia la "s" finale, perché test, senza "s", è un modulo standard di python e questo può creare problemi) nella directory principale del progetto, a fianco degli altri moduli e packages sviluppati.

La cartella contenente questa guida presenta un esempio.
Il modulo *src.counter* implementa un contatore, mentre *test.test_counter* contiene i test.

Lanciare i test dalla cartella principale del progetto (in questo caso la cartella che contiene la guida), usando il seguente comando che permette di specificare il modulo che contiene i test.

```bash
python -m unittest tests.test_counter
```

Altrimenti è possibile lanciare i test contenuti in uno specifico testcase (classe) o un singolo unit test.
Tramite il flag -v (--verbose) è possibile ottenere un output più dettagliato.

```bash
python -m unittest -v tests.test_counter.TestIncrement
python -m unittest -v tests.test_counter.TestIncrement.test_multiple_increment
```

E possibile lanciare tutti i test del progetto, indipendentemente da dove siano, tramite il comando senza parametri:
```bash
python -m unittest
```
Per funzionare, i nomi dei moduli contenenti i test devono iniziare con *test_*.
Inoltre, se essi si trovano in un package, deve essere presente il file *\_\_init\_\_.py* (anche vuoto).

## Esame
All'esame i test che vengono lanciati sul vostro codice sono da considerarsi black box,
ovvero vengono scritti senza conoscere la vostra implementazione.

Prendendo come esempio il modulo *counter*, 
quello che viene visto da chi scrive i test (e da chi li esegue per testare la vostra prova)
è l'interfaccia della classe, ovvero quello che è stato riportato (a titolo di esempio) nel file *interface.py*.

È pertanto fondamentale che la vostra implementazione segua accuratamente i requisiti richiesti nel testo della prova
(tipo e numero parametri metodo, tipo valore restituito metodo, struttura stringhe etc...)

D'altra parte, ciò che **NON** viene richiesto o specificato accuratamente nel testo,
**NON** viene testato e **NON** è necessario venga implementato.

Per esempio, se un metodo accetta come parametro un intero da utilizzare come divisore
e non viene detto niente sui valori ammessi,
non deve essere controllato che questo sia diverso da zero perché i test non esploreranno quel caso.

## VSCode
Per lanciare i test, utilizzare i comandi descritti in precedenza nel terminale di VSCode.

## PyCharm
Per lanciare i test tramite PyCharm, fare tasto destro sulla cartella dei test e selezionare *Run*.

In questo modo i test vendono lanciati usando come *working directory* la cartella che li contiene.
È necessario impostare la *working directory* per essere la cartella principale del progetto
(in questo caso la cartella che contiene la guida).
Questa convenzione verrà sempre usata quando il vostro codice verrà sottoposto a test (anche il compito d'esame).

Per farlo andare usare il menù a tendina vicino all bottone verde *Play* e andare su *Edit configurations*.
Aprire dal menù laterale la configurazione che è stata creata in automatico per i test e cambiare il percorso.