from tests.schemas.const import SCHEMA

HomePageSchema = {
    '$schema': SCHEMA,
    'type': 'object',
    'required': [
        'service',
        'version',
    ],
    'additionalProperties': False,
    'properties': {
        'service': {'type': 'string'},
        'version': {'type': 'string'},
        'environment': {'type': 'string'},
    },
}
