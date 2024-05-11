# medical-nlp

NLP for scientific and medical research.

## Installation 

Make sure you have the latest version of pip install: `python -m pip install --upgrade pip `

I highly recommend building a new virtual environment. You can use conda for example. medical-nlp requires Python >= 3.12

`conda create -n <ENVNAME> python==3.12`

activate your virtual environment if you created it.

`conda activate <ENVNAME>`

Build the module. This will allow to import methods and classes from the package seamlessly.

run 
`pip install --upgrade build`
followed by 
`python -m build`

install all dependencies with 
`pip install .`

**Install the NLP models desired** 

Depending on the size of your machine and your specs, you might want to install different versions of the Scispacy and Spacy models. 

To run the notebooks and examples a model is required. For example you can install the "medium" medical model via:

> `conda activate <ENVNAME>`

> `pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_md-0.5.4.tar.gz`

More information about the models in the following [link](https://github.com/allenai/scispacy)

**NOTE**: Some of the features like vectors are only available in medium and large models in Spacy. Hence, it is suggested to install at least a medium size model to be able to run all the methods and functions of this tutorial.
