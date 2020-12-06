import stanfordnlp

def tokeniza(texto_fichero):

    MODELS_DIR = '.'
    stanfordnlp.download('es', MODELS_DIR)  # Download the Spanish models
    nlp = stanfordnlp.Pipeline(processors='tokenize,pos', models_dir=MODELS_DIR, treebank='es_ancora', use_gpu=False,
                               pos_batch_size=3000)  # Build the pipeline, specify part-of-speech processor's batch size
    doc = nlp(texto_fichero)  # Run the pipeline on input text
    for frase in doc.sentences:
        frase.print_tokens()  # Look at the result

    # Read the corpus into a list,
    # each entry in the list is one sentence.
