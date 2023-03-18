
import sys
import numpy as np
import matplotlib.pyplot as plt

from fealpy.mesh import MeshFactory
from fealpy.functionspace import LagrangeFiniteElementSpace



#a = int(sys.argv[1])#在cmd中运行  命令python3 homework2.py int    注需要几维空间 int取几
mf = MeshFactory
box = [0, 1, 0, 1]  #求解区间
mesh = mf.boxmesh2d(box, nx=10, ny=10, meshtype='tri')
# 打印网格信息
NN = mesh.number_of_nodes()#节点个数
NE = mesh.number_of_edges()#边个数
NC = mesh.number_of_cells()#单元个数
print("节点 边 单元", NN, NE, NC)



#创造拉格朗日有限元空间
# space = LagrangeFiniteElementSpace(mesh, p=a)#空间次数
space = LagrangeFiniteElementSpace(mesh, p=2)#空间次数
ldof = space.number_of_local_dofs()  #局部自由度
gdof = space.number_of_global_dofs() #体自由度


bc = np.array([[1/3, 1/3, 1/3]], dtype=float)#重心坐标
bs = mesh.bc_to_point(bc)#NQ NC
phi = space.basis(bc) #计算重心坐标
gphi = space.grad_basis(bc) #重心坐标的梯度

# print('ldof', ldof)
# print('gdof', gdof)
# print('bc', bc.shape)
# print('phi', phi.shape)
# print('gphi', gphi.shape)

ipoints = space.interpolation_points()#自由度对应的插值点
cell2dof = space.cell_to_dof()
print('cell2dof:')
# for i,cal in enumerate(cell2dof)
#     print(i, ":", val)#打印每个单元的自由度信息


multiIndex = space.dof.multiIndex
# print(multiIndex) #打印基函数信息



fig = plt.figure()  #fig是个画布
axes = fig.gca()    #画坐标
mesh.add_plot(axes)
mesh.add_plot(axes)
mesh.find_node(axes, showindex=Ture)
mesh.find_cell(axes, showindex=Ture)



plt.show()













