

from ceevee.dummy import DummyPredictor
from ceevee.features import FeaturesExtractor


__all__ = ['DummyPredictor', 'FeaturesExtractor']

MODELS = {
    'dummy': DummyPredictor,
    'features': FeaturesExtractor
}