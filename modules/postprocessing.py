from typing import List


def make_pipe_play_nice_with_jsonify(predictions: List[dict]) -> List[dict]:
	"""
	Fixes the dumb issue where pipe outputs a float32 which isn't json serializable.
	"""

	for entity_prediction in predictions:
		entity_prediction.update({"score": float(entity_prediction["score"])})

	return predictions
