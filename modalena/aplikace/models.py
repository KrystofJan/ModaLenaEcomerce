from django.db import models
from django.urls import reverse

# Create your models here.
class Adresa(models.Model):
    adresa_id = models.AutoField(primary_key=True)
    zeme = models.CharField(max_length=25)
    mesto = models.CharField(max_length=55)
    ulice = models.CharField(max_length=75)
    cislo_popisne = models.IntegerField()
    psc = models.CharField(max_length=6)
    cislo_bytu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adresa'
    def __str__(self) -> str:
        return self.mesto + ' ' + self.ulice + ' ' + str(self.cislo_popisne)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    action_flag = models.PositiveSmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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


class Dorucovatel(models.Model):
    dorucovatel_id = models.AutoField(primary_key=True)
    nazevfirmy = models.CharField(db_column='NazevFirmy', max_length=32)  # Field name made lowercase.
    telefonni_cislo = models.CharField(max_length=16)
    email = models.CharField(max_length=256)
    adresa = models.ForeignKey(Adresa, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dorucovatel'
    def __str__(self) -> str:
        return self.nazevfirmy


class Kategorie(models.Model):
    kategorie_id = models.AutoField(primary_key=True)
    nazev_kategorie = models.CharField(max_length=32)
    kat = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kategorie'
    def __str__(self) -> str:
        return self.nazev_kategorie


class KreditniKarta(models.Model):
    karta_id = models.AutoField(primary_key=True)
    cislo_karty = models.CharField(max_length=19)
    expirace = models.CharField(max_length=5)
    jmeno_karta = models.CharField(max_length=64)
    prijmeni_karta = models.CharField(max_length=32)
    cvc = models.IntegerField(db_column='CVC')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kreditni_karta'
    def __str__(self) -> str:
        return self.cislo_karty

class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    nazev = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'material'
    def __str__(self) -> str:
        return self.nazev


class MaterialProcentoProdukt(models.Model):
    material = models.OneToOneField(Material, models.DO_NOTHING, primary_key=True)
    produkt = models.ForeignKey('Produkt', models.DO_NOTHING)
    proceto = models.FloatField()

    class Meta:
        managed = False
        db_table = 'material_procento_produkt'
        unique_together = (('material', 'produkt'),)
    def __str__(self) -> str:
        return self.material + ' ' + self.produkt + ' ' + str(self.proceto)


class Objednavka(models.Model):
    objednavka_id = models.AutoField(primary_key=True)
    cislo_objednavky = models.CharField(max_length=8)
    dorucovatel = models.ForeignKey(Dorucovatel, models.DO_NOTHING)
    zakaznik = models.ForeignKey('Zakaznik', models.DO_NOTHING)
    celkova_cena = models.FloatField(blank=True, null=True)
    datum_koupe = models.DateField()
    datum_odeslani = models.DateField(blank=True, null=True)
    datum_doruceni = models.DateField(blank=True, null=True)
    datum_zaplaceni = models.DateField(blank=True, null=True)
    isdoruceno = models.IntegerField(db_column='isDoruceno', blank=True, null=True)  # Field name made lowercase.
    iszaplaceno = models.IntegerField(db_column='isZaplaceno', blank=True, null=True)  # Field name made lowercase.
    platba = models.ForeignKey('Platba', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'objednavka'
    def __str__(self) -> str:
        return str(self.objednavka_id) + ' ' + self.cislo_objednavky
    def generate_order_number(self):
        length = len(str(self.objednavka_id))
        str_len = 8-length
        s = ""
        for i in range(str_len):
            s+='0'
        s+=str(self.objednavka_id)
        self.cislo_objednavky = s

class ObjednavkaProdukt(models.Model):
    objednavka = models.OneToOneField(Objednavka, models.DO_NOTHING, primary_key=True)
    produkt = models.ForeignKey('Produkt', models.DO_NOTHING)
    kusu = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'objednavka_produkt'
        unique_together = (('objednavka', 'produkt'),)
    def __str__(self) -> str:
        return self.objednavka + ' ' + self.produkt + ' ' + str(self.kusu)
    

class Platba(models.Model):
    platba_id = models.AutoField(primary_key=True)
    typ_platby = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'platba'
    def __str__(self) -> str:
        return self.typ_platby

class ProductManager(models.Manager):
     def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Produkt(models.Model):
    produkt_id = models.AutoField(primary_key=True)
    nazev_produktu = models.CharField(max_length=64)
    velikost = models.CharField(max_length=3)
    barva = models.CharField(max_length=16)
    kratky_popis = models.CharField(max_length=64)
    dlouhy_popis = models.CharField(max_length=254)
    obrazek = models.ImageField(upload_to='images/')
    cena = models.FloatField()
    pocet_kusu = models.IntegerField()
    kategorie = models.ForeignKey(Kategorie, models.DO_NOTHING)
    is_active = models.BooleanField(default=True)
    products = ProductManager()

    class Meta:
        managed = False
        db_table = 'produkt'
    def __str__(self) -> str:
        return self.nazev_produktu
    
    def get_absolute_url(self):
        return reverse('store:produkt_detail',args=[self.produkt_id])

class ZakazikAccount(models.Model):
    zakazik_account_id = models.AutoField(primary_key=True)
    uzivatelske_jmeno = models.CharField(max_length=64)
    heslo = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'zakazik_account'
    def __str__(self) -> str:
        return self.uzivatelske_jmeno


class Zakaznik(models.Model):
    zakaznik_id = models.AutoField(primary_key=True)
    jmeno = models.CharField(max_length=64)
    prijmeni = models.CharField(max_length=32)
    email = models.CharField(max_length=256)
    telefoni_cislo = models.CharField(max_length=16)
    karta = models.ForeignKey(KreditniKarta, models.DO_NOTHING, blank=True, null=True)
    adresa = models.ForeignKey(Adresa, models.DO_NOTHING)
    account = models.ForeignKey(ZakazikAccount, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zakaznik'
    def __str__(self) -> str:
        return self.jmeno + ' ' + self.prijmeni
    
class Kosik(models.Model):
    kosik_id = models.AutoField(primary_key=True)
    zakaznik = models.ForeignKey('Zakaznik', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'kosik'


class KosikProdukt(models.Model):
    produkt = models.OneToOneField('Produkt', models.DO_NOTHING, primary_key=True)
    kosik = models.ForeignKey(Kosik, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'kosik_produkt'
        unique_together = (('produkt', 'kosik'),)
        