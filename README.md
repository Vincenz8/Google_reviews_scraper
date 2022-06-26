# ***Scraper of Google's reviews***
<img src="data/img_doc/google_img.png" alt="Google review logo" style="height: 300px; width:1000px;"/>

>This guide illustrate how to use and configure this **Web Scraper** made with [*Selenium*](https://www.selenium.dev/).
> 
>This program was developed for gathering textual data for a ***Natural Language Processing*** project during my time at [*BSD design*](https://www.bsdesign.eu/).
---

## ***Contents***
- [Set up](#inst)
- [Web page](#use)
- [Configuring Json file](#conf)
- [Run program](#start)

---
<a id="inst"></a>
## ***Set up***
First, you need to install [Python](https://www.python.org/), i've used ***3.9.7*** version.

I recommend installing [Anaconda](https://www.anaconda.com/products/individual) because you can manage ***virtual environments*** more easily.

After installing Anaconda, you can create a virtual environment with the folllowing command from terminal:

    conda create -n <Env's name> python=3.9.7

Activate it with:

    conda activate <Env's name>

Then install dependences with:

    pip install -r requirements.txt

More details on Anaconda and virtual environments at this [site](https://www.geeksforgeeks.org/set-up-virtual-environment-for-python-using-anaconda/).

---
<a id="use"></a>
## ***Web page***

This scraper works only on this type of page :

<img src="data/img_doc/pagina_rev.png" alt="pagina reviews" style="height: 400px; width:1000px;"/>

You can find the above page by clicking where indicated by the red box :

<img src="data/img_doc/reviews.png" alt="home reviews" style="height: 400px; width:1000px;"/>


---
<a id="conf"></a>
## ***Configuring JSON file***
Here we can see how the Json file present itself:

<img src="data/img_doc/json_conf.png" alt="json file" style="height: 400px; width:1000px;"/>

You only need to change:
- "link": url
- "reviews_file": filename.pickle

Remember to always choose ***.pickle*** format.

---
<a id="start"></a>
## ***Run program***
From terminal:

    python scraper.py

Or from the start button of your preferred ***IDE***.


