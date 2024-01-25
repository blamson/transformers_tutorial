import jsonschema
from loguru import logger


def validate_request(body: dict) -> bool:

	schema = {
		"type": "object",
		"properties": {
			"strings": {
				"type": "array",
				"items": {
					"type": "string"
				}
			}
		},
		"required": ["strings"],
		"additionalProperties": False
	}

	logger.info("Validating Request")
	try:
		jsonschema.validate(instance=body, schema=schema)
		logger.success("Validation Successful")
		return True
	except jsonschema.exceptions.ValidationError:
		logger.error("Body failed schema validation.")
		return False
