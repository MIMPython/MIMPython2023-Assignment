"""
a) Tạo một class Rectangle (Hình chữ nhật) và thiết kế một số phương
thức phù hợp. Sau đó, tạo class Square (Hình vuông) kế thừa từ class
Rectangle.

b) Tạo class Rhombus (hình thoi) và thực hiện kế thừa một cách phù hợp

c) Tạo class Ellipse (hình elip) và class Circle (hình tròn). Thực hiện
kế thừa một cách phù hợp.
"""

class Rectangle():
    def __init__(self, length, width):
        """
        Tạo một hình chữ nhật từ chiều dài và chiều rộng
        (Chiều dài >= Chiều rộng).
        """
        self.length = length
        self.width = width
        if length < width:
            raise ValueError("Chiều dài không được nhỏ hơn chiều rộng.")
    
    @property
    def center(self):
        """
        Thiết lập thuộc tính center (tâm hình chữ nhật).
        """
        try:
            a = self._center
        except AttributeError:
            raise AttributeError(f"Tâm chưa được khởi tạo.")
        return tuple(self._center)
    
    @center.setter
    def center(self, coords):
        import numpy as np
        self._center = np.array(coords)
        return self._center
    
    @property
    def length_direction(self):
        """
        Thiết lập thuộc tính véc-tơ chỉ phương của chiều dài.
        """
        try:
            a = self._length_direction
        except AttributeError:
            raise AttributeError(f"Hướng của chiều dài chưa được khởi tạo.")
        return tuple(self._length_direction)
    
    @length_direction.setter
    def length_direction(self, vector):
        import numpy as np
        if vector == (0, 0):
            raise ValueError("Hướng của chiều dài phải khác véc-tơ (0, 0).")
        self._length_direction = np.array(vector)
        return self._length_direction

    @property
    def vertex_coords(self):
        """
        Thiết lập toạ độ các đỉnh của hình chữ nhật, khi đã biết toạ
        độ của tâm và hướng của chiều dài.
        """
        import numpy as np
        vector = self._length_direction
        vec_length = (vector[0]**2 + vector[1]**2)**0.5
        normalized_vec = vector / vec_length
        normalized_normal_vec = np.array([-normalized_vec[1], normalized_vec[0]])
        self.vertices = [
                [self.center + 
                 (i*self.width*0.5) * normalized_normal_vec +
                 (j*self.length*0.5) * normalized_vec
                for j in [-1, 1]] 
            for i in [-1, 1]
            ]
        return self.vertices

    def plot_rectangle(self):
        """
        Vẽ hình chữ nhật khi đã biết toạ độ các đỉnh.
        """
        from matplotlib import pyplot as plt
        a = self.vertex_coords
        plot_x_coords = [a[0][0][0], a[0][1][0], a[1][1][0], a[1][0][0], a[0][0][0]]
        plot_y_coords = [a[0][0][1], a[0][1][1], a[1][1][1], a[1][0][1], a[0][0][1]]
        
        fig, ax = plt.subplots()
        ax.plot(plot_x_coords, plot_y_coords)
        ax.plot(self.center[0], self.center[1], "o")
        ax.set(aspect = "equal")
        plt.show()

    
# A = Rectangle(3, 2.2)
# A.center = (1.2, 0.5)
# A.length_direction = (0.3, 0.4)
# A.plot_rectangle()

class Rhombus():
    def __init__(self, major_axis_length, minor_axis_length):
        """
        Tạo một hình thoi từ độ dài hai trục.
        """
        if major_axis_length < minor_axis_length:
            raise ValueError("Độ dài trục lớn không được nhỏ hơn độ dài trục nhỏ.")
        self.M_len = major_axis_length
        self.m_len = minor_axis_length
        self.length = ((self.M_len**2 + self.m_len**2) / 4)**0.5

    @property
    def center(self):
        """
        Thiết lập thuộc tính center (tâm hình thoi).
        """
        try:
            a = self._center
        except AttributeError:
            raise AttributeError(f"Tâm chưa được khởi tạo.")
        return tuple(self._center)
    
    @center.setter
    def center(self, coords):
        import numpy as np
        self._center = np.array(coords)
        return self._center

    @property
    def axis_direction(self):
        """
        Thiết lập thuộc tính véc-tơ chỉ phương của trục lớn.
        """
        try:
            a = self._axis_direction
        except AttributeError:
            raise AttributeError(f"Hướng của trục lớn chưa được khởi tạo.")
        return tuple(self._axis_direction)
    
    @axis_direction.setter
    def axis_direction(self, vector):
        import numpy as np
        if vector == (0, 0):
            raise ValueError("Hướng của trục lớn phải khác véc-tơ (0, 0).")
        self._axis_direction = np.array(vector)
        return self._axis_direction

    @property
    def rhombus_vertex_coords(self):
        """
        Thiết lập toạ độ các đỉnh của hình thoi, khi đã biết toạ
        độ của tâm và hướng của chiều dài.
        """
        import numpy as np
        vector = self.axis_direction
        vec_length = (vector[0]**2 + vector[1]**2)**0.5
        normalized_vec = vector / vec_length
        normalized_normal_vec = np.array([-normalized_vec[1], normalized_vec[0]])
        M_vertices = [
                [self.center + 
                 (i*self.M_len*0.5) * normalized_vec
                for i in [-1, 1]] 
            ]
        m_vertices = [
                [self.center + 
                 (i*self.m_len*0.5) * normalized_normal_vec
                for i in [-1, 1]]
            ]
        self.vertices  = M_vertices + m_vertices
        return self.vertices
    
    def plot_rhombus(self):
        """
        Vẽ hình thoi khi đã biết toạ độ các đỉnh.
        """
        from matplotlib import pyplot as plt
        a = self.rhombus_vertex_coords
        plot_x_coords = [a[0][0][0], a[1][0][0], a[0][1][0], a[1][1][0], a[0][0][0]]
        plot_y_coords = [a[0][0][1], a[1][0][1], a[0][1][1], a[1][1][1], a[0][0][1]]
        
        fig, ax = plt.subplots()
        ax.plot(plot_x_coords, plot_y_coords)
        ax.plot(self.center[0], self.center[1], "o")
        ax.set(aspect = "equal")
        plt.show()

# B = Rhombus(4, 3)
# B.center = (0, 0)
# B.axis_direction = (1, 0)
# B.plot_rhombus()

class Square(Rectangle, Rhombus):
    def __init__(self, side_length = 0, axis_length = 0):
        if side_length != 0:
            Rectangle.__init__(self, side_length, side_length)
        elif axis_length != 0:
            Rhombus.__init__(self, axis_length, axis_length)

# C = Square(axis_length = 3)
# C.center = (0, 0)
# C.axis_direction = (1, 1)
# print(C.length)
# print(C.plot_rhombus())

class Ellipse():
    def __init__(self, major_axis_length, minor_axis_length):
        """
        Tạo một hình elip từ độ dài hai trục.
        """
        if major_axis_length < minor_axis_length:
            raise ValueError("Độ dài trục lớn không được nhỏ hơn độ dài trục nhỏ.")
        self.M_len = major_axis_length
        self.m_len = minor_axis_length

    @property
    def center(self):
        """
        Thiết lập thuộc tính center (tâm hình elip).
        """
        try:
            a = self._center
        except AttributeError:
            raise AttributeError(f"Tâm chưa được khởi tạo.")
        return tuple(self._center)
    
    @center.setter
    def center(self, coords):
        import numpy as np
        self._center = np.array(coords)
        return self._center
    
    @property
    def axis_direction(self):
        """
        Thiết lập thuộc tính véc-tơ chỉ phương của trục lớn.
        """
        try:
            a = self._axis_direction
        except AttributeError:
            raise AttributeError(f"Hướng của trục lớn chưa được khởi tạo.")
        return tuple(self._axis_direction)
    
    @axis_direction.setter
    def axis_direction(self, vector):
        import numpy as np
        if vector == (0, 0):
            raise ValueError("Hướng của trục lớn phải khác véc-tơ (0, 0).")
        self._axis_direction = np.array(vector)
        return self._axis_direction
    
    def plot_ellipse(self):
        import matplotlib.pyplot as plt
        import numpy as np
        a = self.M_len / 2
        b = self.m_len / 2
        pi = np.pi
        if self.axis_direction[0] == 0:
            rot_angle = pi / 2
        else:
            rot_angle = np.arctan(self.axis_direction[1] / self.axis_direction[0])
        rot_mat = np.array(
            [[np.cos(rot_angle), np.sin(-rot_angle)],
             [np.sin(rot_angle), np.cos(rot_angle)],]
        )
        t = np.linspace(0, 2*pi, 100)
        ell = np.array([a * np.cos(t), b * np.sin(t)])
        M_axis_point = np.array([[-a, a], [0, 0]])
        m_axis_point = np.array([[0, 0], [b, -b]])

        rot_ell = np.zeros((2, ell.shape[1]))
        for i in range(ell.shape[1]):
            rot_ell[:,i] = np.dot(rot_mat, ell[:,i]) + self.center
        
        for i in range(2):
            M_axis_point[:,i] = np.dot(rot_mat, M_axis_point[:,i]) + self.center
            m_axis_point[:,i] = np.dot(rot_mat, m_axis_point[:,i]) + self.center

        fig, ax = plt.subplots()
        ax.plot(rot_ell[0,:], rot_ell[1,:])
        ax.plot(M_axis_point[0,:], M_axis_point[1,:], "--")
        ax.plot(m_axis_point[0,:], m_axis_point[1,:], "--")
        ax.plot(self.center[0], self.center[1], "o")
        ax.set(aspect = "equal")
        plt.show()

# E = Ellipse(4, 3)
# E.center = (1, 1)
# E.axis_direction = (1, 1)
# E.plot_ellipse()

class Circle(Ellipse):
    def __init__(self, radius):
        """
        Tạo một hình tròn từ bán kính.
        """
        super().__init__(2*radius, 2*radius)

# D = Circle(2)
# D.center = (0, 0)
# D.axis_direction = (1, 0)
# D.plot_ellipse()

