from app import db


class Gene(db.Model):
    tablename = 'gene'
    id = db.Column(db.String(100), primary_key="True")
    chrom = db.Column(db.String(200))
    pos = db.Column(db.Integer)
    ref = db.Column(db.String(100))
    alt = db.Column(db.String(100))
    info = db.Column(db.String(100))

    def init(self, chrom,  pos, ref, alt, info):
        self.chrom = chrom
        self.pos = pos
        self.ref = ref
        self.alt = alt
        self.info = info
