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
