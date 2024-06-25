import spacy_streamlit

models = ["en_ner_bc5cdr_md", "en_core_sci_md"]
default_text = """
Spinal and bulbar muscular atrophy (SBMA) is an inherited motor
neuron disease caused by the expansion
of a polyglutamine tract within the androgen receptor (AR).
"""
visualizers = ["ner", "textcat"]
spacy_streamlit.visualize(models, default_text, visualizers)
