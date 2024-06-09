# medical-nlp

NLP for scientific and medical research. This use case guides you through some of the basics on using [SciSpacy](https://allenai.github.io/scispacy/) and building a medical-based clustering algorithm from text embeddings. 

## Exercise and use case.

We have been tasked to explore the [MT Samples](https://mtsamples.com/) data set, which consists of several medical transcriptions from different consultations. There, we can see that they have manually annotated the consultation under `medical_specialty`, but this categories are very broad. Using Machine Learning, we aim to "drill-down" on these to provide more accurate and fine-grained granularity in the categorization. 

### How to start
The Notebooks are under the [analysis](/analysis/) folder. It's recommended to run the [scispacy_basics](./analysis/scispacy_basics.ipynb) notebook first, and then continue with [medical_text_clustering](./analysis/medical_text_clustering.ipynb)

---


## Installation 

**NOTE**: Using a Bash terminal is recommended for the set up. 

It is assumed Python and Conda have been installed. Also worth noting that SciSpacy requires python==3.11 to work in MacOS M1, M2 and M3 machines. 

Make sure you have the latest version of pip install: `python -m pip install --upgrade pip`

I highly recommend building a new virtual environment. You can use conda for example: 

`conda create -n <ENVNAME> python==3.11`

activate your virtual environment after you created it.

`conda activate <ENVNAME>`

Build the module. This will allow to import methods and classes from the package seamlessly.

**NOTE**: Scispacy can give errors when installing in MacOS M1, M2 or M3 machines. In that case, first execute:
`conda install nmslib`. In other operating systems this might not be required.

### Build the module

First, install the build package. This will allow you to build the Python Module and install its dependencies. 

`python -m pip install build`

or

`pip install --upgrade build`

then, Build the `medical-nlp` module using: 

`python -m build`

Finally, install all dependencies that are in the `setup.py` file with 
`pip install .`

**Install the NLP models desired** 

Depending on the size of your machine and your specs, you might want to install different versions of the Scispacy and Spacy models. 

To run the notebooks and examples a model is required. For example you can install the "medium" medical model via:

> `conda activate <ENVNAME>`

> `pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_md-0.5.4.tar.gz`

or the small one with:

> `pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_sm-0.5.4.tar.gz`

More information about the models in the following [link - SciSpacy](https://github.com/allenai/scispacy)

**NOTE**: Some of the features like vectors are only available in medium and large models in Spacy. Hence, it is suggested to install at least a medium size model to be able to run all the methods and functions of this tutorial.


The dependencies are highlighted in the `setup.py` file under `requires` and can be manually installed as well.

## License 

Protected under MIT license.
