# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Address(models.Model):
    idaddress = models.AutoField(db_column='idAddress', primary_key=True)  # Field name made lowercase.
    cust_idcustomer = models.ForeignKey('Customer', models.DO_NOTHING, db_column='cust_idCustomer')  # Field name made lowercase.
    postcode = models.CharField(max_length=10)
    housenumber = models.CharField(db_column='houseNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    county = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Address'


class Customer(models.Model):
    idcustomer = models.AutoField(db_column='idCustomer', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=200)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=200)  # Field name made lowercase.
    blacklist = models.IntegerField()
    emailaddress = models.CharField(db_column='eMailAddress', max_length=200, blank=True, null=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='contactNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=45, blank=True, null=True)
    dob = models.CharField(max_length=45, blank=True, null=True)
    maritalstatus = models.CharField(db_column='maritalStatus', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customer'


class Employee(models.Model):
    idemployee = models.AutoField(db_column='idEmployee', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Employee'


class Payment(models.Model):
    idpayment = models.AutoField(db_column='idPayment', primary_key=True)  # Field name made lowercase.
    cust_idcustomer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='cust_idCustomer')  # Field name made lowercase.
    type = models.CharField(max_length=45, blank=True, null=True)
    cardnumber = models.CharField(db_column='cardNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateField(db_column='expiryDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment'


class Product(models.Model):
    idproduct = models.AutoField(db_column='idProduct', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=200, blank=True, null=True)
    buyprice = models.FloatField(db_column='buyPrice', blank=True, null=True)  # Field name made lowercase.
    saleprice = models.FloatField(db_column='salePrice', blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Product'


class Purchase(models.Model):
    idpurchase = models.AutoField(db_column='idPurchase', primary_key=True)  # Field name made lowercase.
    purchasestatus = models.CharField(db_column='purchaseStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    emp_idemployee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='emp_idEmployee', blank=True, null=True)  # Field name made lowercase.
    cust_idcustomer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='cust_idCustomer', blank=True, null=True)  # Field name made lowercase.
    add_idaddress = models.ForeignKey(Address, models.DO_NOTHING, db_column='add_idAddress', blank=True, null=True)  # Field name made lowercase.
    pay_idpayment = models.ForeignKey(Payment, models.DO_NOTHING, db_column='pay_idPayment', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    gdzdate = models.DateField(db_column='GDZDate', blank=True, null=True)  # Field name made lowercase.
    dispatcheddate = models.DateField(db_column='dispatchedDate', blank=True, null=True)  # Field name made lowercase.
    delivereddate = models.DateField(db_column='deliveredDate', blank=True, null=True)  # Field name made lowercase.
    cancelleddate = models.DateField(db_column='cancelledDate', blank=True, null=True)  # Field name made lowercase.
    returneddate = models.DateField(db_column='returnedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Purchase'


class Purchaselines(models.Model):
    pur_idpurchase = models.ForeignKey(Purchase, models.DO_NOTHING, db_column='pur_idPurchase')  # Field name made lowercase.
    pro_idproduct = models.ForeignKey(Product, models.DO_NOTHING, db_column='pro_idProduct')  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PurchaseLines'
        unique_together = (('pur_idpurchase', 'pro_idproduct'),)


class Supplier(models.Model):
    idsupplier = models.AutoField(db_column='idSupplier', primary_key=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='contactNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Supplier'


class Supplierorder(models.Model):
    idsupplierorder = models.IntegerField(db_column='idSupplierOrder', primary_key=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='createDate', max_length=45, blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.CharField(db_column='deliveryDate', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sup_idsupplier = models.ForeignKey(Supplier, models.DO_NOTHING, db_column='sup_idSupplier', blank=True, null=True)  # Field name made lowercase.
    emp_idemployee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='emp_idEmployee', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SupplierOrder'


class Supplierorderlines(models.Model):
    pro_idproduct = models.ForeignKey(Product, models.DO_NOTHING, db_column='pro_idProduct')  # Field name made lowercase.
    sup_idsupplierorder = models.ForeignKey(Supplierorder, models.DO_NOTHING, db_column='sup_idSupplierOrder')  # Field name made lowercase.
    quantity = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SupplierOrderLines'
        unique_together = (('pro_idproduct', 'sup_idsupplierorder'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
