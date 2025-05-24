from .point import Point
from .line import Line 

class Shape:
    def __init__(self, is_regular: bool, vertices: list["Point"], 
                 edges: list["Line"], inner_angles: list[float]) -> None:
        self._is_regular = is_regular         
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles
        
    def get_is_regular(self) -> bool:
        return self._is_regular
    
    def set_is_regular(self, is_regular: bool) -> None:
        self._is_regular = is_regular
        
    def get_vertices(self):
        return self._vertices
    
    def set_vertices(self, vertices: list["Point"]):
        self._vertices = vertices

    def get_edges(self):
        return self._edges
    
    def set_edges(self, edges: list["Line"]):
        self._edges = edges

    def get_inner_angles(self):
        return self._inner_angles
    
    def set_inner_angles(self, inner_angles: list[float]):
        self._inner_angles = inner_angles
    

    def compute_area(self): 
        pass #El área se calcula según la figura 

    def compute_perimeter(self):
        perimeter = 0
        for edge in self._edges:
            perimeter += edge.get_length()
        return perimeter

    def compute_inner_angles(self):
        total_angles = 0
        for angle in self._inner_angles: 
            total_angles += angle
        return total_angles
