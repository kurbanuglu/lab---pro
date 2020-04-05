
#Matrix Islemleri




def MyMatrixAddition(m_1,m_2):
    result=[]

    for row in range(len(m_1)):
        result.append([])
        for column in range(len(m_1[0])):
            result[row].append(m_1[row][column]+m_2[row][column])
    return result

matrix_1=[[7,2,4],[9,1,7]]
matrix_2=[[5,0,4],[6,7,2]]
toplam=MyMatrixAddition(matrix_1,matrix_2)
print("toplam: ",toplam)


def MyMatrixSubstraction(m_1,m_2):
    result=[]

    for row in range(len(m_1)):
        result.append([])
        for column in range(len(m_1[0])):
            result[row].append(m_1[row][column]-m_2[row][column])
    return result

cikarma=MyMatrixSubstraction(matrix_1,matrix_2)
print("cikarma: ",cikarma)


def MyMatrixScalarProduct(alpha,m_1):
    result=[]

    for row in range(len(m_1)):
        result.append([])
        for column in range(len(m_1[0])):
            result[row].append(m_1[row][column]*alpha)
    return result

alpha=10
alphacarpim=MyMatrixScalarProduct(alpha,matrix_1)
print("alpha a ile carpim: ",alphacarpim)


def f_1(mat_1,i):
    return mat_1[i]

def f_2(mat_1,i):
    my_j_th_cool=[]
    for row in mat_1:
        for indis in range(len(row)):
            if(indis==i):
                my_j_th_cool.append(row[indis])
    return my_j_th_cool


def MyVectorsInnerProduct(v,w):
    size=len(v)
    my_result=[]

    for i in range(size):
        my_result.append(0)

    for i in range(size):
        my_result[i]=v[i]*w[i]
    t=0
    for i in range(size):
        t=t+my_result[i]
    return t


def MyMatrixMultiply(m_1,m_2):
    result=[]

    for row in range(len(m_1)):
        result.append([])
        for column in range(len(m_2[0])):
            a=f_1(m_1,row)
            b=f_2(m_2,column)
            c=MyVectorsInnerProduct(a,b)
            result[row].append(c)
    return result


mat_1=[[1,0],[2,4]]
mat_2=[[5,6,4],[8,9,10]]

r=MyMatrixMultiply(mat_1,mat_2)
print("carpim: ",r)
