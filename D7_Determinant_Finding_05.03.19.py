

#Matrix Determinant finding

my_Matrix_1 =[[1 ,2] ,[3 ,4]]
my_Matrix_2 =[[1 ,5 ,3] ,[4 ,7 ,6] ,[7 ,2 ,9]]
my_Matrix_4 =[[13 ,2 ,3 ,4] ,[5 ,6 ,7 ,8] ,[92 ,10 ,31 ,42] ,[13 ,134 ,15 ,16]]
print(my_Matrix_1)
print(my_Matrix_2)
print(my_Matrix_4)



def MyMatrixDeterminant_2(m_1):

    s1 =(m_1[0][0] ) *(m_1[1][1])
    s2 =(m_1[0][1] ) *(m_1[1][0])
    s3 =s1 -s2
    return s3

print(MyMatrixDeterminant_2(my_Matrix_1))


def MyMatrixDeterminantDelete(m_1 ,m ,n):

    result =[]
    size_1 =len(m_1)
    size_2 =len(m_1[0])

    for i in range(size_1):
        if(i==m):
            continue
        row_1 =[]
        for j in range(size_2):
            if(j==n):
                continue
            row_1.append(m_1[i][j])
        result.append(row_1)
    return result

print(MyMatrixDeterminantDelete(my_Matrix_2,0,0))


def MyMatrixDeterminant_3(m_1):

    a1 =m_1[0][0]
    a2 =MyMatrixDeterminantDelete(m_1,0,0)
    a3 =MyMatrixDeterminant_2(a2)
    a4 =a1 *a3

    b1 =m_1[0][1]
    b2 =MyMatrixDeterminantDelete(m_1,0,1)
    b3 =MyMatrixDeterminant_2(b2)
    b4 =b1*b3

    c1 =m_1[0][2]
    c2 =MyMatrixDeterminantDelete(m_1,0,2)
    c3 =MyMatrixDeterminant_2(c2)
    c4 =c1 *c3

    return a4-b4+c4

print(MyMatrixDeterminant_3(my_Matrix_2))


def MyMatrisDeterminant_4(m_1):

    a1 =m_1[0][0]
    a2 =MyMatrixDeterminantDelete(m_1 ,0 ,0)
    a3 =MyMatrixDeterminant_3(a2)
    a4 =a1 *a3

    b1 =m_1[0][1]
    b2 =MyMatrixDeterminantDelete(m_1,0,1)
    b3 =MyMatrixDeterminant_3(b2)
    b4 =b1 *b3

    c1 =m_1[0][2]
    c2 =MyMatrixDeterminantDelete(m_1,0,2)
    c3 =MyMatrixDeterminant_3(c2)
    c4 =c1 *c3

    d1 =m_1[0][3]
    d2 =MyMatrixDeterminantDelete(m_1,0,3)
    d3 =MyMatrixDeterminant_3(d2)
    d4 =d1 *d3
    return a4-b4+c4-d4

print(MyMatrisDeterminant_4(my_Matrix_4))
