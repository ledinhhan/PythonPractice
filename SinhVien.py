class SinhVien:
    'Class co so chung cho tat ca sinh vien'

    svCount = 0
    def __init__(self, ten, hocphi):
        self.ten = ten
        self.hocphi = hocphi
        SinhVien.svCount += 1

    def displayCount(self):
        print("Tong so Sinh vien %d" % SinhVien.svCount)

    def displaySinhvien(self):
        print("Ten : ", self.ten, ", Hoc phi: ", self.hocphi)

    def __str__(self):
        return ("Day la sinh Vien: %s" % self.ten)

class Adult:
    AdultCount = 0

    def __init__(self, ten, tuoi = 20, gioitinh = "Nam"):
        self.ten = ten
        self.tuoi = tuoi
        self.gioitinh = gioitinh
        Adult.AdultCount += 1

    def displayAdult(self):
        print("Ten cua nguoi lon la: %s" % self.ten)

    def displayCountAdult(self):
        print("Tong so nguoi lon la: %d" % Adult.AdultCount)