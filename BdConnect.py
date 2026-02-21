#тут модуль как первый так и второй так и третий, они все взаимосвязаны я не знаю как их делить

from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine('postgresql+psycopg2://postgres:Admin123@127.0.0.1:5433/mosaic')

#this GEtMEthod
class GetMaterial_suppliers():
    def GetID(self, num):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT ID FROM Material_suppliers LIMIT 1 OFFSET {num}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetName_material(self, mater):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT name_material FROM Material_suppliers LIMIT 1 OFFSET {mater}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetPostawshik(self, Postawshik):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT postawshik FROM Material_suppliers LIMIT 1 OFFSET {Postawshik}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"

class GetMaterial_type():
    def GetID(self, num):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT ID FROM Material_type LIMIT 1 OFFSET {num}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetType_material(self, Type_material):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT type_material FROM Material_type LIMIT 1 OFFSET {Type_material}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetProchentPoteri(self, ProchentPoteri):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT prochentPoteri FROM Material_type LIMIT 1 OFFSET {ProchentPoteri}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
class GetMaterials():
    def GetID(num):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT ID FROM Materials LIMIT 1 OFFSET {num}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetNameMaterial(self, NameMaterial):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT nameMaterial FROM Materials LIMIT 1 OFFSET {NameMaterial}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetTypeMaterial(self, TypeMaterial):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT typeMaterial FROM Materials LIMIT 1 OFFSET {TypeMaterial}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetPrise(self, Prise):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT prise FROM Materials LIMIT 1 OFFSET {Prise}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetCountInSklad(self, CountInSklad):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT countInSklad FROM Materials LIMIT 1 OFFSET {CountInSklad}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetMinColVo(self, MinColVo):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT minColVo FROM Materials LIMIT 1 OFFSET {MinColVo}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    

    def GetColvoinupakovka(self, Colvoinupakovka):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT colvoinupakovka FROM Materials LIMIT 1 OFFSET {Colvoinupakovka}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"

    def GetEdenIzm(self, EdenIzm):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT edenIzm FROM Materials LIMIT 1 OFFSET {EdenIzm}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"    
    

class GetProduct_type():
    def GetID(self, num):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT ID FROM Product_type LIMIT 1 OFFSET {num}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetTyphProduct(self, TyphProduct):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT typhProduct FROM Product_type LIMIT 1 OFFSET {TyphProduct}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetkoofTypeProduct(self, koofTypeProduct):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT koofTypeProduct FROM Product_type LIMIT 1 OFFSET {koofTypeProduct}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    

class GetSuppliers():
    def GetID(self, num):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT ID FROM Suppliers LIMIT 1 OFFSET {num}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetNamePostaw(self, NamePostaw):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT namePostaw FROM Suppliers LIMIT 1 OFFSET {NamePostaw}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetTypePost(self, TypePost):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT typePost FROM Suppliers LIMIT 1 OFFSET {TypePost}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetInn(self, Inn):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT Inn FROM Suppliers LIMIT 1 OFFSET {Inn}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetReiting(self, Reiting):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT reiting FROM Suppliers LIMIT 1 OFFSET {Reiting}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"
    
    def GetDataStart(self, DataStart):
        conn = engine.connect()
        result = conn.execute(text(f"SELECT dataStart FROM Suppliers LIMIT 1 OFFSET {DataStart}")).fetchall()
        conn.close()
        return result[0][0] if result else "Никого не нашли"











#--create table Material_suppliers(
#--id serial primary key,
#--name_material varchar(255),
#--postawshik varchar(255)
#--)

#--create table Material_type(
#--id serial primary key,
#--type_material varchar(255),
#--prochentPoteri float
#--)
#--drop table Material_type


#--create table Materials(
#--id serial primary key,
#--nameMaterial varchar(255),
#--typeMaterial varchar(255),
#--prise float,
#--countInSklad float,
#--minColVo float,
#--colvoinupakovka int,
#--edenIzm varchar(255)
#--)
#--drop table Materials

#--create table Product_type(
#--id serial primary key,
#--typhProduct varchar(255),
#--koofTypeProduct float
#--)
#--drop table Product_type

#--create table Suppliers(
#--id serial primary key,
#--namePostaw varchar(255),
#--typePost varchar(255),
#--Inn int,
#--reiting int,
#--dataStart Date
#--)

