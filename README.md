# ***Web Scraper di Recensioni Google***
<img src="data/img_doc/google_img.png" alt="Google review logo" style="height: 150px; width:400px;"/>

>La seguenta guida illustra come utilizzare e configurare il **Web Scraper** realizzato con [*Selenium*](https://www.selenium.dev/).
> 
>Il programma è stato sviluppato per raccogliere dati testuali per un progetto di ***Natural Language Processing*** svolto durante il mio periodo di stage presso [*BSdesign Srl*](https://www.bsdesign.eu/).
---

## ***Indice***
- [Installazione](#inst)
- [Modalità d'uso](#use)
- [Configurazione JSON file ](#conf)
- [Avvio Programma](#start)
- [Conclusioni](#end)

---
<a id="inst"></a>
## ***Installazione***
Per utilizzare il ***Web Scraper*** è necessario avere una versione di [Python](https://www.python.org/) installata sul proprio dispositivo.

Per comodità consiglio di installare [Anaconda](https://www.anaconda.com/products/individual), in modo da gestire più facilmente il setup di un ***ambiente virtuale***.

Dopo aver installato Anaconda, create un ambiente virtuale con il seguente comando:

    conda create -n <Nome Ambiente> python=3.9.7

Successivamente attivate l'ambiente con:

    conda activate <Nome Ambiente>

Infine dopo esservi collocati nella cartella da linea di comando, eseguite il seguente comando per installare tutte le dipendenze necessarie per il programma:

    pip install -r requirements.txt

Per una guida più dettagliata su Anaconda e gli ambienti virtuali vi consiglio questo [sito](https://www.geeksforgeeks.org/set-up-virtual-environment-for-python-using-anaconda/).

---
<a id="use"></a>
## ***Modalita d'uso***

Prima di utilizzare il Web Scraper è necessario svolgere un primo lavoro di ***analisi*** della pagina di recensioni.

In particolare bisogna raccogliere tutti gli ***elementi HTML*** della pagina necessari al web scraper per funzionare.

Prima di tutto ci serve l'***URL*** della pagina, il web scraper si basa su questa pagina di recensioni:

<img src="data/img_doc/pagina_rev.png" alt="pagina reviews" style="height: 200px; width:400px;"/>




