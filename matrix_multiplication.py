class matrix_product:
    def find_order(self):
        self.m = int(input(f"enter the m of {self.name} = ")) 
        self.n = int(input(f"enter the n of {self.name} = "))
    def order_check(self):
        if matrix1.n != matrix2.m:
            return True
        else:
            return False
    def input_elements(self):
        self.elements = []
        for i in range(0,self.m):
            p = []
            for j in range(0,self.n):
                r = int(input(f"enter the [{i+1}][{j+1}] of {self.name} = "))
                p.append(r)
            self.elements.append(p)
    def calc_product(self):
        r = []
        for i in range(0,matrix1.m):
            p =[]
            for j in range(0,matrix2.n):
                d = 0
                for k in range(0,matrix1.n):
                    d = d + matrix1.elements[i][k] * matrix2.elements[k][j]
                p.append(d)
            r.append(p)
        return r            
matrix1 = matrix_product()
matrix2 = matrix_product()
order = matrix_product()
product = matrix_product()
matrix1.name = "First Matrix"
matrix2.name = "Second Matrix"
matrix1.find_order()
matrix2.find_order()
if order.order_check():
    print("orders mismatch; TRY AGAIN")
else:
    print("orders are compatible")
    matrix1.input_elements()
    matrix2.input_elements()
    x = product.calc_product()
    print(f"the product of two matrices is =\n{x}")
    