from ..basicgeometry.shape import Shape   

class Rectangle(Shape):
    def __init__(self, vertices: list, edges: list) -> None:
        angles = [90.0, 90.0, 90.0, 90.0]
        super().__init__(is_regular=False, vertices=vertices, edges=edges, inner_angles=angles)
        self._width = edges[0].get_length()
        self._height = edges[1].get_length()
            
    def get_width(self) -> float:
        return self._width
    
    def set_width(self, width: float) -> None:
        if width <= 0:
            raise ValueError("El ancho debe ser positivo")
        self._width = width
    
    def get_height(self) -> float:
        return self._height
    
    def set_height(self, height: float) -> None:
        if height <= 0:
            raise ValueError("La altura debe ser positiva")
        self._height = height
    
    def compute_area(self):
        return self._width * self._height

    def compute_perimeter(self):
        return 2 * (self._width + self._height)
    
    def compute_angles(self):
        return 360
    
    def diagonal_length(self) -> float:
        return (self._width**2 + self._height**2) **0.5
    