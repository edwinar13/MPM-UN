import math
import pydantic 

class ModelPolygon(pydantic.BaseModel):
    points: list[tuple[tuple[float, float], tuple[float, float]]]
    mesh_size: float | None = None

class MeshGenerator ():   
    def __init__(self):
        self.mesh = {}
        self.polygon = {}
        self.mesh_size = None
        self.mesh_type = None
        
    def generate_mesh_quadrilateral(self):
        
        polygon, mesh_size = self.polygon["points"], self.polygon["mesh_size"]
        # Extract edges of the polygon
        edge_A = polygon[0]
        edge_B = polygon[1]
        edge_AA = polygon[2]
        edge_BB = polygon[3]
        

        # Calculate maximum distances for mesh division
        dist_A = self.calculate_distance(edge_A)
        dist_B = self.calculate_distance(edge_B)
        dist_AA = self.calculate_distance(edge_AA)
        dist_BB = self.calculate_distance(edge_BB)

        # Determine number of divisions for each edge
        if dist_A >= dist_AA:
            div_a = round(dist_A / mesh_size)
        else:
            div_a = round(dist_AA / mesh_size)
            
        if dist_B >= dist_BB:
            div_b = round(dist_B / mesh_size)
        else:
            div_b = round(dist_BB / mesh_size)
        
  

        # Divide edges into segments
        seg_A = self.divide_line(edge_A, div_a)
        seg_B = self.divide_line(edge_B, div_b)
        seg_AA = self.divide_line(edge_AA, div_a)
        seg_BB = self.divide_line(edge_BB, div_b)
        
        # Reverse segments for proper iteration
        seg_AA.reverse()
        seg_BB.reverse()
        
        # Generate list of points
        points = []

        for i in range(0, len(seg_B)):
            seg_A_i = self.divide_line([seg_BB[i], seg_B[i]], div_a)            
            for point in seg_A_i:
                points.append(point)
                

        # Generate quadrilaterals
        quadrilaterals = []
        na = div_a
        nb = div_b
        for b in range(0, nb):
            row_sum = (na + 1) * b
            for a in range(0, na):
                v1 = a + row_sum
                v2 = a + 1 + row_sum
                v3 = a + 1 + row_sum + (na + 1)
                v4 = a + row_sum + (na + 1)
                quadrilaterals.append([v1, v2, v3, v4])

        # Calculate total number of elements
        n_elements = len(quadrilaterals)
        return points, quadrilaterals, n_elements

    def divide_line(self, line, parts):
        p1, p2 = line
        x1, y1 = p1
        x2, y2 = p2
        
        # Calculate segment distances
        dx = (x2 - x1) / parts
        dy = (y2 - y1) / parts
        
        # Calculate segment coordinates
        segments = []
        for i in range(parts + 1):
            x = x1 + dx * i
            y = y1 + dy * i
            segments.append([x, y])
        
        return segments

    def calculate_distance(self, line):
        p1, p2 = line
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
    def generate_mesh_triangular():
        # Generate mesh
        # ...
        mesh = {}
        return mesh
    
    def add_rectangle(
        self,
        xmin: float,
        xmax: float,
        ymin: float,
        ymax: float,
        mesh_size: float | None = None
    ):
        polygon = [
            ((xmin,ymin),(xmax,ymin)),
            ((xmax,ymin),(xmax,ymax)),
            ((xmax,ymax),(xmin,ymax)),
            ((xmin,ymax),(xmin,ymin))
        ]        
        return self.add_polygon(
            polygon= ModelPolygon(points=polygon, mesh_size=mesh_size)
        )
    
    def add_polygon(
        self,
        polygon: ModelPolygon
    ):
        points = polygon.points
        mesh_size = polygon.mesh_size        
        if mesh_size is None:
            d_max = 0
            for i in range(len(points)):
                d = math.sqrt((points[i][0][0]-points[i][0][1])**2 + (points[i][1][0]-points[i][1][1])**2)
                if d > d_max:
                    d_max = d                        
            mesh_size = d_max/10
        self.polygon = {
            "points": points,
            "mesh_size": mesh_size
        }
        return self.polygon
    

'''
# test add_rectangle
mg = MeshGenerator()
print(mg.add_rectangle(0, 1, 0, 1, 0.1))
print(mg.add_rectangle(0, 1, 0, 1))
print(mg.add_rectangle(0, 1, 0, 1, 0.5))

# test add_polygon
mg = MeshGenerator()
print(mg.add_polygon(polygon=ModelPolygon(points=[((0, 0), (1, 0)),
                                                  ((1, 0), (1, 1)),
                                                  ((1, 1), (0, 1)),
                                                  ((0, 1), (0, 0))], mesh_size=0.03)))
#Este da error ok
print(mg.add_polygon(polygon=ModelPolygon(points=[(0, 0), (1, 0), (1, 1), (0, 1)])))


'''