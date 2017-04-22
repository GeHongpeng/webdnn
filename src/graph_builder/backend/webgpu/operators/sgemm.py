from typing import Dict

from graph_builder.graph.operator import Operator
from graph_builder.graph.operators.attributes.have_weights import HaveWeights
from graph_builder.graph.operators.attributes.post_axiswise import PostAxiswise
from graph_builder.graph.operators.attributes.post_elementwise import PostElementwise
from graph_builder.graph.variable import Variable


class Sgemm(Operator):
    attributes = {PostElementwise,
                  PostAxiswise,
                  HaveWeights}

    def __init__(self, name: str, parameters: Dict[str, object]):
        assert "M" in parameters
        assert "N" in parameters
        assert "K" in parameters
        assert "out_shape" in parameters
        assert "out_order" in parameters

        super().__init__(name, parameters)

    def __call__(self, x: Variable, w: Variable):
        self.append_input("x", x)
        self.append_input("w", w)

        y = Variable(
            self.parameters["out_shape"],
            self.parameters["out_order"]
        )
        self.append_output("y", y)

        return y,

    @property
    def M(self) -> int:
        return int(self.parameters["M"])

    @property
    def N(self) -> int:
        return int(self.parameters["N"])

    @property
    def K(self) -> int:
        return int(self.parameters["K"])
