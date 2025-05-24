from ..basicgeometry.shape import Shape

class Triangle(Shape): 
    def __init__(self, is_regular: bool, vertices: list, 
                 edges: list, inner_angles: list[float]) -> None:
        super().__init__(is_regular, vertices, edges, inner_angles)    
        self._side1 = edges[0].get_length()
        self._side2 = edges[1].get_length()
        self._side3 = edges[2].get_length()
        self._angle1 = inner_angles[0]
        self._angle2 = inner_angles[1]
        self._angle3 = inner_angles[2]
        
    def get_side1(self) -> float:
        return self._side1
    
    def set_side1(self, _side1: float) -> None:
        if _side1 <= 0:
            raise ValueError("El tamaño del lado debe ser positivo")
        self._side1 = _side1

    def get_side2(self) -> float:
        return self._side2
    
    def set_side2(self, _side2: float) -> None:
        if _side2 <= 0:
            raise ValueError("El tamaño del lado debe ser positivo")
        self._side2 = _side2
        
    def get_side3(self) -> float:
        return self._side3
    
    def set_side3(self, _side3: float) -> None:
        if _side3 <= 0:
            raise ValueError("El tamaño del lado debe ser positivo")
        self._side3 = _side3
    
    def get_angle1(self) -> float:
        return self._angle1

    def set_angle1(self, _angle1: float) -> None:
        if _angle1 <= 0:
            raise ValueError("El tamaño del ángulo debe ser positivo")
        self._angle1 = _angle1
        
    def get_angle2(self) -> float:
        return self._angle2

    def set_angle2(self, _angle2: float) -> None:
        if _angle2 <= 0:
            raise ValueError("El tamaño del ángulo debe ser positivo")
        self._angle2 = _angle2
    
    def get_angle3(self) -> float:
        return self._angle3
    
    def set_angle3(self, _angle3: float) -> None:
        if _angle3 <= 0:
            raise ValueError("El tamaño del ángulo debe ser positivo")
        self._angle3 = _angle3

    #Usamos la fórmula de Herón para calcular el área, ya que es aplicable a 
    #cualquier triángulo
    def compute_area(self) -> float:
        #sp es el semiperímetro, lo coloqué así para que no ocupase tanto espacio
        sp = (self._side1 + self._side2 + self._side3) / 2
        return (sp * (sp - self._side1) * (sp - self._side2) * 
                (sp - self._side3)) ** 0.5

    def compute_perimeter(self) -> float: 
        return self._side1 + self._side2 + self._side3
    
    def compute_angles(self) -> float:
        return self._angle1 + self._angle2 + self._angle3 


    def is_acute(self) -> bool:
        return self._angle1 < 90 and self._angle2 < 90 and self._angle3 < 90
    
    def is_obtuse(self) -> bool:
        """Un ángulo > 90°"""
        return self._angle1 > 90 or self._angle2 > 90 or self._angle3 > 90
    
    def is_right(self) -> bool:
        return self._angle1 == 90 or self._angle2 == 90 or self._angle3 == 90
    
    #Decimos que tipo de triángulo es según sus ángulos
    def angles_type(self) -> str:
        if self.is_right():
            return "Triangle Rectangle"
        elif self.is_obtuse():
            return "Triangle Obtuse"
        else:
            return "Triangle Acute"
        