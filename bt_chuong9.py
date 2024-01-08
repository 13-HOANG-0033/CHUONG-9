#bài 9.1
def sign(x):
    if x<0:
        return "-1"
    elif x>0:
        return "1"
    elif x==0:
        return "0"
x=int(input("Nhập x : "))
print("sign(",x,")=",sign(x))

#bài 9.2
#Viết chương trình tính năm âm lích
can = ["Canh","Tân","Nhâm","Quý","Giáp","Ất","Bính","Đinh","Mậu","Kỷ"]
chi = ["Thân","Dậu","Tuất","Hợi","Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi"]
def tinh_nam_am_lich(n):
    i=n%10
    j=n%12
    return i,j
n = int(input("Nhập năm: "))
i,j = tinh_nam_am_lich(n)
print("Năm",n,"lịch âm là năm:",can[i],chi[j])

#bài 9.3
#Tính BMI và in ra đánh giá
import math
def tinh_bmi(can_nang,chieu_cao):
    bmi=can_nang/math.pow(chieu_cao,2)
    return bmi
def danh_gia(bmi):
	if bmi<18.5:
		return 'Bạn đang ở trạng thái Gầy'
	elif 18.5<=bmi<=24.99:
		return 'Bạn đang ở trạng thái Bình thường'
	else:
		return'Bạn đang ở trạng thái Thừa cân'		
can_nang=int(input("Nhập cân nặng (kg): "))
chieu_cao=float(input("Nhập chiều cao (m): "))    
bmi=tinh_bmi(can_nang,chieu_cao)
print("BMI = %0.2f"%bmi)
print(danh_gia(bmi))

#bài 9.4
import math
def tinh_S(n,x):
    S = math.pow((x*x+1),n)
    return S
n = float(input('n = '))
x = float(input("x = "))       
S = tinh_S(n,x)
print("S = %0.2f"%S)

#bài 9.5
import math
def tinh_A(n,x):
    A=math.pow(((x*x)+x+1),n)+math.pow(((x*x)-x+1),n)
    return A
n=float(input('n = '))
x=float(input("x = "))       
A = tinh_A(n,x)
print("A = %0.2f"%A)

#bài 9.6
# Hàm kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(n):
    so_uoc=0
    for i in range(1,n+1):
        if n%i==0:
            so_uoc+=1
    if so_uoc==2:
        return True
    return False
n=int(input("Nhập số cần kiểm tra: "))
print(kiem_tra_so_nguyen_to(n))

#bài 9.7
#Hàm trả về phần nguyên của phép chia hai số nguyên
def chia_lay_nguyen(a,b):
    c=a//b
    return c 
a=int(input("a = "))
b=int(input("b = "))
c= chia_lay_nguyen(a,b)
print("Phần nguyên của",a,"chia",b,"là :",c)

#bài 9.8
# Hàm kiểm tra số hoàn hảo
def kiem_tra_so_hoan_hao(n):
    tong_uoc=0
    for i in range(1,n):
        if n%i==0:
            tong_uoc+=i
    if tong_uoc==n:
        return True
    else:
        return False
n=int(input("Nhập số nguyên dương n: ")) 
if kiem_tra_so_hoan_hao(n):
    print(n,"là số hoàn hảo")
else:
    print(n,"không là số hoàn hảo")

#bài 9.9
# Sử dụng biểu thức lamda để tính diện tích,chu vi (hình tròn , hình chữ nhật)
import math
sht =lambda r:math.pi*math.pow(r,2)
pht =lambda r:2*math.pi*r
scn=lambda a,b:a*b
pcn=lambda a,b:2*(a+b)
r=float(input("Bán kính r = "))
a=float(input("Chiều dài hình chữ nhật a = "))
b=float(input("Chiều rộng hình chữ nhật b = "))
print("S hình tròn = %0.2f"%sht(r))
print("P hình tròn = %0.2f"%pht(r))
print("S hình chữ nhật = %0.2f"%scn(a,b))
print("P hình chữ nhật = %0.2f"%pcn(a,b))


