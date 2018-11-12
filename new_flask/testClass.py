class Sinhvien:
#    'Class co so chung cho tat ca sinh vien'
   svCount = 0

   def __init__(self, ten, hocphi):
      self.ten = ten
      self.hocphi = hocphi
      Sinhvien.svCount += 1
   
   def displayCount(self):
     print "Tong so Sinh vien %d" % Sinhvien.svCount

   def displaySinhvien(self):
      print "Ten : ", self.ten,  ", Hoc phi: ", self.hocphi

"Lenh nay tao doi tuong dau tien cua lop Sinhvien"
sv1 = Sinhvien("Hoang", 4000000)
"Lenh nay tao doi tuong thu hai cua lop Sinhvien"
sv2 = Sinhvien("Huong", 4500000)
sv1.displaySinhvien()
sv2.displaySinhvien()
print "Tong so Sinh vien %d" % Sinhvien.svCount