import json
from virgene.plugin_feature import PluginFeature
from virgene.snippet_feature import SnippetFeature
from virgene.builtin_feature import BuiltinFeature


class FeatureDecoder:

    @staticmethod
    def decode(feature_json):
        decoders = {
            "Plugin": PluginFeature.from_feature_json,
            "Snippet": SnippetFeature.from_feature_json,
            "Builtin": BuiltinFeature.from_feature_json,
        }

        decoder = decoders[feature_json["feature_type"]]
        return decoder(feature_json)

    @staticmethod
    def decode_from_path(feature_path):
        with open(feature_path) as feature_file:
            feature_json = json.load(feature_file)
        return FeatureDecoder.decode(feature_json)
