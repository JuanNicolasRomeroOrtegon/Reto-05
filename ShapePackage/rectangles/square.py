from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, vertices: list, edges: list) -> None:
        super().__init__(vertices, edges)
        self._side = edges[0].get_length()

    def get_side(self) -> float:
        return self._side

    def set_side(self, side: float) -> None:
        if side <= 0:
            raise ValueError("El lado debe ser positivo")
        self._side = side

    def compute_area(self) -> float:
        return self._side**2

    def compute_perimeter(self) -> float:
        return 4 * self._side

    def compute_angles(self) -> float:
        return 360
