# medical-nlp

NLP for scientific and medical research. This use case guides you through some of the basics on using [SciSpacy](https://allenai.github.io/scispacy/) and building a medical-based clustering algorithm from text embeddings. 

The data is an extract from the [MT Samples](https://mtsamples.com/) dataset, which consists of several medical transcriptions from different consultations. 

The Notebooks are under the [analysis](/analysis/) folder. 


## Installation 

**NOTE**: Using a Bash terminal is recommended for the set up. 

It is assumed Python and Conda have been installed.


SciSpacy requires python==3.11 

Make sure you have the latest version of pip install: `python -m pip install --upgrade pip`

I highly recommend building a new virtual environment. You can use conda for example. medical-nlp requires Python >= 3.12

`conda create -n <ENVNAME> python==3.11`

activate your virtual environment if you created it.

`conda activate <ENVNAME>`

Build the module. This will allow to import methods and classes from the package seamlessly.

**NOTE**: Scispacy can give errors when installing in MacOS M1, M2 or M3 machines. In that case, first execute:
`conda install nmslib`

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

or the small one with: 
`pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_sm-0.5.4.tar.gz`

More information about the models in the following [link](https://github.com/allenai/scispacy)

**NOTE**: Some of the features like vectors are only available in medium and large models in Spacy. Hence, it is suggested to install at least a medium size model to be able to run all the methods and functions of this tutorial.


The dependencies are highlighted in the `setup.py` file under `requires` and can be manually installed as well.

## License 

Protected under MIT license.