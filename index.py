def cong(a,b):
    c = a + b
    return c

def tru(a,b):
    tru = a - b
    return tru

def nhan(a,b):
    return a * b

def chia(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        y = int(input("Không thể chia cho 0, Nhập lại số khác 0: "))
        return chia(x , y)
def main():
    print("+--------------------------------Menu--------------------------------+")
    print("|--1. Thực hiện phép tính cộng---------------------------------------|")
    print("|--2. Thực hiện phép tính trừ----------------------------------------|")
    print("|--3. Thực hiện phép tính nhân---------------------------------------|")
    print("|--4. Thực hiện phép tính chia---------------------------------------|")
    print("|--5. Thoát----------------------------------------------------------|")
    print("+--------------------------------------------------------------------+")
    nhap = int(input("\n Nhập lựa chọn của bạn: "))
    if nhap == 1 or nhap == '1':
        a = int(input("Nhập vào số thứ nhất:  "))
        b = int(input("Nhập vào số thứ hai:   "))
        print(f"Kết quả của phép tính là: {cong(a,b)}")
        luachon = input("Bạn có muốn tiếp tục không, Y/N :")
        if luachon == 'Y' or luachon == 'y':
            return main()
        
    elif nhap == 2 or nhap == '2':
        a = int(input("Nhập vào số thứ nhất:  "))
        b = int(input("Nhập vào số thứ hai:   "))
        print(f"Kết quả của phép tính là: {tru(a,b)}")
        luachon = input("Bạn có muốn tiếp tục không, Y/N :")
        if luachon == 'Y' or luachon == 'y':
            return main()
        
    elif nhap == 3 or nhap == '3':
        a = int(input("Nhập vào số thứ nhất:  "))
        b = int(input("Nhập vào số thứ hai:   "))
        print(f"Kết quả của phép tính là: {nhan(a,b)}")
        luachon = input("Bạn có muốn tiếp tục không, Y/N :")
        if luachon == 'Y' or luachon == 'y':
            return main()
        
    elif nhap == 4 or nhap == '4':
        a = int(input("Nhập vào số thứ nhất:  "))
        b = int(input("Nhập vào số thứ hai:   "))
        print(f"Kết quả của phép tính là: {chia(a,b)}")
        luachon = input("Bạn có muốn tiếp tục không, Y/N :")
        if luachon == 'Y' or luachon == 'y':
            return main()
    elif nhap == 5 or nhap == '5':
        exit
    elif nhap != 1 or nhap != '1' and nhap != 2 or nhap != '2' and nhap != 3 or nhap != '3' and nhap != 4 or nhap != '4' and nhap != 5 or nhap != '5':
        print("\n Không có chức năng trong menu, nhập lại!! \n")
        return main()
    

main()
