import asyncpg
from datetime import datetime


from app.model import CameraNew, Statistic

class Database():

    async def create_pool(self):
        
             self.pool = await asyncpg.create_pool(dsn='postgres://vvtnxpvwgyzwqk:3f33be14551e8ab7ec0cb4b066bf4567dca30ba17a745a6e80ca980c6d1ba0d5@ec2-34-255-134-200.eu-west-1.compute.amazonaws.com:5432/d7jahk1cse1r7a')
             print("Connection to PostgreSQL DB successful")
    async def close(self):
           await self.pool.close()
           print("Connecting Close")
    async def add_new_camera(self,camera: CameraNew):
        await self.pool.execute(f'''
        INSERT INTO camera (id_city,addres_name,cameraname) VALUES (1,'{camera.addres_name}','{camera.camera_potok}');
        ''')
    async def take_info_camera(self):
        return await self.pool.fetch(f'''
            SELECT * FROM camera
        ''')
    async def create_call(self,addres_name:str):
        uidcamera = await self.pool.fetchval(f"""
             SELECT id FROM camera WHERE addres_name = '{addres_name}';       
                """)
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        
        #доделать статистику
    async def take_calls(self,period:Statistic):
        print(await self.pool.fetch ( f"""
             select * from monthstatistic where datemonth >= '{period.datestart}' and datemonth =< '{period.dateend}' and where idcamera = {period.cameraid}
            """))
        
    async def take_camera(self):
        return await self.pool.fetch(f'''
            SELECT addres_name,photo from CAMERA;
        ''')
    async def load_photo(self,in_file: str,addres:str):
        # если что можно вставить https://github.com/JustUpFinal/back/tree/master/ для url
        await self.pool.execute(f"""
                UPDATE camera set photo='{in_file}' where addres_name ='{addres}';
            """)
