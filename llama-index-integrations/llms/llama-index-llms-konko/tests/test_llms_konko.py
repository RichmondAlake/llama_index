from llama_index.core.llms.base import BaseLLM
from llama_index.llms.konko import Konko


def test_embedding_class():
    names_of_base_classes = [b.__name__ for b in Konko.__mro__]
    assert BaseLLM.__name__ in names_of_base_classes
