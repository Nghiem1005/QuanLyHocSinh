from my_app import db
from sqlalchemy import PrimaryKeyConstraint, Float, ForeignKey, Boolean, Column, NCHAR, String, Integer, NVARCHAR, \
    DateTime, Numeric
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

"""
class GiaoVien(db.Model):
    __tablename__ = "GiaoVien"
    MaGiaoVien = Column(Integer, primary_key=True, autoincrement=True)
    TenGiaoVien = Column(NVARCHAR(50), nullable=False)
    GioiTinh = Column(NVARCHAR(50), nullable=False)
    Tuoi = Column(Integer, nullable=False)
    Email = Column(String(50), nullable=True)
    SDT = Column(String(50), nullable=False)
    MatKhau = Column(String(50), nullable=False)
    Quyen = Column(NCHAR(10), nullable=False)
    phanCong = relationship('PhanCong', backref='Giáo Viên', lazy=True)

    def __str__(self):
        return self.TenGiaoVien


class HocKy(db.Model):
    __tablename__ = "HocKy"
    MaHocKy = Column(Integer, primary_key=True, autoincrement=True)
    TenHocKy = Column(NVARCHAR(50), nullable=False)
    NamHoc = Column(NVARCHAR(50), nullable=False)
    NgayBatDau = Column(DateTime, nullable=False)
    NgayKetThuc = Column(DateTime, nullable=False)
    phanCong = relationship('PhanCong', backref='Học Kỳ', lazy=True)
    chiTietHocSinh = relationship('ChiTietHocSinh', backref='Học Kỳ', lazy=True)

    def __str__(self):
        return self.TenHocKy
"""


class HocSinh(db.Model):
    __tablename__ = "HocSinh"
    MaHocSinh = Column(Integer, primary_key=True, autoincrement=True)
    TenHocSinh = Column(NVARCHAR(50), nullable=False)
    NgaySinh = Column(DateTime, nullable=False)
    GioiTinh = Column(NVARCHAR(50), nullable=False)
    Email = Column(String(50), nullable=True)
    HocKy = Column(Integer, nullable=False)
    Anh = Column(NVARCHAR(50), nullable=False)
    diemMonHocHocSinh = relationship('DiemMonHocHocSinh', backref='Học sinh', lazy=True)
    diaChi = relationship('DiaChiHS', backref='Học Sinh', lazy=True)
    taiKhoan = relationship('TaiKhoan', backref='Học sinh', lazy=True)
    lopHoc = relationship('LopHoc', backref='Học sinh', lazy=True)

    def __str__(self):
        return self.TenHocSinh


class LopHoc(db.Model):
    __tablename__ = "LopHoc"
    MaLopHoc = Column(Integer, primary_key=True, autoincrement=True)
    TenLop = Column(NVARCHAR(50), nullable=False)
    SiSo = Column(Integer, nullable=False)
    maHocSinh = Column(Integer, ForeignKey(HocSinh.MaHocSinh), nullable=False)

    def __str__(self):
        return self.TenLop


class TaiKhoan(db.Model, UserMixin):
    __tablename__ = "TaiKhoan"
    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    roles = Column(Integer, nullable=False)  # 1: Admin
    maHocSinh = Column(Integer, ForeignKey(HocSinh.MaHocSinh), nullable=False)

    def __str__(self):
        return self.username


class DiaChiHS(db.Model):
    __tablename__ = "DiaChiHS"
    MaDiaChi = Column(Integer, primary_key=True, autoincrement=True)
    PhuongXa = Column(NVARCHAR(50), nullable=False)
    QuanHuyen = Column(NVARCHAR(50), nullable=False)
    TinhThanhPho = Column(NVARCHAR(50), nullable=False)
    maHocSinh = Column(Integer, ForeignKey(HocSinh.MaHocSinh), nullable=False)

    def __str__(self):
        return "Phường: " + self.PhuongXa + ", " + self.TinhThanhPho


class Diem(db.Model):
    MaDiem = Column(Integer, primary_key=True, autoincrement=True)
    LoaiDiem = Column(NVARCHAR(50), nullable=False)
    SoDiem = Column(Float, nullable=False)
    diemMonHocHocSinh = relationship('DiemMonHocHocSinh', backref='Điểm', lazy=True)

    def __str__(self):
        return "Loại điểm: " + str(self.LoaiDiem) + ", Số điểm: " + str(self.SoDiem)


class MonHoc(db.Model):
    __tablename__ = "MonHoc"
    MaMonHoc = Column(Integer, primary_key=True, autoincrement=True)
    TenMonHoc = Column(NVARCHAR(50), nullable=False)
    diemMonHocHocSinh = relationship('DiemMonHocHocSinh', backref='Môn học', lazy=True)

    def __str__(self):
        return self.TenMonHoc


class DiemMonHocHocSinh(db.Model):
    __tablename__ = "DiemMonHocHocSinh"
    maHocSinh = Column(Integer, ForeignKey(HocSinh.MaHocSinh), nullable=False)
    maDiem = Column(Integer, ForeignKey(Diem.MaDiem), nullable=False)
    maMonHoc = Column(Integer, ForeignKey(MonHoc.MaMonHoc), nullable=False)
    db.PrimaryKeyConstraint(maHocSinh, maDiem, maMonHoc)

    def __str__(self):
        return "Điểm của học sinh: " + HocSinh.query.get(self.maHocSinh).TenHocSinh


"""
class PhanCong(db.Model):
    __tablename__ = "PhanCong"
    maGiaoVien = Column(Integer, ForeignKey(GiaoVien.MaGiaoVien), nullable=False)
    maLopHoc = Column(Integer, ForeignKey(LopHoc.MaLopHoc), nullable=False)
    maHocKy = Column(Integer, ForeignKey(HocKy.MaHocKy), nullable=False)
    maMonnHoc = Column(Integer, ForeignKey(MonHoc.MaMonHoc), nullable=False)
    db.PrimaryKeyConstraint(maGiaoVien, maLopHoc, maMonnHoc, maHocKy)

    def __str__(self):
        return "Lớp: " + LopHoc.query.get(self.maLopHoc).TenLop + "-Môn: " + MonHoc.query.get(self.maMonnHoc).TenMonHoc + ". "
"""

if __name__ == '__main__':
    db.create_all()

