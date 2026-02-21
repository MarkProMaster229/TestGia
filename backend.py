from flask import Flask, render_template, request, send_from_directory,redirect, url_for
import os

#тут модуль 2 и 3 
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
MyFolderForVolodia = os.path.join(basedir, '..', 'uploads')
app.config['UPLOAD_FOLDER'] = os.path.normpath(MyFolderForVolodia)

from BdConnect import GetMaterial_suppliers, GetMaterial_type, GetMaterials, GetProduct_type, GetSuppliers


@app.route('/', methods=['GET', 'POST'])
def index():
    Material_suppliers = GetMaterial_suppliers()
    Material_type = GetMaterial_type()
    Product_type = GetProduct_type()
    Suppliers = GetSuppliers()
    Materials = GetMaterials()
    a = Materials.GetMinColVo(2)
    
    
    total_price = None 
    if request.method == 'POST':
        user_data = request.form.get('chet')
        try:
            total_price = float(user_data) * 100
        except:
            total_price = "пустое поле"

    total_price1 = None 
    if request.method == 'POST':
        user_data = request.form.get('chet1')
        try:
            total_price1 = float(user_data) * 100 
        except:
            total_price1 = "пустое поле"


    total_price2 = None 
    if request.method == 'POST':
        user_data = request.form.get('chet2')
        try:
            total_price2 = float(user_data) * 100 
        except:
            total_price2 = "пустое поле"


    
    return render_template('main.html', result=total_price, result1= total_price1, result2= total_price2, items=[a] )




if __name__ == "__main__":
    app.run(debug=True)