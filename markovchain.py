import numpy as np
from numpy.linalg import matrix_power
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/2')
def form2():
    return render_template('2.html')

@app.route('/calc2', methods=['GET'])
def calc2():
    language = request.args.get('row1')
    print(language)
    mat1 = [float(val) for val in request.args.get('row1').split(',')]
    mat2 = [float(val) for val in request.args.get('row2').split(',')]
    period = request.args.get('period')




    print(mat1)    
    print(mat2)



    #for value in range(matrix_size):
    #    print(mat1[value])
    # Create a 2D array, matrix equivalent of the imaginary unit
    arr = np.array([mat1, mat2])
    # Display the array
    print("Our Array...\n",arr)
    # Check the Dimensions
    print("\nDimensions of our Array...\n",arr.ndim)
    # Get the Datatype
    print("\nDatatype of our Array object...\n",arr.dtype)
    # Get the Shape
    print("\nShape of our Array object...\n",arr.shape)
    result_after_two_steps = np.linalg.matrix_power(arr, int(period))
    rows0 = result_after_two_steps[0]
    rows1 = result_after_two_steps[1]
    
    print(result_after_two_steps)
    return render_template('res2.html', rows0=rows0, rows1=rows1)





@app.route('/3')
def form3():
    return render_template('3.html')

@app.route('/calc3', methods=['GET'])
def calc3():
    language = request.args.get('row1')
    print(language)
    mat1 = [float(val) for val in request.args.get('row1').split(',')]
    mat2 = [float(val) for val in request.args.get('row2').split(',')]
    mat3 = [float(val) for val in request.args.get('row3').split(',')]
    period = request.args.get('period')



    print(mat1)    
    print(mat2)
    print(mat3)



    #for value in range(matrix_size):
    #    print(mat1[value])
    # Create a 2D array, matrix equivalent of the imaginary unit
    arr = np.array([mat1, mat2, mat3])
    result_after_two_steps = np.linalg.matrix_power(arr, int(period))
    rows0 = result_after_two_steps[0]
    rows1 = result_after_two_steps[1]
    rows2 = result_after_two_steps[2]
   
    # Display the array
    print("Our Array...\n",arr)
    # Check the Dimensions
    print("\nDimensions of our Array...\n",arr.ndim)
    # Get the Datatype
    print("\nDatatype of our Array object...\n",arr.dtype)
    # Get the Shape
    print("\nShape of our Array object...\n",arr.shape)
    return render_template('res3.html', rows0=rows0, rows1=rows1, rows2=rows2)



@app.route('/4')
def form4():
    return render_template('4.html')

@app.route('/calc4', methods=['GET'])
def calc4():
    language = request.args.get('row1')
    print(language)
    mat1 = [float(val) for val in request.args.get('row1').split(',')]
    mat2 = [float(val) for val in request.args.get('row2').split(',')]
    mat3 = [float(val) for val in request.args.get('row3').split(',')]
    mat4 = [float(val) for val in request.args.get('row4').split(',')]
    period = request.args.get('period')



    print(mat1)    
    print(mat2)
    print(mat3)
    print(mat4)



    #for value in range(matrix_size):
    #    print(mat1[value])
    # Create a 2D array, matrix equivalent of the imaginary unit
    arr = np.array([mat1, mat2, mat3, mat4])
    
    result_after_two_steps = np.linalg.matrix_power(arr, int(period))
    rows0 = result_after_two_steps[0]
    rows1 = result_after_two_steps[1]
    rows2 = result_after_two_steps[2]
    rows3 = result_after_two_steps[3]
    
    # Display the array
    print("Our Array...\n",arr)
    # Check the Dimensions
    print("\nDimensions of our Array...\n",arr.ndim)
    # Get the Datatype
    print("\nDatatype of our Array object...\n",arr.dtype)
    # Get the Shape
    print("\nShape of our Array object...\n",arr.shape)
    return render_template('res4.html', rows0=rows0, rows1=rows1, rows2=rows2, rows3=rows3)



@app.route('/5')
def form5():
    return render_template('5.html')

@app.route('/calc5', methods=['GET'])
def calc5():
    language = request.args.get('row1')
    print(language)
    mat1 = [float(val) for val in request.args.get('row1').split(',')]
    mat2 = [float(val) for val in request.args.get('row2').split(',')]
    mat3 = [float(val) for val in request.args.get('row3').split(',')]
    mat4 = [float(val) for val in request.args.get('row4').split(',')]
    mat5 = [float(val) for val in request.args.get('row5').split(',')]
    period = request.args.get('period')



    print(mat1)    
    print(mat2)
    print(mat3)
    print(mat4)
    print(mat5)



    #for value in range(matrix_size):
    #    print(mat1[value])
    # Create a 2D array, matrix equivalent of the imaginary unit
    arr = np.array([mat1, mat2, mat3, mat4, mat5])
    result_after_two_steps = np.linalg.matrix_power(arr, int(period))
    rows0 = result_after_two_steps[0]
    rows1 = result_after_two_steps[1]
    rows2 = result_after_two_steps[2]
    rows3 = result_after_two_steps[3]
    rows4 = result_after_two_steps[4]
 
    # Display the array
    print("Our Array...\n",arr)
    # Check the Dimensions
    print("\nDimensions of our Array...\n",arr.ndim)
    # Get the Datatype
    print("\nDatatype of our Array object...\n",arr.dtype)
    # Get the Shape
    print("\nShape of our Array object...\n",arr.shape)
    return render_template('res5.html', rows0=rows0, rows1=rows1, rows2=rows2, rows3=rows3, rows4=rows4)   




@app.route('/6')
def form6():
    return render_template('6.html')

@app.route('/calc6', methods=['GET'])
def calc6():
    language = request.args.get('row1')
    print(language)
    mat1 = [float(val) for val in request.args.get('row1').split(',')]
    mat2 = [float(val) for val in request.args.get('row2').split(',')]
    mat3 = [float(val) for val in request.args.get('row3').split(',')]
    mat4 = [float(val) for val in request.args.get('row4').split(',')]
    mat5 = [float(val) for val in request.args.get('row5').split(',')]
    mat6 = [float(val) for val in request.args.get('row6').split(',')]
    period = request.args.get('period')



    print(mat1)    
    print(mat2)
    print(mat3)
    print(mat4)
    print(mat5)
    print(mat6)



    #for value in range(matrix_size):
    #    print(mat1[value])
    # Create a 2D array, matrix equivalent of the imaginary unit
    arr = np.array([mat1, mat2, mat3, mat4, mat5, mat6])
    result_after_two_steps = np.linalg.matrix_power(arr, int(period))
    rows0 = result_after_two_steps[0]
    rows1 = result_after_two_steps[1]
    rows2 = result_after_two_steps[2]
    rows3 = result_after_two_steps[3]
    rows4 = result_after_two_steps[4]
    rows5 = result_after_two_steps[5]
    
    # Display the array
    print("Our Array...\n",arr)
    # Check the Dimensions
    print("\nDimensions of our Array...\n",arr.ndim)
    # Get the Datatype
    print("\nDatatype of our Array object...\n",arr.dtype)
    # Get the Shape
    print("\nShape of our Array object...\n",arr.shape)
    return render_template('res6.html', rows0=rows0, rows1=rows1, rows2=rows2, rows3=rows3, rows4=rows4, rows5=rows5)   


@app.route('/7')
def form7():
    return render_template('7.html')

@app.route('/calc7', methods=['GET'])
def calc7():
    language = request.args.get('row1')
    print(language)
    mat1 = [float(val) for val in request.args.get('row1').split(',')]
    mat2 = [float(val) for val in request.args.get('row2').split(',')]
    mat3 = [float(val) for val in request.args.get('row3').split(',')]
    mat4 = [float(val) for val in request.args.get('row4').split(',')]
    mat5 = [float(val) for val in request.args.get('row5').split(',')]
    mat6 = [float(val) for val in request.args.get('row6').split(',')]
    mat7 = [float(val) for val in request.args.get('row7').split(',')]
    period = request.args.get('period')


    print(mat1)    
    print(mat2)
    print(mat3)
    print(mat4)
    print(mat5)
    print(mat6)
    print(mat7)



    #for value in range(matrix_size):
    #    print(mat1[value])
    # Create a 2D array, matrix equivalent of the imaginary unit
    arr = np.array([mat1, mat2, mat3, mat4, mat5, mat6, mat7])
    result_after_two_steps = np.linalg.matrix_power(arr, int(period))
    rows0 = result_after_two_steps[0]
    rows1 = result_after_two_steps[1]
    rows2 = result_after_two_steps[2]
    rows3 = result_after_two_steps[3]
    rows4 = result_after_two_steps[4]
    rows5 = result_after_two_steps[5]
    rows6 = result_after_two_steps[6]
    # Display the array
    print("Our Array...\n",arr)
    # Check the Dimensions
    print("\nDimensions of our Array...\n",arr.ndim)
    # Get the Datatype
    print("\nDatatype of our Array object...\n",arr.dtype)
    # Get the Shape
    print("\nShape of our Array object...\n",arr.shape)
    return render_template('res7.html', rows0=rows0, rows1=rows1, rows2=rows2, rows3=rows3, rows4=rows4, rows5=rows5, rows6=rows6)   


@app.route('/8')
def form8():
    return render_template('8.html')

@app.route('/calc8', methods=['GET'])
def calc8():
    language = request.args.get('row1')
    print(language)
    mat1 = [float(val) for val in request.args.get('row1').split(',')]
    mat2 = [float(val) for val in request.args.get('row2').split(',')]
    mat3 = [float(val) for val in request.args.get('row3').split(',')]
    mat4 = [float(val) for val in request.args.get('row4').split(',')]
    mat5 = [float(val) for val in request.args.get('row5').split(',')]
    mat6 = [float(val) for val in request.args.get('row6').split(',')]
    mat7 = [float(val) for val in request.args.get('row7').split(',')]
    mat8 = [float(val) for val in request.args.get('row8').split(',')]
    period = request.args.get('period')

 


    print(mat1)    
    print(mat2)
    print(mat3)
    print(mat4)
    print(mat5)
    print(mat6)
    print(mat7)
    print(mat8)


    #for value in range(matrix_size):
    #    print(mat1[value])
    # Create a 2D array, matrix equivalent of the imaginary unit
    arr = np.array([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8])
    result_after_two_steps = np.linalg.matrix_power(arr, int(period))
    print(result_after_two_steps)

    rows0 = result_after_two_steps[0]
    rows1 = result_after_two_steps[1]
    rows2 = result_after_two_steps[2]
    rows3 = result_after_two_steps[3]
    rows4 = result_after_two_steps[4]
    rows5 = result_after_two_steps[5]
    rows6 = result_after_two_steps[6]
    rows7 = result_after_two_steps[7]
    # Display the array
    print("Our Array...\n",arr)
    # Check the Dimensions
    print("\nDimensions of our Array...\n",arr.ndim)
    # Get the Datatype
    print("\nDatatype of our Array object...\n",arr.dtype)
    # Get the Shape
    print("\nShape of our Array object...\n",arr.shape)
    return render_template('res8.html', rows0=rows0, rows1=rows1, rows2=rows2, rows3=rows3, rows4=rows4, rows5=rows5, rows6=rows6, rows7=rows7)   



@app.route('/9')
def form9():
    return render_template('9.html')

@app.route('/calc9', methods=['GET'])
def calc9():
    language = request.args.get('row1')
    print(language)
    mat1 = [float(val) for val in request.args.get('row1').split(',')]
    mat2 = [float(val) for val in request.args.get('row2').split(',')]
    mat3 = [float(val) for val in request.args.get('row3').split(',')]
    mat4 = [float(val) for val in request.args.get('row4').split(',')]
    mat5 = [float(val) for val in request.args.get('row5').split(',')]
    mat6 = [float(val) for val in request.args.get('row6').split(',')]
    mat7 = [float(val) for val in request.args.get('row7').split(',')]
    mat8 = [float(val) for val in request.args.get('row8').split(',')]
    mat9 = [float(val) for val in request.args.get('row9').split(',')]
    period = request.args.get('period')



    print(mat1)    
    print(mat2)
    print(mat3)
    print(mat4)
    print(mat5)
    print(mat6)
    print(mat7)
    print(mat8)
    print(mat9)


    #for value in range(matrix_size):
    #    print(mat1[value])
    # Create a 2D array, matrix equivalent of the imaginary unit
    arr = np.array([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9])
    result_after_two_steps = np.linalg.matrix_power(arr, int(period))
    print(result_after_two_steps)

    rows0 = result_after_two_steps[0]
    rows1 = result_after_two_steps[1]
    rows2 = result_after_two_steps[2]
    rows3 = result_after_two_steps[3]
    rows4 = result_after_two_steps[4]
    rows5 = result_after_two_steps[5]
    rows6 = result_after_two_steps[6]
    rows7 = result_after_two_steps[7]
    rows8 = result_after_two_steps[8]
    # Display the array
    print("Our Array...\n",arr)
    # Check the Dimensions
    print("\nDimensions of our Array...\n",arr.ndim)
    # Get the Datatype
    print("\nDatatype of our Array object...\n",arr.dtype)
    # Get the Shape
    print("\nShape of our Array object...\n",arr.shape)
    return render_template('res9.html', rows0=rows0, rows1=rows1, rows2=rows2, rows3=rows3, rows4=rows4, rows5=rows5, rows6=rows6, rows7=rows7, rows8=rows8)   
@app.route('/10')
def form10():
    return render_template('10.html')

@app.route('/calc10', methods=['GET'])
def calc10():
    language = request.args.get('row1')
    print(language)
    mat1 = [float(val) for val in request.args.get('row1').split(',')]
    mat2 = [float(val) for val in request.args.get('row2').split(',')]
    mat3 = [float(val) for val in request.args.get('row3').split(',')]
    mat4 = [float(val) for val in request.args.get('row4').split(',')]
    mat5 = [float(val) for val in request.args.get('row5').split(',')]
    mat6 = [float(val) for val in request.args.get('row6').split(',')]
    mat7 = [float(val) for val in request.args.get('row7').split(',')]
    mat8 = [float(val) for val in request.args.get('row8').split(',')]
    mat9 = [float(val) for val in request.args.get('row9').split(',')]
    mat10 = [float(val) for val in request.args.get('row10').split(',')]
    period = request.args.get('period')

    print(mat1)    
    print(mat2)
    print(mat3)
    print(mat4)
    print(mat5)
    print(mat6)
    print(mat7)
    print(mat8)
    print(mat9)
    print(mat10)

    #for value in range(matrix_size):
    #    print(mat1[value])
    # Create a 2D array, matrix equivalent of the imaginary unit
    arr = np.array([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10])
    # Display the array
    print("Our Array...\n",arr)
    # Check the Dimensions
    print("\nDimensions of our Array...\n",arr.ndim)
    # Get the Datatype
    print("\nDatatype of our Array object...\n",arr.dtype)
    # Get the Shape
    print("\nShape of our Array object...\n",arr.shape)

    result_after_two_steps = np.linalg.matrix_power(arr, int(period))

    rows0 = result_after_two_steps[0]
    rows1 = result_after_two_steps[1]
    rows2 = result_after_two_steps[2]
    rows3 = result_after_two_steps[3]
    rows4 = result_after_two_steps[4]
    rows5 = result_after_two_steps[5]
    rows6 = result_after_two_steps[6]
    rows7 = result_after_two_steps[7]
    rows8 = result_after_two_steps[8]
    rows9 = result_after_two_steps[9]

    


    print("HAHAHAHAHA")
    print(result_after_two_steps)
    return render_template('res10.html', rows0=rows0, rows1=rows1, rows2=rows2, rows3=rows3, rows4=rows4, rows5=rows5, rows6=rows6, rows7=rows7, rows8=rows8, rows9=rows9)   
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()