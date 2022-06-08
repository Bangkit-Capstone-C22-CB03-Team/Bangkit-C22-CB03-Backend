# Bangkit-C22CB-Company-Based-Capstone

[![CodeFactor](https://www.codefactor.io/repository/github/dhupee/bangkit-c22cb-company-based-capstone/badge)](https://www.codefactor.io/repository/github/dhupee/bangkit-c22cb-company-based-capstone)

![Bangkit](https://lh3.googleusercontent.com/J2QI0L3vJwv63Sm3isI90ctxuxznz67dAtJQN2vu7wnUuwt9Wc-WI7VuIhwvr0yVrDPfc7kBN5usZz75nDW_k96pCfcZBxnfNzvVS0g=w600)

This is our repository for Company Based Capstone.

Our team Consist of 9 people.

- [Bangkit-C22CB-Company-Based-Capstone](#bangkit-c22cb-company-based-capstone)
  - [The Boys](#the-boys)
  - [What is this? (*coming soon*)](#what-is-this-coming-soon)
  - [Editing Architecture Chart](#editing-architecture-chart)
  - [Running Our Project in Local](#running-our-project-in-local)
    - [Using Conda (easier to build)](#using-conda-easier-to-build)
    - [Using PIP (not recommended, still experimental)](#using-pip-not-recommended-still-experimental)
  - [Our ML model result uploaded to Huggingface.co](#our-ml-model-result-uploaded-to-huggingfaceco)
  - [References](#references)

## The Boys

Name | Bangkit ID | Learning Path | Github Profile
:---|:---:|:---:|---:
Ananda Daffa Abdillah | M2008G0791 | Machine Learning | [Profile](https://github.com/Anandadaffa)
Daffa Haj Tsaqif| M2008G0792 | Machine Learning | [Profile](https://https://github.com/dhupee)
Mario Hagi | M2191F1819 | Machine Learning | [Profile](https://github.com/mariohagi)
Alheta Wahyu Matalarens |  A2110F1435 | Mobile Development | [Profile](https://github.com/ZenMachi)
Ary Bayu Nurwicaksono | A2183F1767 | Mobile Development
Hafit Abekrori | A7183F1768 | Mobile Development | [Profile](https://github.com/Haf0)
Muhammad Acla Alamsyah Nurdin Hamzah | C2307F2632 | Cloud Computing | [Profile](https://github.com/Aclaputra)
Aimar Anand | C2323J2836 | Cloud Computing | [Profile](https://github.com/imar6teen)
Ariel Peaceo Gunawan | C7005F0459 | Cloud Computing | [Profile](https://github.com/Kouci01)

## What is this? (*coming soon*)

TBA

## Editing Architecture Chart

Use [Draw.IO]([https://link](https://app.diagrams.net/)) to create our architecture chart, use this VScode Extension to edit our diagram inside the editor: [Draw.io Integration in VSCode](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)

## Running Our Project in Local

### Using Conda (easier to build)

if you are using conda, you can install our project using the following command:

```bash
conda create --name bangkit_capstone python=3.9
conda activate bangkit_capstone
pip install ipykernel
```

or this command if you are want to specify the path of the environment

```bash
conda create --prefix ./venv/ python=3.9
conda activate ./venv/
pip install ipykernel
```

### Using PIP (not recommended, still experimental)

It's advised for machine learning aspect to use virtual environment to working with this project, this is to prevent incompatibilities with other contributors.

If you are still activate Conda, you can deactivate it by typing `conda deactivate`.

in the repo's directory, run the following commands one by one:

```bash
python3 -m pip install --upgrade pip
python3 -m venv venv
source venv/bin/activate | source venv/Scripts/activate
pip install -r requirements.txt
```

## Our ML model result uploaded to Huggingface.co

Here's our working model result uploaded to Huggingface.co
[bert-uncased-finetuned-squad-indonesian](https://huggingface.co/Andaf/bert-uncased-finetuned-squad-indonesian?context=makanan+favorit+dita+adalah+spaghetti&question=apa+makanan+favorit+dita)

## References

- [TensorFlow and Transformers (Medium)](https://towardsdatascience.com/tensorflow-and-transformers-df6fceaf57cc)
- [AjulorC's question answering bot](https://huggingface.co/spaces/AjulorC/question_answering_bot_deployed_with_Gradio)
- [Smaller, faster, cheaper, lighter: Introducing DistilBERT, a distilled version of BERT](https://medium.com/huggingface/distilbert-8cf3380435b5)
