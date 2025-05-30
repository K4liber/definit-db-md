from definit_db.data.field.mathematics.definitions.graph.node import NODE
from definit_db.definition.definition import Definition
from definit_db.definition.definition_key import DefinitionKey
from definit_db.definition.field import Field


class _Leaf(Definition):
    def _get_content(self) -> str:
        return f"A {NODE.key.get_reference(phrase='node')} in a tree that does not have any children (descendants)."


LEAF = _Leaf(
    key=DefinitionKey(
        name="leaf",
        field=Field.MATHEMATICS,
    )
)
