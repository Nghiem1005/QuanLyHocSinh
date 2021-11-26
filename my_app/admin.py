from flask_admin._backwards import ObsoleteAttr
from flask_admin.contrib.sqla import ModelView
from my_app.models import MonHoc, Diem, DiaChiHS, HocSinh, LopHoc
from my_app import db, admin
from flask_admin import BaseView, expose
from flask_login import logout_user, current_user
from flask import redirect


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class MonHocModelView(AuthenticatedView):
    can_export = True
    column_labels = dict(TenMonHoc='Tên môn học', MaMonHoc='Mã môn học', phanCong='Phân công', chiTietHocSinh='Chi tiết học sinh')
    column_filters = ('TenMonHoc', 'MaMonHoc')


class HocSinhModelView(AuthenticatedView):
    can_export = True
    column_list = ('TenHocSinh', 'GioiTinh', 'Email', 'chiTietHocSinh', 'diaChi', 'soDienThoaiHS')
    column_labels = dict(TenHocSinh='Tên học sinh', GioiTinh='Giới tính', soDienThoaiHS='SĐT', diaChi='Địa chỉ', chiTietHocSinh='Chi tiết HS', MatKhau='Mật khẩu')
    column_filters = ('TenHocSinh', 'GioiTinh', 'soDienThoaiHS')


class GiaoVienModelView(AuthenticatedView):
    can_export = True
    column_list = ('TenGiaoVien', 'GioiTinh', 'Tuoi', 'Email', 'SDT', 'Quyen', 'phanCong')
    column_labels = dict(TenGiaoVien='Tên giáo viên', GioiTinh='Giới tính', Tuoi='Tuổi', SDT='SĐT', Quyen='Quyền', phanCong='Phân công', MatKhau='Mật khẩu')
    column_filters = ('TenGiaoVien', 'GioiTinh', 'Quyen')


class ChiTietHocSinhModelView(AuthenticatedView):
    can_export = True
    #column_list = ('maHocSinh', 'LopHoc.TenLop', 'HocKy.TenHocKy', 'MonHoc.TenMonHoc', 'Diem.SoDiem', 'NgayNhap')
    column_labels = dict(maHocSinh='Tên học sinh', maLopHoc='Tên lớp học', maHocKy='Tên học kỳ', maMonHoc='Tên môn học', maDiem='Điểm', NgayNhap='Ngày nhập', phanCong='Phân công', chiTietHocSinh='Chi tiết học sinh')


class DiaChiHSModelView(AuthenticatedView):
    can_export = True
    column_list = ('SoNha', 'TenDuong', 'PhuongXa', 'QuanHuyen', 'TinhThanhPho')
    column_labels = dict(SoNha='Số nhà', TenDuong='Tên đường', PhuongXa='Phường/Xã', QuanHuyen='Quận/Huyện', TinhThanhPho='Tỉnh/Thành phố trực thuộc Tỉnh')
    column_filters = ('TenDuong', 'PhuongXa', 'QuanHuyen', 'TinhThanhPho')


class DiemModelView(AuthenticatedView):
    can_export = True
    column_list = ('LoaiDiem', 'SoDiem')
    column_labels = dict(LoaiDiem='Loại điểm', SoDiem='Số điểm', chiTietHocSinh='Chi tiết học sinh')
    column_filters = ('LoaiDiem', 'SoDiem')


class HocKyModelView(AuthenticatedView):
    can_export = True
    column_list = ('TenHocKy', 'NamHoc', 'NgayBatDau', 'NgayKetThuc')
    column_labels = dict(TenHocKy='Tên học kỳ', NamHoc='Năm học', NgayBatDau='Ngày bắt đầu', NgayKetThuc='Ngày kết thúc',  phanCong='Phân công', chiTietHocSinh='Chi tiết học sinh')
    column_filters = ('TenHocKy', 'NamHoc')


class LopHocModelView(AuthenticatedView):
    can_export = True
    #column_list = ('GiaoVi', 'SiSo')
    column_labels = dict(TenLop='Tên lớp', SiSo='Sỉ số',  phanCong='Phân công', chiTietHocSinh='Chi tiết học sinh')


class PhanCongModelView(AuthenticatedView):
    can_export = True
    #column_list = ('GiaoVien', 'LopHoc.TenLopHoc', 'HocKy.TenHocKy', 'MonHoc.TenMonHoc')
    #column_labels = dict(TenLop='Tên lớp', SiSo='Sỉ số')


class SoDienThoaiHocSinhModelView(AuthenticatedView):
    can_export = True
    column_list = ('LoaiSoDienThoai', 'SoDienThoai')
    column_labels = dict(LoaiSoDienThoai='Loại số điện thoại', SoDienThoai='Số điện thoại')
    column_filters = ('LoaiSoDienThoai', 'SoDienThoai')


class StatsView(BaseView):
    @expose("/")
    def index(self):
        return self.render("admin/stats.html")

    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(MonHocModelView(MonHoc, db.session, name="Môn học"))
admin.add_view(GiaoVienModelView(GiaoVien, db.session, name="Giáo viên"))
admin.add_view(ChiTietHocSinhModelView(ChiTietHocSinh, db.session, name="Chi tiết học sinh"))
admin.add_view(DiaChiHSModelView(DiaChiHS, db.session, name="Địa chỉ"))
admin.add_view(DiemModelView(Diem, db.session, name="Điểm"))
admin.add_view(HocKyModelView(HocKy, db.session, name="Học kỳ"))
admin.add_view(HocSinhModelView(HocSinh, db.session, name="Học sinh"))
admin.add_view(LopHocModelView(LopHoc, db.session, name="Lớp học"))
admin.add_view(PhanCongModelView(PhanCong, db.session, name="Phân công"))
admin.add_view(SoDienThoaiHocSinhModelView(SoDienThoaiHocSinh, db.session, name="Số điện thoại HS"))

admin.add_view(StatsView(name="Thống kê"))
admin.add_view(LogoutView(name="Đăng xuất"))





