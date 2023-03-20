class Fruit:                                                        
    def __init__(self,fruit_name,price):                                    # attribute ของ class Fruit
        self.fruit_name = fruit_name
        self.price = price
    def intro_fruit(self):                                                  # method เริ่มการขาย
        self.word = 'กินผลไม้ดีต่อสุขภาพ'
        return self.word
    def let_sell(self):                                                     # method ลักษณการขาย
        return 'ผลไม้เราขายเป็นกิโลกรัม(kg)นะ'
    def detail_fruit(self):                                                 # method ชื่อผลไม้ ราคา
        return f'{self.fruit_name} ราคากิโลกรัมละ {self.price} บาท'
print('############ obj fruit1 class Fruit ############\n')
fruit1 = Fruit('ทุเรียน',130)    
print(fruit1.intro_fruit())
print(fruit1.let_sell())
print(fruit1.detail_fruit())
##########################################################################################
class Sellmethod(Fruit):                                                 
    def __init__(self, fruit_name,price,weight):                            # attribute ของ class Sellmethod สืบทอดคลาส Inheritance จาก class Fruit
        super().__init__(fruit_name,price)
        self.weight = weight                               
    def sell_weight(self):                                                  # method คืนค่า น้ำหนัก
        return self.weight    
    def sell_net(self):                                                     # method คืนค่า ราคาขายทั้งหมด
        return (self.price)*(self.weight)
##########################################################################################
print('############ obj sellfruit1  class Sellmethod สืบทอดจาก class Fruit ############\n')
sellfruit1 = Sellmethod('ทุเรียน',130,8)
print('ชนิดผลไม้ :',sellfruit1.fruit_name,'ราคา',sellfruit1.price,'บาท')      # แสดงชื่อผลไม้
print('น้ำหนักผลไม้ :',sellfruit1.sell_weight(),'กิโลกรัม')                      # แสดงน้ำหนัก(กิโลกรัมkg)
print('รวมเงินค่าผลไม้ :',f'{sellfruit1.sell_net():.2f}','บาท')                 # แสดงรายขายทั้งสิ้น(น้ำหนัก*ราคาต่อกิโลกรัมkg)