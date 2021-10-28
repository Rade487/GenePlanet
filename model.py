from gene_planet import db


class Gene(db.Model):
    tablename = 'gene'
    id = db.Column(db.String(100), primary_key="True")
    chrom = db.Column(db.String(200))
    pos = db.Column(db.Integer)
    ref = db.Column(db.String(100))
    alt = db.Column(db.String(100))
    format = db.Column(db.String(100))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def init(self, chrom, pos, ref, alt, format):
        self.chrom = chrom
        self.pos = pos
        self.ref = ref
        self.alt = alt
        self.format = format


class Sample1(db.Model):
    tablename = 'sample1'
    id = db.Column(db.String(100), primary_key="True")
    chrom = db.Column(db.String(200))
    pos = db.Column(db.Integer)
    ref = db.Column(db.String(100))
    alt = db.Column(db.String(100))
    qual = db.Column(db.String(100))
    filter = db.Column(db.String(100))
    info = db.Column(db.String(100))
    format = db.Column(db.String(100))
    sample1 = db.Column(db.String(100))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def init(self, chrom, pos, ref, alt, format):
        self.chrom = chrom
        self.pos = pos
        self.ref = ref
        self.alt = alt
        self.format = format


class Sample2(db.Model):
    tablename = 'sample2'
    id = db.Column(db.String(100), primary_key="True")
    chrom = db.Column(db.String(200))
    pos = db.Column(db.Integer)
    ref = db.Column(db.String(100))
    alt = db.Column(db.String(100))
    qual = db.Column(db.String(100))
    filter = db.Column(db.String(100))
    info = db.Column(db.String(100))
    format = db.Column(db.String(100))
    sample2 = db.Column(db.String(100))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def init(self, chrom, pos, ref, alt, format):
        self.chrom = chrom
        self.pos = pos
        self.ref = ref
        self.alt = alt
        self.format = format
