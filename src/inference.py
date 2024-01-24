from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline, Pipeline
from loguru import logger
from modules.postprocessing import make_pipe_play_nice_with_jsonify


def load_model(model_dir: str) -> Pipeline:
    """
    Loads the model and tokenizer from directory, moves them to a pipeline object
    """

    logger.info(f"Model dir: {model_dir}")
    logger.info("Loading tokenizer")
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    logger.success("Tokenizer loaded")

    logger.info("Loading model")
    model = AutoModelForTokenClassification.from_pretrained(model_dir)
    logger.success("Model loaded")

    logger.info("Creating pipeline")
    pipe = pipeline(
        task="token-classification", model=model, tokenizer=tokenizer, aggregation_strategy="average"
    )
    logger.success("Pipeline created")

    return pipe


def predict(data: list, pipe: Pipeline) -> list:

    pipe_output = pipe(data)
    predictions = [make_pipe_play_nice_with_jsonify(text_prediction) for text_prediction in pipe_output]

    return predictions