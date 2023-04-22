import requests
from PIL import Image
from io import BytesIO

grafik_URL = 'https://image-charts.com/chart'

class performans():
    
    def __init__(self,name,may,jun,jul,aug,sep):
        self.name = name
        self.may = may
        self.jun = jun
        self.jul = jul
        self.aug = aug
        self.sep = sep
        
    def performans_ayarla(self):
        return ",".join([
            str(self.may),
            str(self.jun),
            str(self.jul),
            str(self.aug),
            str(self.sep)
        ])
        
    def performans_kiyasla(self,kiyaslanacak_islemci):
        payload = {
            'chco' : '3092de,092182',
            'cht' : 'bhg',
            'chdl' : self.name + '|' + kiyaslanacak_islemci.name,
            'chs' : '999x999',
            'chd' : 't:'+ self.performans_ayarla() + '|' + kiyaslanacak_islemci.performans_ayarla(),
            'chl' : 'May|Jun|July|August|September|May|Jun|July|August|September',
            'chan' : None,
            'chm' : 'B,AAAAAABB,0,0,0|B,0073CFBB,1,0,0'
        }

        response = requests.post(grafik_URL, data=payload)
        image = Image.open(BytesIO(response.content))
        image.show()
        

intel = performans('intel','19.98','20.62','21.59','19.83','19.88')
amd = performans('amd','10.76','11.30','11.77','12.43','12.95')

print(intel.performans_kiyasla(amd))



