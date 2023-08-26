def tinh_diem_chu(diem_thuong_xuyen, diem_giua_ki, diem_cuoi_ki):
    k1 = input("Nhap he so thuong xuyen: ")
    k2 = input("Nhap he so giua ki: ")
    k3 = input("Nhap he so cuoi ki: ")
    diem_tong_ket = k1*diem_thuong_xuyen + k2*diem_giua_ki + k3*diem_cuoi_ki
    if diem_tong_ket >= 9:
        return 'A'
    elif diem_tong_ket >= 8:
        return 'B'
    elif diem_tong_ket >= 7:
        return 'C'
    elif diem_tong_ket >= 6:
        return 'D'
    else:
        return 'F'
    