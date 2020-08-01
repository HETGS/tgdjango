# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
'''For now I've put primary kays on everything, but I don't thik that primary_key and blank=True
makes sense on the same field. Might have to clean that up later.
There are also plenty of tables that the viewer does not need, e.g. the processing table.
For now I've left them in so that I can look around and compare things,
but if they are not needed here, they can be removed.

I also think that most of those fields should not have null and black set.
'''
from django.db import models


class Obsview(models.Model):
    id = models.IntegerField(primary_key=True)
    grpid = models.IntegerField(blank=True, null=True)
    srcid = models.IntegerField(blank=True, null=True)
    obsid = models.IntegerField()
    obi = models.IntegerField(blank=True, null=True)
    object = models.CharField(max_length=50, blank=True, null=True)
    target = models.CharField(max_length=50, blank=True, null=True)
    simbad_id = models.CharField(db_column='simbad_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ptype = models.CharField(db_column='pType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    instrument = models.CharField(max_length=7)
    grating = models.CharField(max_length=4)
    detector_aimpoint = models.CharField(max_length=50, blank=True, null=True)
    readmode = models.CharField(max_length=20, blank=True, null=True)
    datamode = models.CharField(max_length=50, blank=True, null=True)
    ra = models.FloatField(blank=True, null=True)
    decl = models.FloatField(blank=True, null=True)
    date_obs = models.DateTimeField(blank=True, null=True)
    proc_date = models.DateTimeField(blank=True, null=True)
    exposure = models.FloatField(blank=True, null=True)
    zo_method = models.CharField(max_length=10, blank=True, null=True)
    windowed = models.CharField(max_length=1, blank=True, null=True)
    extended = models.CharField(max_length=1, blank=True, null=True)
    multiple_sources = models.CharField(max_length=1, blank=True, null=True)
    pileup = models.IntegerField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    phase = models.IntegerField(blank=True, null=True)
    dtycycle = models.IntegerField(blank=True, null=True)
    ciao_version = models.CharField(max_length=11, blank=True, null=True)
    finzero_version = models.CharField(max_length=11, blank=True, null=True)
    caldb_version = models.CharField(max_length=11, blank=True, null=True)
    tgcat_version = models.CharField(max_length=11, blank=True, null=True)
    vv_sci = models.CharField(max_length=255, blank=True, null=True)
    review = models.CharField(max_length=2, blank=True, null=True)
    reject = models.CharField(max_length=1, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    meg_band = models.FloatField(blank=True, null=True)
    heg_band = models.FloatField(blank=True, null=True)
    leg_band = models.FloatField(blank=True, null=True)
    letg_acis_band = models.FloatField(blank=True, null=True)
    zeroth_order = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'obsview'


class Sourceview(models.Model):
    srcid = models.IntegerField(primary_key=True)
    object = models.CharField(max_length=50, blank=True, null=True)
    simbad_id = models.CharField(db_column='simbad_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ra = models.FloatField()
    decl = models.FloatField()
    ptype = models.CharField(db_column='pType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    other_types = models.TextField(blank=True, null=True)
    num_extractions = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'sourceview'


class Files(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    arc = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files'


class Image(models.Model):
    img_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    file_sfx = models.CharField(max_length=255)
    priority = models.IntegerField()
    detector = models.CharField(max_length=4, blank=True, null=True)
    grating = models.CharField(max_length=4, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image'


class Nedmatch(models.Model):
    srcid = models.IntegerField(blank=True, null=True, primary_key=True)
    ned = models.CharField(max_length=255, blank=True, null=True)
    diff = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nedmatch'


class News(models.Model):
    newsid = models.AutoField(primary_key=True)
    post_date = models.DateTimeField()
    poster = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class Obsid(models.Model):
    qid = models.IntegerField(blank=True, null=True)
    grpid = models.IntegerField(blank=True, null=True)
    srcid = models.IntegerField(blank=True, null=True)
    obsid = models.IntegerField(primary_key=True)
    obi = models.IntegerField(blank=True, null=True)
    target = models.CharField(max_length=50, blank=True, null=True)
    pi = models.CharField(max_length=50, blank=True, null=True)
    instrument = models.CharField(max_length=7)
    grating = models.CharField(max_length=4)
    detector_aimpoint = models.CharField(max_length=50, blank=True, null=True)
    readmode = models.CharField(max_length=20, blank=True, null=True)
    datamode = models.CharField(max_length=50, blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    ra = models.FloatField(blank=True, null=True)
    decl = models.FloatField(blank=True, null=True)
    ra_targ = models.FloatField(blank=True, null=True)
    dec_targ = models.FloatField(blank=True, null=True)
    date_obs = models.DateTimeField(blank=True, null=True)
    proc_date = models.DateTimeField(blank=True, null=True)
    exposure = models.FloatField(blank=True, null=True)
    events = models.IntegerField(blank=True, null=True)
    zo_method = models.CharField(max_length=10, blank=True, null=True)
    windowed = models.CharField(max_length=1, blank=True, null=True)
    extended = models.CharField(max_length=1, blank=True, null=True)
    multiple_sources = models.CharField(max_length=1, blank=True, null=True)
    pileup = models.IntegerField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    phase = models.IntegerField(blank=True, null=True)
    dtycycle = models.IntegerField(blank=True, null=True)
    ciao_version = models.CharField(max_length=11, blank=True, null=True)
    finzero_version = models.CharField(max_length=11, blank=True, null=True)
    caldb_version = models.CharField(max_length=11, blank=True, null=True)
    tgcat_version = models.CharField(max_length=11, blank=True, null=True)
    proc_version = models.IntegerField(blank=True, null=True)
    review = models.CharField(max_length=2, blank=True, null=True)
    grpflg = models.CharField(max_length=1, blank=True, null=True)
    reject = models.CharField(max_length=1, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    vv_sci = models.CharField(max_length=255, blank=True, null=True)
    vv_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obsid'


class OrigStdZo(models.Model):
    obsid = models.IntegerField(blank=True, null=True, primary_key=True)
    zo_m = models.CharField(max_length=1, blank=True, null=True)
    zo_x = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    zo_y = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    hetg_n_msk = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orig_std_zo'


class Pkgkart(models.Model):
    pkgid = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    types = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'pkgkart'


class Pkgque(models.Model):
    pkgid = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    temp_dir = models.CharField(max_length=255, blank=True, null=True)
    queue_time = models.DateTimeField(blank=True, null=True)
    completed = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=255, blank=True, null=True)
    request_ip = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pkgque'


class Process(models.Model):
    tgpid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255)
    pid = models.IntegerField()
    start_time = models.DateTimeField()
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'process'


class Queue(models.Model):
    qid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    obsid = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    host = models.CharField(max_length=50, blank=True, null=True)
    proc_dir = models.CharField(max_length=255, blank=True, null=True)
    coord = models.CharField(max_length=5, blank=True, null=True)
    x = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    y = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    zo_method = models.CharField(max_length=10, blank=True, null=True)
    msk_unit = models.CharField(max_length=6, blank=True, null=True)
    msk_zo_rad = models.FloatField(blank=True, null=True)
    msk_leg_width = models.FloatField(blank=True, null=True)
    msk_meg_width = models.FloatField(blank=True, null=True)
    msk_heg_width = models.FloatField(blank=True, null=True)
    xdisp_unit = models.CharField(max_length=7, blank=True, null=True)
    xdisp_src_min = models.FloatField(blank=True, null=True)
    xdisp_src_max = models.FloatField(blank=True, null=True)
    xdisp_down_min = models.FloatField(blank=True, null=True)
    xdisp_down_max = models.FloatField(blank=True, null=True)
    xdisp_up_min = models.FloatField(blank=True, null=True)
    xdisp_up_max = models.FloatField(blank=True, null=True)
    osort_lo = models.FloatField(blank=True, null=True)
    osort_hi = models.FloatField(blank=True, null=True)
    queue_time = models.DateTimeField()
    status_time = models.DateTimeField()
    runcfg = models.CharField(max_length=255, blank=True, null=True)
    error = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'queue'


class Source(models.Model):
    srcid = models.AutoField(primary_key=True)
    nextract = models.IntegerField(db_column='nExtract', blank=True, null=True)  # Field name made lowercase.
    object = models.CharField(max_length=50, blank=True, null=True)
    simbad_id = models.CharField(db_column='simbad_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ned_id = models.CharField(db_column='ned_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ra = models.FloatField()
    decl = models.FloatField()
    ptype = models.IntegerField(db_column='pType', blank=True, null=True)  # Field name made lowercase.
    reject = models.CharField(max_length=1, blank=True, null=True)
    ctype = models.CharField(db_column='cType', max_length=3, blank=True, null=True)  # Field name made lowercase.
    i2mass = models.CharField(max_length=1)
    idss1 = models.CharField(max_length=1)
    idss2 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'source'


class SpecProp(models.Model):
    id = models.IntegerField(blank=True, null=True, primary_key=True)
    label = models.CharField(max_length=20, blank=True, null=True)
    wmid = models.FloatField(blank=True, null=True)
    wlo = models.FloatField(blank=True, null=True)
    whi = models.FloatField(blank=True, null=True)
    count_rate = models.FloatField(blank=True, null=True)
    err_count_rate = models.FloatField(blank=True, null=True)
    photon_flux = models.FloatField(blank=True, null=True)
    err_photon_flux = models.FloatField(blank=True, null=True)
    energy_flux = models.FloatField(blank=True, null=True)
    err_energy_flux = models.FloatField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spec_prop'


class Src2Type(models.Model):
    srcid = models.IntegerField(primary_key=True)
    typeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'src2type'


class StdZo(models.Model):
    obsid = models.IntegerField(blank=True, null=True, priamry_key=True)
    std_zo_method = models.CharField(max_length=10, blank=True, null=True)
    std_coord = models.CharField(max_length=5, blank=True, null=True)
    std_x = models.FloatField(blank=True, null=True)
    std_y = models.FloatField(blank=True, null=True)
    std_hmsk = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'std_zo'


class TempObj(models.Model):
    object = models.CharField(max_length=55, blank=True, null=True)
    simbad = models.CharField(max_length=55, blank=True, null=True)
    srcid = models.IntegerField(blank=True, null=True, primary_key=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_obj'


class TempObj2(models.Model):
    object = models.CharField(max_length=55, blank=True, null=True, primary_key=True)
    simbad = models.CharField(max_length=55, blank=True, null=True)
    ra = models.FloatField(blank=True, null=True)
    decl = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_obj2'


class Tgcat(models.Model):
    pnum = models.AutoField(primary_key=True)
    param = models.CharField(unique=True, max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    editable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tgcat'


class Type(models.Model):
    typeid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    origin = models.CharField(max_length=25, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type'


class VvUser(models.Model):
    userid = models.AutoField(primary_key=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=41, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vv_user'
