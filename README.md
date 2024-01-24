# Transformers Tutorial
## Author: Brady Lamson

## Intent: 

This repository is intended to function as a user-friendly guide to the `transformers` library and how to utilize it for a deployable end-to-end web application. I will be fine tuning a BERT model on the downstream task of named-entity-recognition. 

This repository itself, though detailed, will only be one part of the tutorial. The bulk of the information will be hosted in a writeup on my website, [here]([https://bradylamson.com/](https://bradylamson.com/p/named-entity-recognition-a-transformers-tutorial/)). 

## Overview:

This project will do the following:

- Utilize a basic toy dataset built for named entity recognition (NER).
- Show how to build all the component pieces to make use of the `transformers` `trainer` object.
- Utilize the `trainer` object and the `optuna` library to perform hyperparameter tuning on the model.
- Perform basic evaluation of a model.
- Compress and store a functional model on `AWS S3`.
- Create a basic web application with `Flask` to take in strings of text to run predictions on.
- Containerize said web application with `Docker` with a custom setup to play nice with `AWS Sagemaker`
- Deploy the web application on `AWS Sagemaker`

## Note:

A lot of the AWS specific information will be found on my personal website. So if any information seems to be missing from this repository, your best bet will be to check there for updates or reach out to me for clarification. 
